from flask import Flask, render_template
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

@application.route('/')
def main():
    return render_template('index.html')


if __name__ == "__main__":
    application.run(debug=True)