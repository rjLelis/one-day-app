import pymongo
import py.dbconnect as db
from bson.json_util import dumps
from urllib.parse import unquote
import datetime

db_collection_name = 'messages'


def list_cadastro():
    db_collection = db.db_connection(db_collection_name)
    cursor = db_collection.find().sort('timestamp', -1).limit(10)
    return dumps(cursor)


def save_cadastro(request):
    data = {
        'contact': unquote(request.args.get('contact')),
        'message': unquote(request.args.get('message')),
        'userid': unquote(request.args.get('userid')),
        'latitude': unquote(request.args.get('latitude')),
        'longitude': unquote(request.args.get('longitude')),
        'timestamp': datetime.datetime.utcnow()
    }
    return db.save_data(db_collection_name, data)