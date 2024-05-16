from flask import jsonify, Blueprint, request
from ..commands.create_employee import CreateEmployee
from ..commands.login import Login
from ..errors.errors import ResourcesRequired
import hashlib


request_blueprint = Blueprint("requests", __name__)

@request_blueprint.route('/employees', methods = ['POST'])
def create():
    json = request.get_json()
    employee = CreateEmployee(json.get("name"),
                              json.get("position"),
                              json.get("email"), 
                              json.get("password"),
                              json.get("phoneNumber"),
                              json.get("skills"),
                              json.get("department")).execute()
    return jsonify(employee)

@request_blueprint.route("/employees/login", methods = ['POST'])
def login():
    json = request.get_json()
    employee = Login(json.get("email"),
                     json.get("password")).execute()
    return jsonify(employee)

@request_blueprint.route('/employees/ping', methods = ['GET'])
def ping():
    return "pong", 200