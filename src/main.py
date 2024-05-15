from flask import Flask, jsonify
from .blueprints.requests import request_blueprint
from .errors.errors import ApiError
from flask_sqlalchemy import SQLAlchemy
from .models.model import db


app = Flask(__name__)

database_uri = 'sqlite:///bakendDB.db'
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(request_blueprint)

@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
      "mssg": err.description,
    }
    return jsonify(response), err.code

with app.app_context():
    db.create_all()

