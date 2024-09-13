# Tech Tutorial: Configure Local Storage on RHEL

## Introduction

In this tutorial, we will delve into managing local storage on a Red Hat Enterprise Linux (RHEL) system, focusing on how to list, create, and delete partitions on both MBR (Master Boot Record) and GPT (GUID Partition Table) disks. This knowledge is crucial for system administrators preparing for the Red Hat Certified Systems Administrator (RHCSA) exam.

We will use specific RHEL commands and tools, ensuring that the examples are directly applicable for RHEL environments.

## Prerequisites

- A system running RHEL 7 or RHEL 8
- Basic familiarity with terminal and command line operations
- Root or sudo privileges on the system

## Step-by-Step Guide

### 1. Listing Existing Partitions

Before modifying disk partitions, it's essential to understand the current partition layout. We'll use the `lsblk` and `fdisk` commands.

#### Using `lsblk`

The `lsblk` command lists all available block devices along with their partitions.

```bash
sudo lsblk
```

Output:
```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda      8:0    0   20G  0 disk 
├─sda1   8:1    0    1G  0 part /boot
└─sda2   8:2    0   19G  0 part 
  ├─rhel-root 253:0    0   17G  0 lvm  /
  └─rhel-swap 253:1    0    2G  0 lvm  [SWAP]
```

#### Using `fdisk`

To view more detailed information, including the disk label type, use `fdisk`.

```bash
sudo fdisk -l /dev/sda
```

### 2. Creating Partitions

We will use `fdisk` for MBR and `gdisk` for GPT. Here's how to create a new partition.

#### MBR Partitions with `fdisk`

1. Start `fdisk` on the target device:

   ```bash
   sudo fdisk /dev/sda
   ```

2. To create a new partition, press `n`. Then choose `p` for primary and specify the partition number, start sector, and size (e.g., +500M for 500 MB).

3. To save the changes and exit, press `w`.

#### GPT Partitions with `gdisk`

1. Start `gdisk` on the target device:

   ```bash
   sudo gdisk /dev/sda
   ```

2. Press `n` to create a new partition, accept the defaults or specify the partition number, first sector, and size.

3. To write the table to disk and exit, press `w`.

### 3. Deleting Partitions

#### Deleting with `fdisk`

1. Start `fdisk`:

   ```bash
   sudo fdisk /dev/sda
   ```

2. Press `d` to delete a partition. Specify the partition number.

3. Press `w` to write changes.

#### Deleting with `gdisk`

1. Start `gdisk`:

   ```bash
   sudo gdisk /dev/sda
   ```

2. Press `d` to delete a partition and enter the partition number.

3. Press `w` to write changes.

## Detailed Code Examples

Here's a complete example of creating and deleting a partition using `fdisk` on an MBR disk:

```bash
# Listing partitions
sudo fdisk -l /dev/sda

# Creating a new partition
sudo fdisk /dev/sda
n
p
3
[default]
+1G
w

# Deleting the partition
sudo fdisk /dev/sda
d
3
w
```

## Conclusion

Understanding how to list, create, and delete partitions on MBR and GPT disks is essential for managing storage on RHEL systems. This tutorial covered the commands and procedures necessary for these tasks, providing a solid foundation for those preparing for the RHCSA exam.

Remember, always back up data before modifying disk partitions to avoid data loss. Happy learning and good luck with your RHCSA preparation!