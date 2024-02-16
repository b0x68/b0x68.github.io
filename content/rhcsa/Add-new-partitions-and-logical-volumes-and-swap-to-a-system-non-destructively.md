+++
title = "Add new partitions and logical volumes, and swap to a system non-destructively"
date = "2024-02-16T10:33:37-05:00"
author = "root"
cover = ""
tags = ["system,", "systems", "volume", "volumes,", "command.", "partition.", "disk.", "`swapon`"]
keywords = ["`fdisk`", "file", "system,", "memory", "swapping", "volumes", "logical", "mount"]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Tutorial: Adding Partitions and Logical Volumes, and Swapping to a System Non-Destructively

The objective "Add new partitions and logical volumes, and swap to a system non-destructively" in Red Hat Certified Systems Administrator Exam 200 requires a thorough understanding of partitioning and logical volume management in Linux. In this tutorial, we will cover the steps to add new partitions and logical volumes, and swap to a system non-destructively on a Red Hat Enterprise Linux system.

## Introduction to Partitioning and Logical Volume Management

Partitioning is the process of dividing a hard drive into separate sections or partitions, each with its own file system. This allows for better organization and utilization of disk space. Logical volume management (LVM) is a tool used to manage the storage on a Linux system by creating logical volumes from physical volumes, allowing for flexibility in managing storage.

## Preparing for Partitioning and LVM

Before we begin adding new partitions and logical volumes, we need to make sure we have the necessary tools and a basic understanding of the current storage setup.

### Required Tools

For this tutorial, we will be using the `parted` and `lvcreate` commands, which are commonly available in most Linux distributions.

### Understanding Current Storage Setup

To view the current storage setup on your system, you can use the `lsblk` command, which displays the block devices connected to your system. Take note of the existing partitions and their file systems, as well as the size of the disk.

## Adding New Partitions

The `parted` command allows us to interactively add new partitions to a disk. Follow the steps below to create a new partition:

1. First, unmount the disk that we want to partition. This is important as any changes made to a mounted disk are not recognized until it is remounted.

2. Next, run the `parted` command with the disk device name as an argument. For example, `parted /dev/sda`.

3. Once in the `parted` interactive prompt, type `print` to view the existing partitions on the disk.

4. To create a new partition, type `mkpart` followed by the desired file system type (e.g. `mkpart ext4`).

5. Enter the start and end points for the new partition in sectors. You can use the default values suggested by `parted` by pressing enter for both start and end points.

6. Finally, type `print` to confirm that the new partition has been created. You can also use the `lsblk` command to verify the creation of the new partition.

## Creating Logical Volumes

After creating a new partition, we can now use LVM to create logical volumes from the partition and make them available for use by the system.

1. Use the `fdisk` command to view the list of available partitions, and identify the newly created partition.

2. Next, use the `pvcreate` command with the partition device name as an argument to initialize the partition as a physical volume for LVM.

3. Use the `vgcreate` command to create a volume group, which is a collection of physical volumes. The syntax for this command is `vgcreate <vg_name> <pv_name>`.

4. Once the volume group is created, we can use the `lvcreate` command to create a logical volume from the volume group. The syntax is `lvcreate -n <lv_name> -L <size> <vg_name>`.

5. Finally, use the `mkfs` command to create a file system on the newly created logical volume.

## Swapping to a System Non-Destructively

Adding a swap partition or swap file to a system allows for better memory management, as it serves as extra memory when the system runs out of physical RAM. In order to swap to a system non-destructively, we will add a swap partition using the steps outlined below.

1. First, identify the partition that will be used for swap. This can be a newly created partition or an existing one.

2. Next, execute the `mkswap` command with the partition device name as an argument to initialize the partition for swap use.

3. Use the `swapon` command to enable the swap partition. You can also add the swap partition to the `/etc/fstab` file to automatically mount the partition on system boot.

4. Verify that the swap partition is active and in use by using the `swapon -s` command.

## Conclusion

In this tutorial, we have covered the process of adding new partitions and logical volumes, as well as swapping to a system non-destructively. These skills are essential for managing storage on a Red Hat Enterprise Linux system, and will be tested in the Red Hat Certified Systems Administrator Exam 200. By following these steps and practicing in a lab environment, you will be well-prepared for this objective.