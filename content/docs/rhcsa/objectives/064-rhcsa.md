# Tech Tutorial: Manage Containers

## Introduction

Containers are a powerful way to deploy, manage, and scale applications. By encapsulating the environment needed to run an application, containers ensure that the software behaves the same way regardless of where it’s deployed. This tutorial focuses on basic container management tasks such as running, starting, stopping, and listing containers using Docker, one of the most popular containerization platforms.

## Prerequisites

Before we proceed, ensure you have the following installed:
- **Docker**: You can download and install Docker from [Docker’s official website](https://www.docker.com/products/docker-desktop). This tutorial assumes you are using Docker on Linux, macOS, or Windows with WSL2.

## Step-by-Step Guide

### 1. Running Containers

To run a container, you use the `docker run` command. This command creates a new container from a specified image and starts it.

#### Example: Running an Nginx Container

```bash
docker run --name my-nginx -p 8080:80 -d nginx
```

**Explanation:**
- `--name my-nginx`: Assigns a name to the container.
- `-p 8080:80`: Maps port 80 on the container to port 8080 on the host.
- `-d`: Runs the container in detached mode (in the background).
- `nginx`: The name of the image to use (pulled from Docker Hub if not locally available).

You can visit `http://localhost:8080` in your web browser to see the default Nginx landing page.

### 2. Listing Running Containers

To list all currently running containers, use the `docker ps` command.

#### Example: Listing Containers

```bash
docker ps
```

**Output:**

You'll see an output similar to the following:

```
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
c3f279d17e0a   nginx     "/docker-entrypoint.…"   5 minutes ago    Up 5 minutes    0.0.0.0:8080->80/tcp   my-nginx
```

### 3. Stopping Containers

To stop a running container, use the `docker stop` command followed by the container name or ID.

#### Example: Stopping the Nginx Container

```bash
docker stop my-nginx
```

### 4. Starting Containers

To start a stopped container, use the `docker start` command followed by the container name or ID.

#### Example: Starting the Nginx Container

```bash
docker start my-nginx
```

### 5. Listing All Containers

To see all containers, including those that are stopped, use the `docker ps -a` command.

#### Example: Listing All Containers

```bash
docker ps -a
```

**Output:**

You'll see an output which includes both running and stopped containers.

## Conclusion

In this tutorial, we covered the basic commands needed to manage containers using Docker: running, starting, stopping, and listing containers. These fundamental skills are essential for anyone managing applications in a Docker environment. Remember, the key to effective container management is understanding how these containers interact with both the host system and each other, and mastering these commands is the first step in achieving that understanding.