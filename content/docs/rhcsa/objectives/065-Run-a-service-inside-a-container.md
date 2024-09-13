# Tech Tutorial: Manage Containers on RHEL

## Introduction

In this tutorial, we'll cover how to manage and run services inside containers specifically using tools and commands applicable in Red Hat Enterprise Linux (RHEL). This knowledge is particularly relevant for those preparing for the Red Hat Certified System Administrator (RHCSA) exam, which includes an objective on running services within containers.

Containers are lightweight, provide a consistent environment for applications, and are isolated from the host system. They make it easier to manage dependencies, ensure consistency across multiple development and production environments, and scale applications efficiently.

We will use Podman, a daemonless container engine for developing, managing, and running OCI Containers on your Linux System. Podman is included in the default RHEL 8 and RHEL 9 repositories and is a core part of the RHCSA exam objectives related to containers.

## Prerequisites

- A running instance of RHEL 8 or RHEL 9.
- Root or sudo privileges.
- Basic familiarity with command-line interface and Linux environment.

## Step-by-Step Guide

### Step 1: Install Podman

First, ensure that your system is updated and then install Podman.

```bash
sudo dnf update -y
sudo dnf install -y podman
```

### Step 2: Search for Container Images

Before you can run a service inside a container, you need an appropriate image. Let's say we want to run an Nginx server. First, search for Nginx images:

```bash
podman search nginx
```

### Step 3: Pull the Container Image

Pull the official Nginx image from the registry:

```bash
podman pull nginx
```

### Step 4: Run the Nginx Service in a Container

Now, run the Nginx service inside a container:

```bash
podman run --name mynginx -d -p 8080:80 nginx
```

This command does the following:
- `--name mynginx`: Names the container 'mynginx'.
- `-d`: Runs the container in detached mode.
- `-p 8080:80`: Maps port 80 of the container to port 8080 on the host.

### Step 5: Verify the Container is Running

Check that the container is running and the Nginx service is accessible:

```bash
podman ps
```

You should see your Nginx container running. You can also access it through the browser or using curl:

```bash
curl http://localhost:8080
```

### Step 6: Managing the Container

To stop the container, use:

```bash
podman stop mynginx
```

To start the container again, use:

```bash
podman start mynginx
```

To remove the container when you are done, use:

```bash
podman rm mynginx
```

## Detailed Code Examples

Let's go a bit further and see how to use a custom Nginx configuration within our container. For this, we need a custom configuration file on the host.

1. Create a directory for custom configurations:

```bash
mkdir -p ~/custom-nginx
cd ~/custom-nginx
```

2. Create a new `nginx.conf` file and modify as needed.

3. Run the container using the custom configuration:

```bash
podman run --name custom-nginx -v ~/custom-nginx/nginx.conf:/etc/nginx/nginx.conf:Z -d -p 8080:80 nginx
```

The `-v` option mounts the custom configuration file inside the container.

## Conclusion

In this tutorial, you've learned how to install Podman, search for, pull, and run a Docker image as a container service in RHEL. We also covered how to manage the lifecycle of containers and how to use custom configurations. This knowledge will be beneficial not only for the RHCSA exam but also for real-world applications where containerization is increasingly becoming a standard practice.