# Tech Tutorial: Configure Local Storage

## Introduction

Managing disk storage is a fundamental skill for system administrators and IT professionals. This tutorial covers how to list, create, and delete partitions on both Master Boot Record (MBR) and GUID Partition Table (GPT) disks. Understanding these operations is crucial for deploying and maintaining robust storage solutions.

## Prerequisites

- A computer running Linux or Windows
- Administrative access to the system
- Basic familiarity with the command line interface

## Step-by-Step Guide

### Understanding MBR and GPT

Before diving into the practical steps, let's briefly understand the two types of disk partitioning systems:

- **MBR (Master Boot Record):** An older partitioning scheme used in PCs. It supports up to four primary partitions per disk or three primary partitions and one extended partition containing logical drives. MBR is limited to 2TB disk size.

- **GPT (GUID Partition Table):** A more modern system required for initializing disks larger than 2TB. GPT supports up to 128 partitions by default in Windows and does not need extended or logical partitions.

### Tools We Will Use

- **Linux:** `fdisk` (for MBR), `gdisk` (for GPT)
- **Windows:** Disk Management GUI, `diskpart` command line tool

### Detailed Code Examples

#### Linux

##### Listing Partitions

1. **List partitions for MBR and GPT:**

   ```bash
   sudo fdisk -l
   ```

   This command lists all partitions and shows whether a disk is using MBR or GPT.

##### Creating Partitions

2. **Create an MBR partition:**

   ```bash
   sudo fdisk /dev/sdx
   ```

   Replace `/dev/sdx` with your disk identifier. Use the `n` command to create a new partition, `p` for primary, `e` for extended, and follow the prompts to specify the partition size.

   After creating the partition, use `w` to write changes to the disk.

3. **Create a GPT partition:**

   ```bash
   sudo gdisk /dev/sdx
   ```

   Similar to `fdisk`, but `gdisk` is used for GPT disks. Use `n` to create a new partition and follow the prompts to allocate space. Use `w` to write changes.

##### Deleting Partitions

4. **Delete a partition in `fdisk` and `gdisk`:**

   When running either `fdisk` or `gdisk`, use the `d` command to delete a partition and `w` to write changes.

#### Windows

##### Using Disk Management

- **List/Create/Delete Partitions:**

  1. Open Disk Management by right-clicking on "This PC" > "Manage" > "Disk Management".
  2. Right-click on the unallocated space to create a new partition or on an existing partition to delete or format it.
  3. Follow the wizard for creating new partitions.

##### Using `diskpart`

1. **Open Command Prompt as Administrator and type `diskpart`.**

2. **List disks:**

   ```plaintext
   list disk
   ```

3. **Select disk:**

   ```plaintext
   select disk 0
   ```

4. **List partitions:**

   ```plaintext
   list partition
   ```

5. **Create a partition:**

   ```plaintext
   create partition primary size=20480
   ```

   This creates a 20GB partition.

6. **Delete a partition:**

   ```plaintext
   select partition 1
   delete partition
   ```

## Conclusion

Managing disk partitions is crucial for effective storage management. Whether you're using a GUI like Windows Disk Management or command-line tools like `fdisk`, `gdisk`, or `diskpart`, understanding these operations can help you optimize storage configurations. Always ensure you back up data before modifying disk partitions to avoid data loss.

Experiment safely by using virtual machines or spare disks to get comfortable with these tools and processes before working on critical systems.