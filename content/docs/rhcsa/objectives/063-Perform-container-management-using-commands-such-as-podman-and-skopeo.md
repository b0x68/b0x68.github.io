# Tech Tutorial: Manage Containers with Podman and Skopeo

## Introduction

In the world of containerization, Docker has been a popular choice for many years. However, alternative tools like Podman and Skopeo have gained traction, especially in environments that prioritize security and simplicity. This tutorial will guide you through container management using Podman and Skopeo, focusing on practical, real-world usage and commands.

### What is Podman?

Podman (Pod Manager) is a daemonless container engine for developing, managing, and running OCI Containers on your Linux System. Containers can be run as root or in rootless mode. Unlike Docker, Podman doesn’t require a running daemon to work, which enhances security and reduces the attack surface.

### What is Skopeo?

Skopeo is a command-line utility that performs various operations on container images and image repositories. Skopeo can handle operations that relate directly to image repositories, not containers themselves, like moving an image from one repository to another without requiring privilege.

## Prerequisites

- A Linux environment (Fedora, CentOS, Ubuntu, etc.)
- Installation of Podman
- Installation of Skopeo

You can install Podman and Skopeo on Fedora like this:

```bash
sudo dnf install -y podman skopeo
```

On Ubuntu:

```bash
sudo apt update
sudo apt install -y podman skopeo
```

## Step-by-Step Guide

### 1. Managing Containers with Podman

#### Run a Container

To start a container using Podman, use the following command:

```bash
podman run -d --name mynginx nginx
```

This command downloads the `nginx` image from the Docker Hub, if it's not available locally, and runs it in detached mode.

#### List Running Containers

To see a list of running containers:

```bash
podman ps
```

#### Executing Commands in a Running Container

To execute commands inside a container:

```bash
podman exec -it mynginx /bin/bash
```

#### Stopping a Container

To stop a running container:

```bash
podman stop mynginx
```

#### Removing a Container

To remove a stopped container:

```bash
podman rm mynginx
```

### 2. Managing Images with Skopeo

#### Copying Images

To copy an image from Docker Hub to another registry:

```bash
skopeo copy docker://docker.io/library/nginx:latest docker://myregistry.local/nginx:latest
```

#### Inspecting Images

To get detailed information about an image, without pulling it:

```bash
skopeo inspect docker://docker.io/library/nginx:latest
```

#### Deleting Images

To delete an image from a registry:

```bash
skopeo delete --creds=username:password docker://myregistry.local/nginx:latest
```

### 3. Advanced Usage

#### Podman with Systemd

You can integrate Podman containers with systemd to manage the lifecycle of your containers. Here is an example of a systemd unit file for a Podman container:

```ini
[Unit]
Description=My Nginx Podman Container
After=network.target

[Service]
Restart=always
ExecStart=/usr/bin/podman start -a mynginx
ExecStop=/usr/bin/podman stop -t 10 mynginx

[Install]
WantedBy=multi-user.target
```

Save this as `nginx-container.service` and use `systemctl` to manage the container lifecycle.

## Conclusion

Podman and Skopeo offer powerful, flexible alternatives to Docker for container management. Podman operates without a daemon, enhancing security and ease of use in many scenarios, while Skopeo provides handy tools for working with image repositories. By mastering these tools, you can efficiently manage containers and images, fitting into CI/CD pipelines, development environments, and production setups.

Now that you have a fundamental grasp of managing containers and images with Podman and Skopeo, you can explore more complex scenarios and integrate these tools into your infrastructure. Happy containerizing!