# Tech Tutorial: Manage containers

## Introduction

In this tutorial, we will focus on how to run a service inside a container. This process is fundamental in the world of software development, particularly in DevOps practices and microservices architecture. Containers offer a lightweight, portable, and consistent environment for applications, ensuring that they run the same way on any system.

We will use Docker, one of the most popular containerization platforms, to demonstrate how to containerize a simple web service. Docker allows applications to run in isolated environments, and it uses containers to achieve this.

## Prerequisites

Before we begin, make sure you have the following installed:
- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Basic knowledge of command-line tools and Docker concepts (images, containers, Dockerfile)

## Step-by-Step Guide

### Step 1: Create a Simple Web Service

First, we'll create a simple web service using Python and Flask. Flask is a lightweight WSGI web application framework.

1. **Create a new directory for your project:**

   ```bash
   mkdir flask-app
   cd flask-app
   ```

2. **Create a Python virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Flask:**

   ```bash
   pip install Flask
   ```

4. **Create a new file `app.py` and add the following Python code:**

   ```python
   from flask import Flask
   app = Flask(__name__)

   @app.route('/')
   def hello_world():
       return 'Hello, World!'

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
   ```

   This code creates a basic web server that returns "Hello, World!" when accessed at the root URL.

### Step 2: Containerize the Web Service

Now that we have our web service, let's containerize it using Docker.

1. **Create a Dockerfile in the same directory as your `app.py`:**

   ```Dockerfile
   # Use an official Python runtime as a parent image
   FROM python:3.8-slim

   # Set the working directory in the container
   WORKDIR /usr/src/app

   # Copy the current directory contents into the container at /usr/src/app
   COPY . /usr/src/app

   # Install any needed packages specified in requirements.txt
   RUN pip install --no-cache-dir -r requirements.txt

   # Make port 5000 available to the world outside this container
   EXPOSE 5000

   # Define environment variable
   ENV NAME World

   # Run app.py when the container launches
   CMD ["python", "app.py"]
   ```

2. **Create a `requirements.txt` file that lists Flask:**

   ```text
   Flask
   ```

3. **Build the Docker image:**

   ```bash
   docker build -t flask-app .
   ```

4. **Run the Docker container:**

   ```bash
   docker run -p 4000:5000 flask-app
   ```

   This command runs the container and maps port 5000 inside the container to port 4000 on your host machine.

### Step 3: Access the Web Service

Open a web browser and visit `http://localhost:4000/`. You should see "Hello, World!" displayed. This confirms that your service is running inside the container.

## Conclusion

You have successfully containerized a simple web service using Docker. This tutorial covered the essentials of writing a Dockerfile, building a Docker image, and running a container. Containers encapsulate the environment needed to run an application, making it easier to manage dependencies and deployments. As you advance, consider exploring more complex applications, handling persistent storage, and container orchestration with Kubernetes or Docker Swarm.