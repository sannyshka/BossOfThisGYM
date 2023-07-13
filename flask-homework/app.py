from flask import Flask, jsonify, render_template
import logging
from dotenv import load_dotenv
from config import AppConfig
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

db = SQLAlchemy()

app = Flask(__name__)

app.config.from_object(AppConfig)
db.init_app(app)

# Logging setup
logging.basicConfig(level=logging.INFO)

@app.route('/')
def hello_world():
    return 'Hello World!'

# The endpoint that returns "Hello, world"
@app.route('/hello', methods=['GET'])
def hello():
    app.logger.info('Hello endpoint was accesed')
    return 'Hello, world'


# The endpoint that returns HTML
@app.route('/html', methods=['GET'])
def html():
    app.logger.info('HTML endpoint was accesed')
    return render_template('index.html')


# The endpoint that returns JSON
@app.route('/json', methods=['GET'])
def json():
    app.logger.info('JSON endpoint was accesed')
    data = {'message': 'Hello, world!'}
    return jsonify(data)

from views import *
from models import *

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=AppConfig.HOST,
            port=AppConfig.PORT,
            debug=AppConfig.DEBUG)