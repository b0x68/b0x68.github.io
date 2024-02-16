+++
title = "Configure a container to start automatically as a systemd service"
date = "2024-02-16T10:39:58-05:00"
author = "root"
cover = ""
tags = ["mycontainer-image", "boot", "command-line", "file", "security", "services", "containerization", "dockerfile:"]
keywords = ["dockerfile:", "image:", "`mycontainer`,", "`mycontainer`", "containers.", "file", "system.", "`dockerfile`"]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Tutorial: Configuring a container as a systemd service on Red Hat Certified Systems Administrator Exam

In this tutorial, we will walk through the process of configuring a container to start automatically as a systemd service on the Red Hat Certified Systems Administrator Exam. By completing this objective, you will gain the necessary knowledge and skills to successfully configure and manage containers as systemd services in a Red Hat environment. 

## Prerequisites
- A basic understanding of containers and containerization. 
- Familiarity with Red Hat Enterprise Linux (RHEL) and its command-line interface (CLI).
- Root or sudo access to RHEL.

## Step 1: Install and Configure Docker
The first step in configuring a container as a systemd service is to install and configure Docker on your RHEL system. Docker is a popular containerization platform that enables you to create and manage containers. Follow the below steps to install and configure Docker on your RHEL system:

1. Update your system by running the command `yum update`.
2. Install Docker by running the command `yum install docker`.
3. Start the Docker service by running the command `systemctl start docker`.
4. Enable the Docker service to automatically start at boot by running the command `systemctl enable docker`.

## Step 2: Create a Container Image
Next, we need to create a container image that will be used to start our systemd service. A container image is a single file that contains all the necessary files and dependencies required to run an application in a container. Follow these steps to create a simple container image using a Dockerfile:

1. Create a new directory for your container by running the command `mkdir mycontainer`.
2. Navigate to the directory by running the command `cd mycontainer`.
3. Create a new file named `Dockerfile` using your preferred text editor.
4. Copy and paste the following code into the Dockerfile:

```
FROM centos:latest
RUN yum -y update && \
    yum -y install httpd && \
    yum clean all
COPY index.html /var/www/html/
EXPOSE 80
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
```

5. Save and close the file.
6. Create a new file named `index.html` within the `mycontainer` directory.
7. Add some HTML content into the `index.html` file, such as `<h1>Hello World</h1>`.
8. Save and close the file.

The above Dockerfile will create a container based on the latest version of CentOS, update the system, install Apache HTTP server, copy the `index.html` file into the container, expose port 80, and start the HTTP server.

## Step 3: Build the Container Image
Now that we have created our Dockerfile and `index.html` file, we can build our container image. Follow these steps to build the image:

1. In the `mycontainer` directory, run the command `docker build -t mycontainer-image .`. This command will build an image with the name `mycontainer-image` based on the Dockerfile in the current directory.
2. Once the build process is complete, you can verify the image by running the command `docker images`. You should see your newly created image in the list.

## Step 4: Create a Systemd Service Unit File
To configure our container to start automatically as a systemd service, we need to create a systemd unit file. This file will define the service and its properties, such as the container image to use and any specific configurations. Follow these steps to create the unit file:

1. Create a new file named `mycontainer.service` in the `/etc/systemd/system/` directory using your preferred text editor.
2. Copy and paste the following code into the file:

```
[Unit]
Description=My Container Service
Requires=docker.service
After=docker.service

[Service]
Restart=always
RestartSec=900

ExecStartPre=-/usr/bin/docker kill mycontainer
ExecStartPre=-/usr/bin/docker rm mycontainer

ExecStart=/usr/bin/docker run --rm --name=mycontainer -p 80:80 mycontainer-image

ExecStop=/usr/bin/docker stop mycontainer

[Install]
WantedBy=multi-user.target
```

3. Save and close the file.

The above unit file will create a service named `mycontainer`, define its dependencies and restart policies, and specify the docker run command to start and stop the container.

## Step 5: Enable and Start the Service
Now that we have created our systemd unit file, we can enable and start the service. Follow these steps to enable and start the service:

1. Reload systemd to ensure it picks up the changes made to unit files by running the command `systemctl daemon-reload`.
2. Enable the `mycontainer` service by running the command `systemctl enable mycontainer`.
3. Start the service by running the command `systemctl start mycontainer`.
4. Check the status of the service by running the command `systemctl status mycontainer`. You should see the service is active (running) and its process ID (PID).

## Step 6: Test the Service
To ensure that our container is starting correctly and serving our HTML content, we can test the service. Follow these steps to test the service:

1. In your browser, navigate to `http://(server IP address)` where the server IP address is the IP address of your RHEL system.
2. If everything is configured correctly, you should see the HTML content we added to the `index.html` file within the container. 
3. To stop the service, run the command `systemctl stop mycontainer` and ensure the webpage is no longer accessible. 

Congratulations, you have successfully configured a container to start automatically as a systemd service on your Red Hat Certified Systems Administrator Exam.

## Additional Notes
- You can customize the Dockerfile and systemd unit file to suit your specific needs and configurations.
- You can also use other containerization platforms, such as Podman, to build and run containers on Red Hat systems.
- Remember to regularly update and maintain your container images and services for security and performance purposes.
- It is recommended to practice this process multiple times before taking the exam to familiarize yourself with each step and troubleshoot any potential issues that may arise.