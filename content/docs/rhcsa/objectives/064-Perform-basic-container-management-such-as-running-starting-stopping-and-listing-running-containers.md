# Tech Tutorial: Manage Containers

## Introduction
In the realm of Red Hat Certified System Administrator (RHCSA) exam preparation, understanding how to manage containers is essential. Containers allow you to package and run applications and their environments as a single, consistent unit which can be shared across multiple environments. Red Hat Enterprise Linux (RHEL) provides robust support for container management through tools like Podman and Skopeo. This tutorial will focus on Podman, a daemonless container engine, to perform basic container management tasks such as running, starting, stopping, and listing running containers.

## Step-by-Step Guide

### Prerequisites
Before diving into the commands, ensure that your RHEL system has the `podman` package installed. You can install it using the following command:
```bash
sudo yum install -y podman
```

### Running Containers
To run a container, you use the `podman run` command. This command pulls the image from a container registry, creates a container from it, and then runs the container.

**Example: Running an Nginx Container**
```bash
sudo podman run --name mynginx -d -p 8080:80 nginx
```
This command does the following:
- `--name mynginx`: Assigns the name `mynginx` to the new container.
- `-d`: Runs the container in detached mode (in the background).
- `-p 8080:80`: Maps port 80 in the container to port 8080 on the host.
- `nginx`: The image to use. If it's not available locally, Podman pulls it from the default Docker registry.

### Listing Running Containers
To see a list of all running containers, use:
```bash
sudo podman ps
```
For more detailed information, you can add the `-a` switch to see all containers, even those that are stopped.

**Example:**
```bash
sudo podman ps -a
```

### Stopping Containers
To stop a running container, use the `podman stop` command followed by the container ID or name.

**Example: Stopping the Nginx Container**
```bash
sudo podman stop mynginx
```

### Starting Containers
If your container is stopped and you wish to start it again, use the `podman start` command.

**Example: Starting the Nginx Container**
```bash
sudo podman start mynginx
```

### Removing Containers
To remove a stopped container, use the `podman rm` command.

**Example: Removing the Nginx Container**
```bash
sudo podman rm mynginx
```

## Detailed Code Examples

**Running a temporary interactive container:**
```bash
sudo podman run -it --rm ubuntu bash
```
This command opens an interactive shell (`bash`) inside the latest Ubuntu container. The `--rm` flag tells Podman to automatically remove the container once it exits, which is useful for temporary or test containers.

**Exporting container logs:**
```bash
sudo podman logs mynginx > nginx_logs.txt
```
This command redirects logs from the `mynginx` container into a text file called `nginx_logs.txt`, which can be useful for debugging or auditing.

## Conclusion
This tutorial covered the basics of managing containers on a RHEL system, focusing on the Podman tool. By mastering these commands, you'll be able to effectively manage the lifecycle of containers on your system, a crucial skill for any systems administrator preparing for the RHCSA exam. Remember, practice is key, so experiment with these commands to build your confidence and proficiency.