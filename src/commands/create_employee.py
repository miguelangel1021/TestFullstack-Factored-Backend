from .base_command import BaseCommannd
from sqlalchemy import or_
from ..errors.errors import ResourcesRequired, ResourcesAlreadyExist
from ..models.model import  db, Employee, EmployeeSchema, Skill
import hashlib
from ..validations.validations import validate_empty,get_password,valid_email

employee_schema = EmployeeSchema()

class CreateEmployee(BaseCommannd):
    def __init__(self, name, position, email, password, phoneNumber, skills):
        self.name = name
        self.position = position
        self.email = email
        self.password = password
        self.phoneNumber = phoneNumber
        self.skills = skills
    
    def execute(self):
        if validate_empty(self.name) or validate_empty(self.position) or validate_empty(self.email) or not valid_email(self.email) or validate_empty(self.password) or validate_empty(self.phoneNumber):
            raise ResourcesRequired
        employee = Employee.query.filter(or_(Employee.email == self.email)).first()
        if employee is None:
            new_employee = Employee(name = self.name, position = self.position, email = self.email, password =hashlib.sha256(get_password(self.password, self.email).encode()).hexdigest(), phoneNumber = self.phoneNumber)
            db.session.add(new_employee)
            db.session.commit()
            for skill in self.skills.keys():
                new_skill = Skill(nameSkill = skill, levelSkill = self.skills[skill], employee_id = new_employee.id)
                db.session.add(new_skill)
                db.session.commit()
            return employee_schema.dump(new_employee)  
        else:
            raise ResourcesAlreadyExist      


