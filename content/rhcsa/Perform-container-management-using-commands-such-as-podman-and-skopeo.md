+++
title = "Perform container management using commands such as podman and skopeo"
date = "2024-02-16T11:54:26-05:00"
author = "root"
cover = ""
tags = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
keywords = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# How to Perform Container Management using Podman and Skopeo

In this tutorial, we will guide you through the process of performing container management using commands such as podman and skopeo. This is a required skill for the Red Hat Certified Systems Administrator Exam (EX200), Objective 200.

## Introduction to Podman and Skopeo

Podman and Skopeo are two important tools used in Linux systems for container management. Podman is a daemonless container engine that is used to manage containers, pods, and images. Skopeo, on the other hand, is a command-line utility used for working with remote container registries.

## Requirements

Before we dive into the tutorial, make sure you have the following requirements:

- A Linux system with Podman and Skopeo installed
- Basic knowledge of the Linux command line

## Step 1: Starting the Podman Service

The first step in managing containers using Podman is to start the Podman service. This can be done by running the following command in the terminal:

`sudo systemctl start podman`

This will start the Podman service and allow you to manage containers on your system.

## Step 2: Pulling an Image using Skopeo

Before we can create containers, we need to pull an image from a container registry. Skopeo allows us to do this easily by providing the following command:

`skopeo copy <source> <destination>`

Where `<source>` is the location of the image in the registry and `<destination>` is the location where the image will be stored on your system. For example, to pull the latest CentOS image from Docker Hub, we can use the following command:

`skopeo copy docker://docker.io/centos:latest dir:///home/images`

This will pull the image from Docker Hub and save it in the specified directory.

## Step 3: Creating a Container with Podman

Now that we have an image, we can use Podman to create a container from it. The basic syntax for creating a container is as follows:

`podman run <options> <image> <command>`

Where `<options>` are the various configurations for the container, `<image>` is the image used to create the container, and `<command>` is the command that the container will run. For example, to create a CentOS container and run a bash shell inside it, we can use the following command:

`podman run -it centos bash`

This will create a container named "centos" and open a bash shell inside it, allowing us to interact with the container.

## Step 4: Managing Containers with Podman

Once a container is created, it can be managed using various Podman commands. Some of the useful commands are:

- `podman ps`: lists all running containers
- `podman start <container>`: starts a stopped container
- `podman stop <container>`: stops a running container
- `podman rename <oldname> <newname>`: renames a container
- `podman rm <container>`: removes a container

For a full list of Podman commands, you can refer to the official documentation.

## Step 5: Managing Images with Skopeo

Similarly, we can also use Skopeo to manage images on our system. Some useful commands for managing images are:

- `skopeo inspect <image>`: shows details about the image
- `skopeo delete <image>`: deletes the image from your system

Again, for a full list of Skopeo commands, refer to the official documentation.

## Conclusion

In this tutorial, we have covered the basics of container management using Podman and Skopeo. By following these steps, you should now be able to start, stop, and manage containers on your Linux system using these tools. For more in-depth knowledge, we recommend further reading from the official documentation and practicing on your own system.

We hope this tutorial has been helpful in preparing you for the Red Hat Certified Systems Administrator Exam, Objective 200. Good luck on your certification journey!