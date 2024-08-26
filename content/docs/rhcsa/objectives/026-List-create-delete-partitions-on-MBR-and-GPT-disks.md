# Tech Tutorial: Configure Local Storage

## Introduction
In this tutorial, we will delve into the management of disk partitions on both MBR (Master Boot Record) and GPT (GUID Partition Table) disks. Understanding how to list, create, and delete partitions on these types of disks is crucial for system administrators, IT professionals, and anyone interested in the maintenance or setup of computer systems.

### What are MBR and GPT?
- **MBR (Master Boot Record)** is an older disk-labeling scheme that's used on disks smaller than 2TB. MBR disks support up to four primary partitions, or three primary partitions and one extended partition containing logical drives.

- **GPT (GUID Partition Table)** is a newer standard that supports larger disks and allows for a virtually unlimited number of partitions. It's required for initializing disks larger than 2TB and is part of the UEFI (Unified Extensible Firmware Interface) standard.

## Prerequisites
- A system running Linux or Windows.
- A disk or virtual disk to practice on.
- Basic command-line interface skills.

## Step-by-Step Guide

### 1. Listing Partitions
Before creating or deleting partitions, it's essential to know how to list existing partitions to understand the current disk layout.

#### On Linux:

```bash
sudo fdisk -l
```
This command will list all available disks and their partitions.

#### On Windows:
Open Command Prompt as Administrator and run:

```cmd
diskpart
list disk
```
This lists all disks. To see partitions on a specific disk:

```cmd
select disk 0
list partition
```
Replace `0` with the disk number you want to inspect.

### 2. Creating Partitions

#### Creating a Partition on MBR Disk

##### On Linux:
```bash
sudo fdisk /dev/sdx
```
Replace `/dev/sdx` with your disk, and follow the interactive menu to create a new partition.

##### On Windows:
```cmd
select disk 0
create partition primary size=20480
```
This creates a new primary partition of 20 GB.

#### Creating a Partition on GPT Disk

##### On Linux:
```bash
sudo gdisk /dev/sdx
```
Use the `n` command to create a new partition and follow the prompts.

##### On Windows:
```cmd
convert gpt
create partition primary size=20480
```
This converts the disk to GPT and creates a 20 GB partition.

### 3. Deleting Partitions

#### Deleting a Partition on MBR Disk

##### On Linux:
```bash
sudo fdisk /dev/sdx
```
Use the `d` command to delete a partition.

##### On Windows:
```cmd
select partition 1
delete partition
```
This deletes partition 1. Be sure you select the correct partition.

#### Deleting a Partition on GPT Disk

##### On Linux:
```bash
sudo gdisk /dev/sdx
```
Use the `d` command to delete a partition.

##### On Windows:
```cmd
select partition 1
delete partition
```
Ensure you select the correct partition to delete.

## Detailed Code Examples

Here we focus on the Linux side, particularly useful for scripting and automation:

### Script to List, Create, and Delete a Partition on Linux

```bash
#!/bin/bash

# List partitions
echo "Current partitions:"
sudo fdisk -l /dev/sdx

# Create a partition
echo "Creating a new partition..."
echo -e "n\np\n1\n\n+1G\nw" | sudo fdisk /dev/sdx

# List partitions to confirm creation
echo "Updated partition table:"
sudo fdisk -l /dev/sdx

# Delete the partition
echo "Deleting the created partition..."
echo -e "d\nw" | sudo fdisk /dev/sdx

# Final list to confirm deletion
echo "Final partition table:"
sudo fdisk -l /dev/sdx
```
This script demonstrates listing, creating a 1GB partition, and then deleting that partition.

## Conclusion
Understanding how to manage disk partitions in both MBR and GPT disks is a fundamental skill in system administration. This tutorial provided you with the necessary commands and scripts to successfully list, create, and delete partitions on these disks. Practice these commands in a safe environment to master the partitioning of both MBR and GPT disks effectively.