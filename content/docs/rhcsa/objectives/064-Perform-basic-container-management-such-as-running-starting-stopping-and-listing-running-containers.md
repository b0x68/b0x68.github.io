# Tech Tutorial: Manage Containers

## Introduction

In the world of software development, containerization has become a pivotal strategy for deploying applications in various environments consistently. Containers encapsulate an application's code along with its dependencies, making the application run the same regardless of the underlying infrastructure. Docker, one of the most popular containerization platforms, helps developers and system administrators manage these containers efficiently.

This tutorial focuses on performing basic container management tasks such as running, starting, stopping, and listing running containers using Docker. These foundational skills are essential for anyone looking to manage containers effectively in any development, staging, or production environments.

## Prerequisites

Before you begin, ensure you have the following:
- Docker installed on your machine. Installation guides for Docker can be found on the [Official Docker website](https://docs.docker.com/get-docker/).
- Basic familiarity with command-line interfaces (CLI).

## Step-by-Step Guide

### 1. Running a New Container

To run a new container, you generally use the `docker run` command followed by the name of the image you want to use. Docker images are templates used to create containers; they provide the necessary executable and libraries.

**Example: Run an Ubuntu Container**

```bash
docker run -it ubuntu /bin/bash
```

- `docker run`: Command to create and start a container.
- `-it`: Option to run the container in interactive mode with a tty terminal.
- `ubuntu`: Name of the Docker image.
- `/bin/bash`: Command to be executed inside the new container.

This command will download the Ubuntu image if it's not already present on your machine, create a new container, and log you into the bash shell of the container.

### 2. Listing Running Containers

To see a list of all running containers, you can use the `docker ps` command.

**Example: List Containers**

```bash
docker ps
```

For more detailed information, you can add the `-a` option to see all containers (not just the running ones):

```bash
docker ps -a
```

### 3. Stopping a Container

When you need to stop a running container, you can use the `docker stop` command followed by the container ID or name.

**Example: Stop a Container**

First, find the container ID by listing the running containers:

```bash
docker ps
```

Then stop the container using:

```bash
docker stop [CONTAINER_ID]
```

Replace `[CONTAINER_ID]` with the actual ID of the container.

### 4. Starting a Stopped Container

To start a previously stopped container, use the `docker start` command.

**Example: Start a Container**

```bash
docker start [CONTAINER_ID]
```

Replace `[CONTAINER_ID]` with the ID of the container you want to start.

## Detailed Code Examples

Let’s run a more practical example: deploying a simple web server.

**Run a Simple Nginx Web Server**

1. **Run the Container**

   ```bash
   docker run --name my-nginx -p 8080:80 -d nginx
   ```

   - `--name my-nginx`: Assigns a name to the container.
   - `-p 8080:80`: Maps port 80 of the container to port 8080 on the host.
   - `-d`: Runs the container in detached mode.
   - `nginx`: The image used to create the container.

2. **Verify the Container is Running**

   ```bash
   docker ps
   ```

3. **Access the Web Server**

   Open a web browser and navigate to `http://localhost:8080`. You should see the Nginx welcome page.

4. **Stop the Container**

   ```bash
   docker stop my-nginx
   ```

5. **Restart the Container**

   ```bash
   docker start my-nginx
   ```

## Conclusion

Managing containers is a fundamental skill for developers and system administrators working in modern IT environments. This tutorial covered the basics of running, listing, stopping, and starting containers using Docker. Mastery of these commands provides a foundation for more advanced Docker usage, including container orchestration, networking, and security management. Practice these commands to become proficient in container management and take full advantage of the benefits that Docker offers.