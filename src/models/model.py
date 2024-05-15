
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested
from enum import Enum as pythonEnum
from sqlalchemy import Enum
from json import JSONEncoder

db = SQLAlchemy()

#Skill table
class Skill(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nameSkill = db.Column(db.String(15), nullable=False)
    levelSkill = db.Column(db.Integer, nullable = False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)

#Employee table
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(70), nullable = False)
    position = db.Column(db.String(70))
    email = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    phoneNumber = db.Column(db.String(20))
    skills = db.relationship("Skill", backref = 'employee', lazy= True) 

class SkillSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Skill
        load_instance = True

class EmployeeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        load_instance = True
    
    id = fields.String()
    skills = Nested('SkillSchema', many=True)








 