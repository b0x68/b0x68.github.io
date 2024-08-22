# Tech Tutorial: Manage Containers by Configuring Them to Start Automatically as a systemd Service

In this tutorial, we will delve into the process of managing containers by configuring them to start automatically on your Linux system using systemd. This approach is crucial for ensuring that your containerized applications run as expected after a reboot or system start, enhancing reliability in production environments.

## Introduction

Systemd is a system and service manager for Linux operating systems, which creates a unified framework for service management and makes it easier to manage and understand. Docker, a popular containerization platform, allows you to package applications into containers—standardized executable components combining application source code with the operating system (OS) libraries and dependencies required to run that code in any environment.

While Docker provides its own commands to manage the lifecycle of containers, integrating Docker with systemd allows for more robust management, like automatically starting containers at boot time and restarting them if they fail.

## Prerequisites

To follow this tutorial, you'll need:
- A Linux system with systemd installed (most modern Linux distributions like CentOS, Debian, and Ubuntu come with systemd).
- Docker installed on your system. You can install Docker by following the official documentation: [Install Docker](https://docs.docker.com/engine/install/).

## Step-by-Step Guide

### Step 1: Create a Docker Container

First, let's pull a Docker image and run it to create a container. We'll use the official nginx image for this example.

```bash
docker pull nginx
docker run --name my-nginx -d nginx
```

This command pulls the latest nginx image from Docker Hub and runs it in detached mode with the name `my-nginx`.

### Step 2: Create a systemd Service File

Next, we need to create a systemd service file that will manage our Docker container. Systemd service files are typically stored in `/etc/systemd/system`. Here's how to create a service file for our nginx container:

1. Open a new file in the `/etc/systemd/system` directory. We'll name it `nginx-container.service`.

   ```bash
   sudo nano /etc/systemd/system/nginx-container.service
   ```

2. Add the following content to the file:

   ```ini
   [Unit]
   Description=Nginx Container
   Requires=docker.service
   After=docker.service

   [Service]
   Restart=always
   ExecStart=/usr/bin/docker start -a my-nginx
   ExecStop=/usr/bin/docker stop -t 2 my-nginx

   [Install]
   WantedBy=multi-user.target
   ```

   Explanation:
   - `[Unit]` section defines dependencies and a description.
   - `[Service]` section tells systemd how to start and stop the service (container). `Restart=always` instructs systemd to restart the service on failure.
   - `[Install]` section defines when the service should be automatically started. `multi-user.target` is a standard target for services on a multi-user system.

### Step 3: Enable and Start the Service

Now that we have our service file created, we need to reload the systemd manager configuration, enable our service to start on boot, and then start the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable nginx-container.service
sudo systemctl start nginx-container.service
```

### Step 4: Verify the Service

Check the status of the service to ensure it's running properly:

```bash
sudo systemctl status nginx-container.service
```

## Conclusion

In this tutorial, you learned how to configure a Docker container to start automatically as a systemd service. This setup not only ensures that your container starts automatically after a reboot but also provides robust management capabilities through systemd, such as automatic restarts on failure.

Using systemd to manage container lifecycle adds a layer of reliability and integration into the system's standard service management framework, making it an essential skill for system administrators and DevOps professionals working with Linux and containerized applications.

This approach can be adapted for any container by modifying the Docker commands in the service file according to the container's requirements. As you continue to work with Docker and systemd, you'll find this integration invaluable for maintaining consistent, reliable service availability.