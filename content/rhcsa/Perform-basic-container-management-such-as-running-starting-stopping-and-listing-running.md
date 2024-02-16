+++
title = "Perform basic container management such as running, starting, stopping, and listing running"
date = "2024-02-16T10:39:35-05:00"
author = "root"
cover = ""
tags = ["system,", "container's", "containerization", "system.", "system's", "images**:", "image.", "<container"]
keywords = ["container,", "tasks", "**podman**:", "systems", "containers,", "image.", "command,", "system."]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Red Hat Certified Systems Administrator Exam 200 Objective: Perform Basic Container Management

In today's digital world, containerization has become an essential aspect of software development and deployment. Red Hat Certified Systems Administrator (RHCSA) certification is a well-recognized and highly sought-after certification in the IT industry. One of the objectives of the RHCSA exam (Exam 200) is to test your knowledge and skills in basic container management. This tutorial will provide in-depth information on this objective to help you prepare and ace the exam.

## Understanding Containers
Before diving into the specifics of container management, it's important to have a clear understanding of what containers are. Containers are a lightweight and portable way of packaging, deploying, and running applications. In simple terms, containers are self-contained and isolated environments that contain all the necessary components and dependencies for an application to run. This allows applications to run consistently and reliably, regardless of the underlying computing environment.

## Container Management Tools
Red Hat offers various tools for container management, depending on your specific needs and environment. Some of the popular tools include:

- **Docker**: Docker is a popular open-source platform for building and running containers. It provides a user-friendly command-line interface (CLI) for managing containers.
- **Podman**: Podman is a container management tool that is native to Red Hat Enterprise Linux (RHEL) since version 7. Podman allows you to run containers in a non-daemon mode, making it a secure alternative to Docker.
- **Kubernetes**: Kubernetes is an advanced container orchestration tool for managing multiple containers at scale. It allows for easy scaling, networking, and load balancing of containers.

For the purpose of this tutorial, we will focus on using Docker for basic container management.

## Basic Docker Commands
To start managing containers with Docker, you first need to have Docker installed and running on your system. Once you have Docker set up, you can use the following basic commands to manage containers:

- **docker pull**: This command allows you to download the container image from a Docker registry.
- **docker run**: Using this command, you can create and start a new container from a specified image.
- **docker start**: This command starts an existing container that has been stopped.
- **docker stop**: This command stops a running container but does not remove it.
- **docker rm**: You can use this command to remove a stopped container from your system.
- **docker ps**: This command lists all the running containers on your system.
- **docker images**: Using this command, you can view all the downloaded images on your system.

## Starting and Stopping Containers
To perform basic container management, you need to know how to start and stop containers. Let's go through the steps for starting and stopping a container using Docker:

### Starting a Container
1. First, open your terminal or command-line interface (CLI) and ensure Docker is running.
2. Use the **docker pull** command to download a container image from a registry.
```
$ docker pull nginx
```
3. Once the download is complete, use the **docker run** command to create and start a new container from the downloaded image.
```
$ docker run -d -p 8080:80 nginx
```
In the above command, **-d** flag runs the container in detached mode, and **-p** flag exposes the container's port 80 to your system's port 8080.

4. To verify that the container is running, you can use the **docker ps** command. You should see your container in the list of running containers with its container ID, image name, status, and other details.

### Stopping a Container
1. To stop a running container, use the **docker stop** command and provide the container ID or name as the argument.
```
$ docker stop <container ID or name>
```
2. To verify that the container has stopped, you can use the **docker ps** command. The stopped container should no longer appear on the list.

## Listing Running Containers
To view a list of all the running containers on your system, you can use the **docker ps** command. This command displays various details such as container ID, image name, status, ports, etc. However, if you want to view detailed information about all the containers on your system, including the stopped ones, you can use the **docker ps -a** command.

## Conclusion
Managing containers involves performing various tasks such as starting, stopping, and listing running containers. In this tutorial, we have covered the basics of container management using Docker, which is a popular container management tool. To become proficient in managing containers, it's essential to practice using these commands and understand how they work. We hope this tutorial has helped you gain a better understanding of basic container management and prepared you for the RHCSA Exam 200 objective. Good luck on your certification journey!

 