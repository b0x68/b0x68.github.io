# Tech Tutorial: Manage Containers - Inspecting Container Images

## Introduction

Containers have become a fundamental part in deploying applications in various environments. Docker, one of the most popular containerization platforms, allows developers to package applications into containers—standardized executable components combining application source code with the operating system (OS) libraries and dependencies required to run that code in any environment.

While working with containers, it is crucial to understand the details of the container images. Inspecting container images allows developers to fetch detailed information about the image such as its size, layers, creation time, and metadata like the environment variables, default command and entry points, and labels. This tutorial will guide you through the process of inspecting container images using Docker, providing you with robust examples and detailed explanations.

## Step-by-Step Guide

### Prerequisites

- Docker installed on your machine. You can download and install Docker from [Docker's official website](https://www.docker.com/get-started).
- Basic understanding of Docker and container terminologies.

### Step 1: Pulling a Docker Image

Before inspecting a container image, you need to have a Docker image on your local machine. Let's pull a basic image, such as the official Ubuntu image.

```bash
docker pull ubuntu:latest
```

This command downloads the latest Ubuntu image from Docker Hub.

### Step 2: Inspecting a Docker Image

To inspect an image, use the `docker inspect` command followed by the image name or ID. This command returns a JSON array with a lot of detailed information about the image.

```bash
docker inspect ubuntu:latest
```

### Detailed Code Examples

Let's break down the information you can obtain from the `docker inspect` command, using the Ubuntu image as an example.

#### Example 1: Basic Inspection

Running the basic inspect command:

```bash
docker inspect ubuntu:latest
```

This outputs a JSON array with comprehensive details about the image. Here’s a brief look at some key pieces of information you might find:

- **Id**: The image ID.
- **RepoTags**: List of tags associated with the image.
- **Created**: Timestamp when the image was created.
- **Architecture**: Processor architecture that the image is compatible with.
- **Os**: Operating system of the image.
- **Size**: The total size of the image.
- **Layers**: Detailed information about the layers that make up the image.

#### Example 2: Filtering the Output

Often, you only need specific information, such as the size of the image. You can filter the output using the `--format` option. For instance, to get the size of the image:

```bash
docker inspect --format='{{.Size}}' ubuntu:latest
```

This command will return the size of the Ubuntu image in bytes.

#### Example 3: Checking Environment Variables

To inspect environment variables set within the image:

```bash
docker inspect --format='{{range .Config.Env}}{{println .}}{{end}}' ubuntu:latest
```

This will list all environment variables set in the Ubuntu image.

## Conclusion

Inspecting Docker images is crucial for understanding the contents and properties of your containers. This can help in debugging issues, optimizing your Docker images, and ensuring security compliance. The `docker inspect` command is a powerful tool in your Docker arsenal, providing a wealth of information that can be filtered and tailored to your specific needs.

By mastering image inspection, you're better equipped to manage your Docker containers effectively, leading to more stable and efficient deployments. Remember, the key to effective container management is understanding the details, and Docker provides all the tools necessary to gain this insight.