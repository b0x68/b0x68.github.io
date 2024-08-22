# Tech Tutorial: Manage Containers

## Introduction

In this tutorial, we will delve into the basics of managing containers using two powerful tools: `podman` and `skopeo`. Containers have become a key part of software development and deployment strategies, offering a lightweight, portable, and consistent environment for applications. `podman` provides a daemonless container engine for developing, managing, and running OCI Containers on your Linux system. `skopeo` is a command line utility that performs various operations on container images and image repositories.

Understanding how to effectively use these tools can help you streamline your development and deployment workflows. By the end of this tutorial, you should be able to manage container images and containers proficiently using `podman` and `skopeo`.

## Prerequisites

Before you start, ensure you have the following installed on your Linux machine:
- Podman (Version 2.0 or later recommended)
- Skopeo

You can install these tools using your distribution's package manager. For example, on Fedora:
```bash
sudo dnf install -y podman skopeo
```

## Step-by-Step Guide

### 1. Managing Containers with Podman

#### Starting, Stopping, and Managing Container Lifecycle

**Start a Container:**
```bash
# Start a container from the Fedora image and run bash
podman run -it fedora /bin/bash
```

**List Containers:**
```bash
# List all running containers
podman ps

# List all containers, including stopped ones
podman ps -a
```

**Stopping a Container:**
```bash
# Stop a container by name or ID
podman stop [container_name_or_id]
```

**Removing a Container:**
```bash
# Remove a container by name or ID
podman rm [container_name_or_id]
```

### 2. Managing Images with Podman

**Pulling an Image:**
```bash
# Pull the latest Ubuntu image
podman pull ubuntu
```

**Listing Images:**
```bash
# List all images
podman images
```

**Removing an Image:**
```bash
# Remove an image by name or ID
podman rmi ubuntu
```

### 3. Advanced Podman Operations

**Inspecting Containers and Images:**
```bash
# Inspect a container
podman inspect [container_name_or_id]

# Inspect an image
podman inspect --type image [image_name_or_id]
```

**Running Containers in Detached Mode:**
```bash
# Run a container in detached mode
podman run -d --name mynginx nginx
```

### 4. Using Skopeo to Work with Image Registries

**Copying an Image from Docker Hub to Another Registry:**
```bash
# Copy an image from Docker Hub to a private registry
skopeo copy docker://docker.io/library/busybox:latest docker://myregistry.local/busybox:latest
```

**Inspecting a Remote Image:**
```bash
# Inspect an image on Docker Hub without pulling it
skopeo inspect docker://docker.io/library/ubuntu:latest
```

**Deleting an Image from a Registry:**
```bash
# Delete an image from a registry (if the registry supports the deletion API)
skopeo delete docker://myregistry.local/busybox:latest
```

## Conclusion

In this tutorial, we covered the basic and some advanced operations you can perform with `podman` and `skopeo` to manage containers and container images. These tools provide powerful, flexible, and scriptable ways to handle containerized applications without the overhead of a daemon, offering a robust solution for container management in various environments.

With the knowledge acquired, you should now be able to integrate these tools into your CI/CD pipelines, enhance your development workflows, or even manage containers in production environments more effectively.