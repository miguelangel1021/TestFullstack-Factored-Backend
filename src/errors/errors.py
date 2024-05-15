
class ApiError(Exception):
    code = 422
    description = "Default message"

class NotFound(ApiError):
    code = 404
    description = "No information was found with the fields submitted."

class ResourcesRequired(ApiError):
    code = 400
    description = "There are some required fields please validate."

class ResourcesAlreadyExist(ApiError):
    code = 412
    description = "The employee already exist in the DB."