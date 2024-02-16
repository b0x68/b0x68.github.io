+++
title = "Build a container from a Containerfile"
date = "2024-02-16T10:39:24-05:00"
author = "root"
cover = ""
tags = ["`containerfile`.", "commands", "images", "container", "images`", "command.", "terminal,", "process."]
keywords = ["containers", "command", "container,", "commands", "system.", "packages", "process", "container:"]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# How to Build a Container from a Containerfile in Red Hat Certified Systems Administrator Exam

Building a container is a crucial skill for any Red Hat Certified Systems Administrator. It allows you to create a lightweight and portable environment for running applications and services. In this tutorial, we will guide you through the process of building a container from a Containerfile in the Red Hat Certified Systems Administrator Exam.

## 1. Introduction to Containerfiles

A Containerfile is a text document that contains a set of instructions for building a container image. It is similar to a Dockerfile, but it is specific to the Buildah tool used in the Red Hat Certified Systems Administrator Exam. A Containerfile is divided into multiple sections, each containing different instructions for building the container image.

## 2. Understanding the sections of a Containerfile

Before we begin writing our Containerfile, let's understand the different sections it contains. These sections are:

- **FROM**: This section specifies the base image used for your container. It can be any existing image, such as Fedora, CentOS, or Ubuntu.
- **RUN**: This section contains commands that will be executed during the build process.
- **ENV**: This section allows you to set environment variables in the container.
- **WORKDIR**: This section specifies the working directory in the container.
- **EXPOSE**: This section exposes specific ports in the container.
- **CMD**: This section defines the command that will be executed when the container runs.

## 3. Creating a simple Containerfile

Let's start by creating a simple Containerfile for our example. Open a text editor and create a new file called `Containerfile`.

**Important:** Make sure the file is named `Containerfile`, with a capital "C" and no file extension.

Now, add the following content to your `Containerfile`:

```bash
FROM ubuntu:20.04

RUN apt-get update \
    && apt-get install -y python3-pip \
    && pip install flask

ENV FLASK_APP app.py
WORKDIR /app

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
```

Let's break down what each section of this Containerfile is doing:

- **FROM**: We are using the Ubuntu 20.04 image as our base image.
- **RUN**: We are using the `apt-get` command to update our packages and install `python3-pip`. Then, we use `pip` to install the `flask` library.
- **ENV**: We are setting the environment variable `FLASK_APP` to point to our `app.py` file.
- **WORKDIR**: We are setting the working directory inside the container to be `/app`.
- **EXPOSE**: We are exposing port `5000` in our container.
- **CMD**: We are defining the command that will be executed when the container runs, which is `flask run` with the `--host=0.0.0.0` flag.

## 4. Building the container

Now that we have our Containerfile ready, we can build our container using the `buildah` command. Follow these steps to build your container:

1. Open the terminal or command prompt and navigate to the directory where you saved your `Containerfile`.
2. Run the command `sudo buildah bud -t myapp .` This will build the container image and tag it with the name `myapp`.

If everything goes well, you should see the message `Successfully tagged myapp:latest` in your terminal.

## 5. Verifying the container

To verify that our container has been built successfully, we can use the `buildah images` command. This will list all the container images on the system. You should see your newly built image `myapp` in the list.

## 6. Running the container

To run the container, we can use the `buildah run` command. Follow these steps to run your container:

1. In the terminal, run the command `sudo buildah run -p 5000:5000 myapp`. This will start the container and map the port `5000` from the container to the host.
2. Open your web browser and navigate to `http://localhost:5000`. You should see a hello world message from the running container.

## 7. Conclusion

Congratulations, you have successfully built a container from a Containerfile in the Red Hat Certified Systems Administrator Exam. This is just a simple example; there are many more things you can do with Containerfiles to build more complex and powerful containers. We encourage you to explore and practice building containers from Containerfiles to prepare for the exam. Best of luck!