+++
title = "Perform basic container management such as running, starting, stopping, and listing running"
date = "2024-02-16T11:54:48-05:00"
author = "root"
cover = "stoprunwalk.png"
tags = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
keywords = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
description = "Containers are a lightweight and efficient way to package and run applications. They provide a stable and consistent environment for applications to run, making it easier to deploy and manage them. As a system administrator, it is essential to have a good understanding of container management to be able to effectively manage and troubleshoot applications in a Red Hat environment."
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++

#
# Introduction to Container Management on Red Hat: 
Containers are a lightweight and efficient way to package and run applications. They provide a stable and consistent environment for applications to run, making it easier to deploy and manage them. As a system administrator, it is essential to have a good understanding of container management to be able to effectively manage and troubleshoot applications in a Red Hat environment.

In this tutorial, we will cover the Red Hat Certified Systems Administrator Exam 200 objective: "Perform basic container management such as running, starting, stopping, and listing running". We will go through the various commands and techniques required to perform basic container management in Red Hat, providing you with a comprehensive guide to mastering this objective.

# Objectives:

- Understand the core concepts of containers in Red Hat.
- Learn how to run containers on Red Hat.
- Explore how to start and stop containers.
- Understand how to list running and stopped containers.
- Troubleshoot common issues related to container management.

# Core Concepts of Containers in Red Hat:
Before we dive into the specifics of container management, it is essential to have a good understanding of the core concepts of containers in Red Hat. 

Containers are lightweight and isolated environments that run on top of a host operating system. They encapsulate all the libraries and dependencies required for an application to run, providing a consistent runtime environment. This isolation ensures that applications can run on any host system without having to worry about compatibility issues or dependencies.

In Red Hat, containers are managed through a container engine called "podman". Podman can run both rootless and root-owned containers, making it a flexible and secure tool for container management. It also allows for easy creation, deployment, and management of containers using a simple command-line interface.

# Running Containers on Red Hat:
The first step in container management is to run a container on a Red Hat system. To run a container using podman, you can use the following command:
```
$ podman run [options] image [command [args...]]
```
Let's break down the options in this command:

- The "run" keyword instructs podman to run a container.
- The [options] parameter specifies any additional configuration options for the container. Some commonly used options include --detach (to run the container in the background), --name (to give the container a specific name), and --publish (to expose ports from the container to the host).
- The "image" parameter specifies the image that you want to use to run the container. Red Hat provides a plethora of images in its registry, which you can access through the "podman search" command.
- The [command [args...]] parameter allows you to specify a command to run within the container. If not specified, the container will run the default command defined in the image's Dockerfile.

For example, let's run a container using the "nginx" image from the Red Hat registry and expose port 80 to the host:
```
$ podman run --detach --name webserver -p 80:80 nginx 
```
This command will pull the latest version of the "nginx" image, create a container named "webserver", and expose container port 80 to host port 80.

# Starting and Stopping Containers:
Once you have a container running, you may need to start or stop it at any given time. To start a stopped container, use the following command:
```
$ podman start <container-name>
```
Similarly, to stop a running container, use the following command:
```
$ podman stop <container-name>
```
You can also use the container's ID instead of its name in these commands.

# Listing Running and Stopped Containers:
To list all the running containers on a Red Hat system, you can use the following command:
```
$ podman ps
```
This command will display a list of all the running containers, along with their name, ID, and other relevant information.

To list all the stopped containers on a Red Hat system, use the following command:
```
$ podman ps -a
```
This command will display a list of both running and stopped containers.

# Troubleshooting Common Container Management Issues:
Like any other technology, container management on Red Hat may encounter some common issues that you should be aware of. These issues can range from problems starting or stopping containers to issues with network connectivity.

One of the most common troubleshooting steps is to check the logs of the container to identify any errors or issues. You can use the following command to view the logs of a container:
```
$ podman logs <container-name>
```

If you encounter any errors related to port binding or connectivity, you may need to check if the ports are properly exposed and opened. You can use the following commands to check and open ports on a Red Hat system:
```
$ podman port <container-name>
$ sudo firewall-cmd --add-port=<port-number>/tcp --permanent
$ sudo firewall-cmd --reload
```

Additionally, you can also use various debugging techniques such as running containers in interactive mode, executing commands within a container, or inspecting the container's network settings to troubleshoot and resolve any issues.

# Conclusion:
In this tutorial, we have covered the Red Hat Certified Systems Administrator Exam 200 objective: "Perform basic container management such as running, starting, stopping, and listing running". We went through the core concepts of containers in Red Hat, learned how to run and start/stop containers, and explored techniques to troubleshoot common issues related to container management.

By understanding and mastering container management on Red Hat, you will be well-equipped to deploy and manage applications in a Red Hat environment, making you a valuable asset as a Red Hat Certified Systems Administrator.
