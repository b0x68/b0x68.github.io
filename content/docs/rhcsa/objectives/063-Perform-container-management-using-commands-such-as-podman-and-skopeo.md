# Tech Tutorial: Manage Containers with Podman and Skopeo

## Introduction

In the world of Red Hat Enterprise Linux (RHEL), container management is an essential skill for system administrators. This tutorial will cover how to manage containers using `podman` and `skopeo`, two powerful tools in the Red Hat ecosystem. By the end of this guide, you will understand how to effectively use these tools to handle container images and containers.

`Podman` is a daemonless container engine for developing, managing, and running OCI Containers on your Linux System. Containers can either be run as root or in rootless mode. Unlike Docker, it does not require a running daemon. This can be advantageous for system administrators seeking to manage containers without the overhead or security implications of a daemon.

`Skopeo` is a command-line utility that performs various operations on container images and image repositories. Skopeo can inspect a repository on a container registry without pulling the image. It allows you to copy container images between various repositories, convert between image formats, and more, all without needing an elevated permissions, daemon, or even Docker.

## Step-by-Step Guide

### 1. Installing Podman and Skopeo

First, ensure that you are running RHEL 8 or newer, as `podman` and `skopeo` are included in these versions by default.

To install Podman and Skopeo, you can run the following commands:

```bash
sudo dnf install -y podman skopeo
```

### 2. Managing Containers with Podman

#### Pulling a container image

To download a container image from a registry, use the following command:

```bash
podman pull docker.io/library/ubuntu:latest
```

This command pulls the latest Ubuntu image from the Docker official registry.

#### Listing images

To list all downloaded images:

```bash
podman images
```

#### Running a container

To run a container interactively:

```bash
podman run -it --name myubuntu ubuntu /bin/bash
```

This command starts an interactive Bash shell inside the Ubuntu container.

#### Viewing running containers

To see all running containers:

```bash
podman ps
```

To view all containers, including stopped ones:

```bash
podman ps -a
```

#### Stopping a container

To stop a running container:

```bash
podman stop myubuntu
```

#### Removing a container

To remove a stopped container:

```bash
podman rm myubuntu
```

### 3. Managing Container Images with Skopeo

#### Inspecting an image

To inspect an image on Docker Hub without pulling it:

```bash
skopeo inspect docker://docker.io/library/ubuntu:latest
```

This command gives you the JSON output with all the configuration details of the Ubuntu image.

#### Copying an image

To copy an image from Docker Hub to another registry:

```bash
skopeo copy docker://docker.io/library/ubuntu:latest docker://myregistry.local/ubuntu:latest
```

Make sure to replace `myregistry.local` with your actual registry URL.

#### Deleting an image

To delete an image from a local registry:

```bash
skopeo delete --creds username:password docker://myregistry.local/ubuntu:latest
```

### 4. Advanced Podman Usage

#### Creating and managing pods

Podman allows you to create your own pods, which are groups of one or more containers that share the same network namespace, among other resources.

```bash
podman pod create --name mypod
```

Adding a container to the pod:

```bash
podman run -d --pod mypod nginx
```

Listing pods:

```bash
podman pod list
```

## Conclusion

`Podman` and `Skopeo` offer robust, flexible tools for container management without the overhead of a daemon, suitable for both development and production environments in RHEL. By mastering these tools, you can significantly enhance your capabilities in managing containers and container images efficiently. Whether you are preparing for the RHCSA exam or looking to improve your container management skills, understanding and utilizing `podman` and `skopeo` are essential for any Red Hat system administrator.