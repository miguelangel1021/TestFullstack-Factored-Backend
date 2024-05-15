FROM python:3.10
WORKDIR /employee

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r /app/Pipfile

# Make port 5000 available to the world outside this container
EXPOSE 3000

# Define environment variable
ENV FLASK_APP=/app/src/main.py

CMD /bin/bash -c "sleep 2 && flask run --host=0.0.0.0 -p 3000"