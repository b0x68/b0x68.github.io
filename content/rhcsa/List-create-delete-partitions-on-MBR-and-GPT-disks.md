+++
title = "List, create, delete partitions on MBR and GPT disks"
date = "2024-02-16T10:32:43-05:00"
author = "root"
cover = ""
tags = ["fdisk", "partition", "linux.", "command", "filesystem", "partition,", "terminal:", "(logical/physical):"]
keywords = ["command,", "disk,", "logical", "`fdisk`", "disk", "filesystem", "command", "partition"]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Red Hat Certified Systems Administrator Exam 200 Objective: "List, create, delete partitions on MBR and GPT disks"

In this tutorial, we will be discussing the objective of listing, creating, and deleting partitions on both MBR (Master Boot Record) and GPT (GUID Partition Table) disks for the Red Hat Certified Systems Administrator (RHCSA) Exam 200. This objective falls under the "Storage Management" topic and is one of the essential skills required for managing storage on Red Hat Enterprise Linux.

## Understanding Partitioning

Before we dive into listing, creating, and deleting partitions, let's first understand what partitioning is. A partition is a logical division of a physical hard disk, and it is used to organize and manage data on the disk. With partitions, you can split a hard drive into smaller sections, which can then be used to install different operating systems or store different types of data.

MBR and GPT are two different partitioning schemes used in modern computers. MBR has been the standard for a long time, while GPT is the new and preferred partitioning scheme. GPT offers several advantages over MBR, such as support for larger disks, more partitions, and improved data integrity. However, both MBR and GPT have their use cases, and it is essential to know how to work with both of them.

## Listing Partitions

To list the partitions on a disk, we will be using the `fdisk` command. This command is used to manipulate and list partition tables on disks. To view the current partition table for a particular disk, run the following command in the terminal:

`sudo fdisk -l /dev/sdX`

Replace `sdX` with the disk name you want to view. This will display a list of the partitions on the disk, their type, and size. The output may look something like this:

```
Disk /dev/sda: 500 GiB, 536870912000 bytes, 1048576000 sectors
Disk model: TOSHIBA DT01ACA0
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
Disklabel type: gpt
Disk identifier: 2CE5FAF2-2919-4091-8F92-1B544369E07A

Device       Start       End   Sectors   Size Type
/dev/sda1     2048   1050623   1048576   512M EFI System
/dev/sda2  1050624 316254975 315204352 150.3G Linux filesystem
/dev/sda3 316254976 355239679  38984704  18.6G Linux swap
/dev/sda4 355239680 957914879 602675200 287.3G Linux filesystem
```

You can also use the `lsblk` command to list the partitions on a disk in a tree-like format. This command shows the relationships between different block devices, such as disks and partitions. To run this command, use the following syntax:

`sudo lsblk`

## Creating Partitions

To create a partition on a disk, we will be using the `fdisk` command as well. First, run the `sudo fdisk /dev/sdX` command to enter the fdisk interactive mode. You will be prompted with the following message:

```
Welcome to fdisk (util-linux 2.23.2).

Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

```

To create a new partition, follow these steps:

1. Type `n` and press Enter to create a new partition.
2. Select the partition type by typing `p` for primary or `e` for extended (if you are using MBR partitioning scheme).
3. Select the partition number, starting from 1. If you already have existing partitions, make sure that the new partition does not conflict with any existing ones.
4. Set the partition's size by entering the start and end sector or the desired size in bytes, kilobytes, megabytes, etc.
5. After setting the partition's size, use the `t` command followed by the partition number to change the partition type if needed.
6. Repeat these steps if you want to create more partitions.
7. Once you are done, use the `w` command to write the partition table to the disk.

## Deleting Partitions

To delete a partition on a disk, you can follow the same steps as in the previous section, but instead of creating a partition, you will use the `d` command to delete an existing partition. This command will prompt you to enter the partition number you want to delete. After confirming the deletion, use the `w` command to write the changes to the disk.

## Conclusion

In this tutorial, we have discussed the objective of listing, creating, and deleting partitions on both MBR and GPT disks for the Red Hat Certified Systems Administrator (RHCSA) Exam 200. We have also learned how to use the `fdisk` command to manage partitions and the `lsblk` command to list partitions in a tree-like format. By mastering this objective, you will be well-prepared to manage storage on Red Hat Enterprise Linux.