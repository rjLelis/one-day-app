from flask import Flask, render_template, request
import py.formCadastro as form
# import py.authentication as auth
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

@application.route('/')
def main():
    return render_template('index.html')


@application.route('/saveNewUser', methods=['POST'])
def save_new_user():
    # authenticate()
    return form.save_user(request)


@application.route('/listForm', methods=['POST'])
def list_form():
    # authenticate()
    return form.list_cadastro()


@application.route('/saveForm', methods=['POST'])
def save_form():
    # authenticate()
    return form.save_cadastro(request)


""" def authenticate():
    login = request.args.get('login')
    userid = request.args.get('userid')
    token = request.args.get('token')
    if login == 'fb':
        return verify_fb_token(token, userid)
    elif login == 'gl':
        return verify_gl_token(token, userid)
 """

if __name__ == "__main__":
    application.run(debug=True)