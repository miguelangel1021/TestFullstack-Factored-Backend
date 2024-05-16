# Test Fullstack -Factored-Backend
To run the project first you need to clone the repo locally and have installed and running the Docker Desktop application. After cloning the repository, open cmd or windows terminal, and go to the root folder of the project, in this case TestFullstack-Factored-Backend (use cd name_folder to go to the correct address). Once you are in the correct folder, type in the cmd the instruction “docker build -t backend .” (backend can change, it is the name you want to assign to the image). This will create an image that can be run in a container. Once the build process is finished, you must write the instruction “docker run -it --publish 5000:3000 backend”. Finally, you can access the service using localhost and port 5000, for example you can make a request from postman to create an employee. 

To create an employee, you must execute the following request:

method: POST
URL: http://localhost:5000/employees
body: {
    "name" : "Miguel Angel Cardenas Cardenas",
    "position": "Engineering intern",
    "email": "ma.cardenasc1@example.com",
    "password": "Karol0516_m",
    "phoneNumber": "3508601521",
    "skills": {
        "PYTHON": 8,
        "SQL" : 6,
        "JAVA" : 7,
        "SPARK" : 3,
        "REACT" : 7,
        "BACKEND" : 8
    }

}

The service automatically creates 2 test records to be used by the frontend, the records are the following: 
email: ma.cardenasc1@example.com
password: password

email: ma.cardenasc1@example.com
password: password

email: john21@example.com
password: password

