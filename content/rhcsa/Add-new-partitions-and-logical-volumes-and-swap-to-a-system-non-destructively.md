+++
title = "Add new partitions and logical volumes, and swap to a system non-destructively"
date = "2024-02-16T11:48:29-05:00"
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


# Tutorial: Adding New Partitions and Logical Volumes and Using Swap Non-Destructively

## Introduction
In this tutorial, we will be covering the objective of “Adding New Partitions and Logical Volumes and Using Swap Non-Destructively” as part of the Red Hat Certified Systems Administrator Exam 200. We will explain the process of adding new partitions and logical volumes, as well as the use of swap non-destructively on a system. This objective is essential for system administrators to understand, as partitioning and logical volumes are crucial for managing data and storage on a Linux system.

## Prerequisites
Before beginning this tutorial, please make sure that you have a basic understanding of Linux and have access to a Red Hat Enterprise Linux system. You will also need root or sudo privileges to complete the commands mentioned in this tutorial.

## Understanding Partitions and Logical Volumes
A partition is a division of a physical disk into separate sections, each with its own file system. It is used to organize and manage data on a disk. On the other hand, a logical volume is a virtual partition created from free space on one or more physical disks. It allows for more flexibility in managing the storage space compared to traditional partitions.

## Adding New Partitions
To add a new partition, we will be using the `fdisk` utility. This command can create, delete, and modify partitions on a disk. Let’s say we need to add a new partition named `/dev/sdb1` with a size of 100MB. Follow the steps below to complete this task:

1. Start by typing `sudo fdisk /dev/sdb` to access the `fdisk` utility for the specified disk. 
2. Create a new partition by typing the `n` command and press enter.
3. Select the partition type by typing `p` for primary partition or `l` for logical partition. 
4. Enter the partition number when prompted. In our case, it would be `1`.
5. Specify the starting and end cylinders for the partition. If you want to allocate the entire disk space to the partition, press enter for both fields. 
6. Once done, type `t` to assign a partition type. Consult the `fdisk` man page for a list of partition types and their corresponding codes. 
7. Finally, save the changes by typing `w` and press enter.

The new partition will now be created and available for use.

## Adding Logical Volumes
To create a logical volume, we will be using the `lvcreate` command. This command creates a new logical volume within a volume group. Here’s an example of creating a logical volume named `myvol` with a size of 200MB on the volume group `vg1`:

`sudo lvcreate -L 200M -n myvol vg1`

The `-L` flag specifies the size of the logical volume and the `-n` flag specifies the name. You can also specify the percentage of available space in the volume group instead of the exact size.

## Swap Space
Swap space is a designated space on a disk used by the operating system when the physical memory (RAM) becomes full. It acts as a backup memory, allowing the system to continue functioning even when RAM is full. To view the current swap space on your system, use the command `swapon -s`. 

### Adding Swap Space
To add a new swap space to your system, follow these steps:

1. Create a swap partition using the `fdisk` utility as explained in the previous section. 
2. Once the partition is created, use the `mkswap` command to format it as swap space. This command takes the partition name as an argument. 
3. Enable the swap space by typing `sudo swapon /dev/sdb1` where `/dev/sdb1` is the name of your swap partition.
4. To make the changes permanent, add the swap space to the `/etc/fstab` file. Open the file using a text editor and add the following line at the end:
`/dev/sdb1     swap     swap     defaults     0     0`
5. Save and close the file. The next time the system boots, the swap space will be automatically enabled.

## Conclusion
In this tutorial, we have covered the objective of “Adding New Partitions and Logical Volumes and Using Swap Non-Destructively” in great depth. We have explained the process of adding new partitions and logical volumes using `fdisk` and `lvcreate` commands. We also discussed the importance of swap space and how to add it non-destructively to a system. By following these steps, you will be able to successfully manage partitions and logical volumes on your Linux system and use swap space efficiently.