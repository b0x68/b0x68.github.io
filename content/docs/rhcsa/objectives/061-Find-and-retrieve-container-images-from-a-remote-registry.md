# Tech Tutorial: Manage Containers

## Introduction

In the realm of Red Hat Certified System Administrator (RHCSA) exam preparation, understanding how to manage containers is crucial. Containers are a foundational technology in modern infrastructure, enabling lightweight, portable, and consistent software deployments. This tutorial focuses on a specific aspect of container management: finding and retrieving container images from a remote registry.

For Red Hat systems, particularly those using Red Hat Enterprise Linux (RHEL), managing containers typically involves working with `podman`, a tool designed to find, run, and build application containers. `podman` is a daemonless container engine that works seamlessly with Open Container Initiative (OCI) images and containers.

This tutorial will guide you through the processes of finding and pulling container images from a remote registry using the `podman` command, which is essential for deploying applications in containers on RHEL systems.

## Step-by-Step Guide

### Step 1: Installing Podman

Before you can pull container images, you must ensure that `podman` is installed on your system. On RHEL, `podman` can be installed using the following `yum` command:

```bash
sudo yum install -y podman
```

### Step 2: Searching for Container Images

To find container images, you use the `podman search` command. This command queries a container registry for images that match the search term you provide. By default, `podman` searches on Docker Hub. However, you can specify other registries.

For example, to search for the official Redis image on Docker Hub, you would use:

```bash
podman search redis
```

This command will return a list of all images whose descriptions match the term "redis". To narrow down the search, you can specify more specific terms or use the `--filter` option to filter results based on specific criteria like stars, is-official, etc.

### Step 3: Pulling a Container Image

Once you have identified the container image you want to use, you can pull it to your local system using the `podman pull` command. For instance, to pull the latest official Redis image from Docker Hub, you would run:

```bash
podman pull redis
```

If you need a specific version of Redis, you can specify the tag associated with that version:

```bash
podman pull redis:6.0
```

### Step 4: Verifying the Image Pull

After pulling the image, you can verify that it is now stored on your local machine by listing all the container images:

```bash
podman images
```

This command will show you a list of all images available locally, including the ones you just pulled.

## Detailed Code Examples

Let's consider a real-world scenario where you need to deploy a WordPress site using container images for both WordPress and MySQL. You'll need to pull these images from Docker Hub using `podman`.

1. **Search for WordPress and MySQL Images:**

   ```bash
   podman search wordpress
   podman search mysql
   ```

2. **Pull the Desired Images:**

   ```bash
   podman pull wordpress:latest
   podman pull mysql:5.7
   ```

3. **Check the Images:**

   ```bash
   podman images
   ```

4. **Run the Containers:**

   Here, you might want to run the MySQL container first and then the WordPress container linked to the MySQL container. This step is beyond the scope of this tutorial but is a common next step in deploying applications using containers.

## Conclusion

This tutorial covered the essential skills needed to manage containers on a RHEL system, focusing on finding and retrieving container images from a remote registry using `podman`. These skills are not only vital for the RHCSA exam but also for real-world applications where containerization plays a significant role in software deployment and development.

Understanding how to efficiently search for, pull, and manage container images will streamline your workflow and ensure you're using the best practices recommended for RHEL systems. As you prepare for your RHCSA exam, practice these commands and explore further the capabilities of `podman` in managing containers.