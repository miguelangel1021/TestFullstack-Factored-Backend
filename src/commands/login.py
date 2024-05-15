from ..models.model import Employee, EmployeeSchema
from .base_command import BaseCommannd
from ..errors.errors import NotFound, ResourcesRequired
from ..validations.validations import get_password, validate_empty, valid_email
import hashlib


employee_schema = EmployeeSchema()

class Login(BaseCommannd):
    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    def execute(self):
        if validate_empty(self.email) or validate_empty(self.password) or not valid_email(self.email):
            raise ResourcesRequired
        employee = Employee.query.filter(Employee.email == self.email).first()
        if employee is not None:
            if(employee.password != hashlib.sha256(get_password(self.password, employee.email).encode()).hexdigest()):
                raise NotFound
            return employee_schema.dump(employee)
        else:
            raise NotFound