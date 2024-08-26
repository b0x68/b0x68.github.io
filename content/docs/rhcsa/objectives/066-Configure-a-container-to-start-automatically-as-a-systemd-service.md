# Tech Tutorial: Manage Containers

## Introduction

In the world of software development, containers have become an essential tool for ensuring consistency across different environments. One popular container platform is Docker, which simplifies the deployment of applications inside software containers. However, managing the lifecycle of containers in a production environment typically requires integration with the host system's service management. On Linux systems, `systemd` is the de facto system and service manager. It provides robust tools for managing services that start at boot time, including Docker containers.

In this tutorial, we will cover how to configure a Docker container to start automatically using `systemd`. This setup ensures that your containerized applications are treated as first-class citizens on your server, starting and stopping along with the system, just like other services.

## Prerequisites

- A Linux system with `systemd` installed (Most modern Linux distributions like CentOS, Ubuntu, and Fedora come with `systemd`).
- Docker installed on your system. You can install Docker by following the instructions on the [official Docker website](https://docs.docker.com/engine/install/).

## Step-by-Step Guide

### Step 1: Create a Docker Container

First, we need a Docker container that we want to manage via `systemd`. For this example, let's use a simple NGINX container. We will pull the NGINX image from Docker Hub and run it:

```bash
docker pull nginx
docker run --name my-nginx -d -p 8080:80 nginx
```

This command starts an NGINX container named `my-nginx` which listens on port 8080.

### Step 2: Create a Systemd Service File

To manage this container with `systemd`, we need to create a service file in `/etc/systemd/system`. For instance, let's name it `nginx-container.service`:

```bash
sudo nano /etc/systemd/system/nginx-container.service
```

Add the following content to this file:

```ini
[Unit]
Description=NGINX Docker Container
After=docker.service
Requires=docker.service

[Service]
Restart=always
ExecStart=/usr/bin/docker start -a my-nginx
ExecStop=/usr/bin/docker stop my-nginx

[Install]
WantedBy=multi-user.target
```

Here’s what each part does:
- **[Unit]**: Metadata and dependencies of the service. This service requires `docker.service` to function properly.
- **[Service]**: Commands to execute when starting or stopping the service. It uses Docker commands to start and stop the NGINX container.
- **[Install]**: Specifies when the service should be automatically started. `multi-user.target` is a standard target for creating multi-user environments.

### Step 3: Enable and Start the Service

Now that our `systemd` service is defined, enable it to start at boot time:

```bash
sudo systemctl enable nginx-container.service
```

Start the service manually for now:

```bash
sudo systemctl start nginx-container.service
```

Check the status of the service:

```bash
sudo systemctl status nginx-container.service
```

If everything is configured correctly, your NGINX container should be running, and the service should show as active.

## Conclusion

By integrating Docker with `systemd`, you can automatically manage your containers as part of the system services. This setup is particularly useful in production environments where containers need to start in a specific order or require robust logging and monitoring. `systemd` provides a comprehensive and flexible way to manage container lifecycles, ensuring your applications are always running as expected.

This tutorial should serve as a stepping stone into deeper integrations of container technology with native system services, paving the way for more resilient and manageable deployments.