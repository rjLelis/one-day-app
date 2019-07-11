import pymongo, json

def get_config(config_item):
    with open('py/config.json', 'r') as f:
        config = json.loads(f.read())
    return config[config_item]


def db_connection(db_collection_name):
    db_uri = get_config('dburi')
    db_name = 'test'
    client = pymongo.MongoClient(db_uri)
    db = client[db_name]
    db_collection = db[db_collection_name]
    return db_collection


def save_data(db_collection_name, data):
    db_collection = db_connection(db_collection_name)
    id = db_collection.insert_one(data).inserted_id
    return str(id)