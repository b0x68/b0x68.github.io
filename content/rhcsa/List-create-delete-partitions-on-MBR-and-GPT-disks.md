+++
title = "List, create, delete partitions on MBR and GPT disks"
date = "2024-02-16T11:47:44-05:00"
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


# Tutorial: Managing Partitions on MBR and GPT Disks for Red Hat Certified Systems Administrator Exam

In this tutorial, we will cover the objective of managing partitions on MBR and GPT disks for the Red Hat Certified Systems Administrator Exam. Managing partitions is a crucial aspect of system administration, as it allows for efficient storage allocation and organization. We will cover the basics of MBR and GPT disks, and then dive into the process of creating, deleting, and listing partitions on these types of disks.

## Understanding MBR and GPT Disks

MBR (Master Boot Record) and GPT (GUID Partition Table) are two different partitioning schemes used on disks. MBR is the traditional partitioning system, while GPT is the newer and more advanced system.

MBR partitions have been around for a long time and are widely supported by various operating systems. However, they have a limitation of only supporting up to 2TB of storage per disk. GPT, on the other hand, can support much larger storage capacities (up to 9.4 zettabytes) and has features like backup partition tables and better data protection.

It is essential to note that the process of managing partitions on MBR and GPT disks is slightly different, so it is crucial to understand which type of disk you are working with.

## Creating Partitions

### Creating Partitions on MBR Disks

1. To create a partition on an MBR disk, we will use the `fdisk` command. This command is used to create, view, or manipulate partitions on Linux systems.

2. First, list all disks on your system using the `fdisk -l` command. This will give you a list of all disks and their corresponding information, including their partition table type.

3. Once you have identified the MBR disk you want to create a partition on, use the `fdisk` command with the disk's name as an argument. For example, `fdisk /dev/sda`.

4. You will now be in the fdisk interactive mode, where you can use various commands to manage the disk's partitions. Press `n` to create a new partition.

5. Next, you will be prompted to choose between creating a primary or extended partition. Primary partitions are used for bootable volumes and cannot be further divided, while extended partitions can be divided into multiple logical volumes.

6. After selecting the partition type, you will be prompted to enter the first and last sector for the partition. The default values will use the entire disk, but you can specify a custom size.

7. Once the partition is created, use the `p` command to print the partition table and make sure the new partition is listed.

8. Finally, use the `w` command to write the changes to the disk and exit fdisk.

### Creating Partitions on GPT Disks

1. To create a partition on a GPT disk, we will use the `gdisk` command. This command is the GPT equivalent of `fdisk` and has similar functionality.

2. Use the `gdisk -l` command to list all disks on your system and identify the GPT disk you want to create a partition on.

3. Once you have identified the disk, use the `gdisk` command with the disk's name as an argument. For example, `gdisk /dev/sda`.

4. Similar to fdisk, you will now be in an interactive mode where you can use various commands to manage the disk's partitions. Use the `n` command to create a new partition.

5. Next, you will be prompted to enter the first and last sector for the partition, or you can choose to use the entire disk's size.

6. After creating the partition, you can use the `p` command to print the partition table to verify the new partition was created.

7. Finally, use the `w` command to save the changes to the disk and exit gdisk.

## Deleting Partitions

### Deleting Partitions on MBR Disks

1. To delete a partition on an MBR disk, use the `fdisk -l` command to list all disks and identify the MBR disk with the partition you want to delete.

2. Use the `fdisk` command with the disk's name as an argument to enter the interactive mode.

3. Use the `p` command to print the partition table and identify the partition you want to delete.

4. Use the `d` command to delete the selected partition.

5. Once you have deleted all desired partitions, use the `w` command to save the changes and exit fdisk.

### Deleting Partitions on GPT Disks

1. Use the `gdisk -l` command to list all disks and identify the GPT disk with the partition you want to delete.

2. Use the `gdisk` command with the disk's name as an argument to enter the interactive mode.

3. Use the `p` command to print the partition table and identify the partition you want to delete.

4. Use the `d` command to delete the selected partition.

5. Once you have deleted all desired partitions, use the `w` command to save the changes and exit gdisk.

## Listing Partitions

### Listing Partitions on MBR Disks

1. Use the `fdisk -l` command to list all disks and identify the MBR disk you want to list partitions for.

2. Use the `fdisk` command with the disk's name as an argument to enter the interactive mode.

3. Use the `p` command to print the partition table and list all partitions on the disk.

### Listing Partitions on GPT Disks

1. Use the `gdisk -l` command to list all disks and identify the GPT disk you want to list partitions for.

2. Use the `gdisk` command with the disk's name as an argument to enter the interactive mode.

3. Use the `p` command to print the partition table and list all partitions on the disk.

In conclusion, managing partitions on MBR and GPT disks is essential for efficient storage management. Understanding the differences between these partitioning schemes and the commands to create, delete, and list partitions is crucial for the Red Hat Certified Systems Administrator Exam. We hope this tutorial has provided in-depth information and guidance on managing partitions on MBR and GPT disks. Happy partitioning!