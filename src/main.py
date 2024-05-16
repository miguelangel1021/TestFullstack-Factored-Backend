from flask import Flask, jsonify
from .blueprints.requests import request_blueprint
from .errors.errors import ApiError
from flask_sqlalchemy import SQLAlchemy
from .models.model import db, Employee, Skill
from .validations.validations import get_password
import hashlib
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

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
  
@app.before_first_request
def create_initial_records():
    with app.app_context():
        employee1 = Employee(name="John Doe", email="john21@example.com", 
                            password= hashlib.sha256(get_password("password", "john21@example.com").encode()).hexdigest(),
                            position = "Engineering intern", phoneNumber = "3508601521", department = 'IT Department')
        
        employee2 = Employee(name="Miguel Cardenas", email="ma.cardenasc1@example.com", 
                             password= hashlib.sha256(get_password("password", "ma.cardenasc1@example.com").encode()).hexdigest(), 
                             position = "Engineering intern", phoneNumber = "3508601521", department = 'IT Department')
        
        db.session.add_all([employee1, employee2])
        db.session.commit()

        skill1 = Skill(nameSkill="Python", levelSkill=10, employee_id=employee1.id)
        skill2 = Skill(nameSkill="JavaScript", levelSkill=5, employee_id=employee1.id)
        skill3 = Skill(nameSkill="SQL", levelSkill=7, employee_id=employee1.id)
        skill4 = Skill(nameSkill="Spark", levelSkill=2, employee_id=employee1.id)
        skill5 = Skill(nameSkill="React", levelSkill=5, employee_id=employee1.id)
        skill6 = Skill(nameSkill="Backed", levelSkill=6, employee_id=employee1.id)
        db.session.add_all([skill1, skill2, skill3, skill4,skill5, skill6])
        db.session.commit()
        
        skill12 = Skill(nameSkill="Python", levelSkill=10, employee_id=employee2.id)
        skill22 = Skill(nameSkill="JavaScript", levelSkill=7, employee_id=employee2.id)
        skill32 = Skill(nameSkill="SQL", levelSkill=6, employee_id=employee2.id)
        skill42 = Skill(nameSkill="Spark", levelSkill=0, employee_id=employee2.id)
        skill52 = Skill(nameSkill="React", levelSkill=7, employee_id=employee2.id)
        skill62 = Skill(nameSkill="Backed", levelSkill=9, employee_id=employee2.id)
        db.session.add_all([skill12, skill22, skill32, skill42,skill52, skill62])
        db.session.commit()

