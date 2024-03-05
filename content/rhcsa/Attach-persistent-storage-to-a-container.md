+++
title = "Attach persistent storage to a container"
date = "2024-02-16T11:55:20-05:00"
author = "root"
cover = "container-storage.png"
tags = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
keywords = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
description = "Attaching persistent storage to a container on a Red Hat Enterprise Linux system."
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# How to Attach Persistent Storage to a Container in Red Hat Certified Systems Administrator Exam 200

## Introduction
One of the key skills that is assessed in the Red Hat Certified Systems Administrator Exam 200 is the ability to attach persistent storage to a container. This tutorial will guide you through the process of attaching persistent storage to a container on a Red Hat Enterprise Linux system. 

## Prerequisites
Before we begin, make sure that you have the following prerequisites:
- A Red Hat Enterprise Linux system with Docker installed.
- Basic knowledge of Docker and containers.
- Basic knowledge of persistent storage and file systems.
- Root or sudo privileges on the system.

## Step 1: Check Storage Availability
The first step is to check the storage availability on your system. This can be done by using the `df` command, which displays the currently available storage volumes and their mount points. Ensure that you have enough available space for the persistent storage that you want to attach to the container.

## Step 2: Create a Persistent Storage Volume
Next, you need to create a persistent storage volume that will be attached to the container. This can be achieved using a variety of methods, such as LVM, NFS, or GlusterFS. In this tutorial, we will be using a normal ext4 file system for our persistent storage. 

To create the persistent storage volume, follow these steps:

1. Choose a location for your persistent storage volume, preferably on a separate partition or disk.
2. Create a new partition using the `parted` or `fdisk` command.
3. Format the partition to the ext4 file system using the `mkfs` command.
4. Create a mount point for the persistent storage using the `mkdir` command.
5. Mount the persistent storage volume to the mount point using the `mount` command.
6. Verify that the persistent storage is successfully mounted by using the `df` command.

## Step 3: Start a Container
Now that we have our persistent storage volume ready, we can start a container and attach the storage to it. To start a container, you can use the `docker run` command, specifying the persistent storage volume with the `--volume` flag. For example:

```
docker run -it --name mycontainer --volume /path/to/persistent/storage:/container/storage:Z <image_name>
```

In this command, we are starting a container with the name `mycontainer` and attaching the persistent storage volume located at `/path/to/persistent/storage` to the container's internal storage location at `/container/storage`.

Note the use of the `:Z` at the end of the volume flag. This is important because it sets the security context of the persistent storage to match that of the container, allowing the container to have the necessary read/write access to the storage.

## Step 4: Verify Persistent Storage Attachment
To verify that the persistent storage has been successfully attached to the container, you can use the `docker inspect` command. This command will display detailed information about the container, including its mounted volumes. You should see your persistent storage volume listed as a mounted volume for the container.

## Step 5: Modify Container to Use Persistent Storage
By default, the container will not automatically use the attached persistent storage. To modify the container to use the persistent storage, you need to make changes to its configuration. This can be done in several ways, such as using the `docker commit` command or editing the container's Dockerfile. For the purposes of this tutorial, we will be using the `docker commit` command to make changes to the container.

To modify the container using the `docker commit` command, follow these steps:

1. Edit the container's configuration to use the persistent storage. For example, if you want to modify the container's Apache configuration, you would edit the `/etc/httpd/conf/httpd.conf` file.
2. Stop the container using the `docker stop` command.
3. Use the `docker commit` command to create a new image from the modified container. For example:

    ```
    docker commit mycontainer myimage
    ```
    This will create a new image, named `myimage`, from the modified container `mycontainer`.

4. Start a new container using the newly created image, specifying the persistent storage volume with the `--volume` flag once again.
5. Verify that the container is now using the modified configuration, which should be accessing the persistent storage.

## Conclusion
Congratulations! You have now successfully attached persistent storage to a container on your Red Hat Enterprise Linux system. This is a valuable skill that is frequently used in production environments, and one that you will be expected to demonstrate in the Red Hat Certified Systems Administrator Exam 200. Practice and master this skill, and you will be well on your way to becoming a Red Hat Certified Systems Administrator.
