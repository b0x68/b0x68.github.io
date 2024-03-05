+++
title = "Configure a container to start automatically as a systemd service"
date = "2024-02-16T11:55:10-05:00"
author = "root"
cover = "auto-start.pnng"
tags = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
keywords = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
description = "How to configure a container to start automatically as a systemd service."
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Red Hat Certified Systems Administrator Exam 200 Objective: "Configure a container to start automatically as a systemd service"

In today's world of ever-growing virtualization and cloud computing, containerization has become a popular approach for deploying and managing applications. And with the rise of container orchestration tools like Kubernetes, the demand for professionals who can configure and manage containers is increasing rapidly. As a Red Hat Certified Systems Administrator, it is important to have a good understanding of containerization and its tools. In this tutorial, we will go in-depth to explore how to configure a container to start automatically as a systemd service.

## What is systemd?

Systemd is an init system and service manager for Linux operating systems. It is designed to provide a more powerful and efficient way of starting and managing services compared to the traditional init system. Systemd is responsible for starting, stopping, and supervising system services, including containers. It is also responsible for managing system resources, such as power management, logging, and device management.

## What is a container?

Containers are lightweight, standalone, and executable packages that encapsulate a piece of software and all its dependencies. They are designed to run isolated applications on a single host machine without requiring a virtual machine. Containers offer a faster, more portable, and efficient way of deploying applications, making them a popular choice among developers and system administrators.

## Setting up a container to start as a systemd service

Before we dive into configuring a container to start automatically as a systemd service, let's first make sure we have the necessary prerequisites in place:

- A Linux operating system with systemd installed (In this tutorial, we will be using Red Hat Enterprise Linux)
- Docker or Podman (container engines)
- A container image to use (In our example, we will be using a web application container image)

Once we have all the necessary prerequisites, we can move on to the steps to configure a container to start as a systemd service.

### Step 1: Create a container image

The first step is to create a container image for our web application. If you already have a container image, you can skip this step. Otherwise, we will use the following command to create a basic web application using the "index.html" file:

`mkdir html_files`

`vi html_files/index.html` (Add some basic HTML code here, like "Hello from my web application!")

`docker build -t mywebapp:1.0 .`

### Step 2: Create a systemd unit file

A systemd unit file is a configuration file that describes how a systemd service should be managed. We will create a unit file in the "/etc/systemd/system" directory with the name "mywebapp.service." We can use any text editor to create the file, but for simplicity, we will use the "vi" editor:

`sudo vi /etc/systemd/system/mywebapp.service`

Within this file, we need to provide some information, like the service name, description, recommended resources to be used, and command-line options. We will use the following template for our unit file:

``` 
[Unit]
Description= My Web Application Service
Requires=docker.service
After=docker.service

[Service]
ExecStart=/usr/bin/docker run -p 80:80 mywebapp:1.0
Restart=always

[Install]
WantedBy=multi-user.target 
```

Now, let's break down the different sections of this unit file:

- `[Unit]`: This section provides general information about the service, like the name and description.
- `Requires`: This option specifies that our service depends on the docker service, and it will not start until the docker service has started successfully.
- `After`: This option sets the order in which services are started. In this case, we want our service to start after the docker service has started.
- `[Service]`:
- `ExecStart`: This is the main command that will be executed to start our container. In this case, we are using Docker to run our container and expose port 80 for our web application. Make sure to use the appropriate command for the container engine you are using.
- `Restart`: This option specifies that the service should be restarted if it fails for any reason.
- `[Install]`: This section specifies where the service should be located in the multi-user target, which is responsible for starting services during boot time.

### Step 3: Start the service and verify its status

Now that we have our unit file configured, we can start our service using the following command:

`sudo systemctl start mywebapp`

We can also verify the status of our service using the following command:

`sudo systemctl status mywebapp`

If the service has started successfully, we should see a "active (running)" status. If there are any errors, the status will show as "failed," and we can check the logs for more information.

### Step 4: Enable the service to start on boot

If we want our service to start automatically every time the system boots, we can enable it using the following command:

`sudo systemctl enable mywebapp`

Now, the next time our system boots, the service will start automatically, and we won't have to start it manually.

## Conclusion

In this tutorial, we went in-depth into configuring a container to start automatically as a systemd service. We started by understanding what systemd and containers are and their importance in today's world of virtualization. Then, we walked through the steps to create a unit file and start our container service. By the end of this tutorial, we should have a clear understanding of how to configure a container to start automatically as a systemd service, which is an essential skill for any Red Hat Certified Systems Administrator. 
