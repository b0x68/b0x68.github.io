# Tech Tutorial: Configure Local Storage on Red Hat Enterprise Linux

In this tutorial, we will focus on a critical skill set required for the Red Hat Certified System Administrator (RHCSA) exam: configuring local storage in Red Hat Enterprise Linux (RHEL). We'll cover the steps to list, create, and format partitions, and manage logical volumes. This guide will provide detailed instructions and code samples, ensuring you have hands-on knowledge to tackle local storage configuration tasks effectively.

## Introduction

Managing local storage is a foundational task for any system administrator. In RHEL, this often involves handling physical disks, creating partitions, and managing logical volumes. Understanding these elements is crucial for system performance and crucial data management practices.

### Key Concepts:

- **Partitions:** These are divisions on a physical disk that allow you to separate data logically.
- **File Systems:** This is the system used to control how data is stored and retrieved. Without a file system, stored information would be one large body of data without the ability to tell where one piece of data stops and the next begins.
- **Logical Volume Manager (LVM):** LVM is a device mapper that provides logical volume management for the Linux kernel. It is extremely flexible and facilitates the management of disk storage space.

## Step-by-Step Guide

### Step 1: Listing Current Disk Storage with `lsblk` and `fdisk`

Before making any changes, it's essential to understand the current storage setup:

```bash
# List all block devices along with mount points
lsblk

# Detailed view of disk partitions
sudo fdisk -l
```

### Step 2: Creating Partitions Using `fdisk`

`fdisk` is a powerful utility for disk partitioning. To create a new partition:

```bash
# Start fdisk on a specific disk, for example /dev/sda
sudo fdisk /dev/sda

# Within fdisk, use 'n' to create a new partition
n

# Follow the prompts to specify partition type, number, and size
# Use 'w' to write the new partition table to disk
w
```

After partitioning, it's always a good practice to verify the changes:

```bash
sudo fdisk -l /dev/sda
```

### Step 3: Creating File Systems

Once you have your partition, you'll need to create a file system on it:

```bash
# Create an ext4 file system on the new partition (e.g., /dev/sda1)
sudo mkfs.ext4 /dev/sda1
```

### Step 4: Mounting the File System

To use the new partition, mount it:

```bash
# Create a mount point directory
sudo mkdir /mnt/data

# Mount the new partition
sudo mount /dev/sda1 /mnt/data
```

**Persisting Mounts:** To ensure the partition is mounted automatically at boot, add it to `/etc/fstab`:

```bash
echo '/dev/sda1 /mnt/data ext4 defaults 0 0' | sudo tee -a /etc/fstab
```

### Step 5: Managing Logical Volumes with LVM

LVM allows for more flexibility than traditional partitioning.

1. **Create Physical Volume:**

   ```bash
   sudo pvcreate /dev/sda2
   ```

2. **Create Volume Group:**

   ```bash
   sudo vgcreate vgdata /dev/sda2
   ```

3. **Create Logical Volume:**

   ```bash
   sudo lvcreate -n lvdata -L 10G vgdata
   ```

4. **Create File System on Logical Volume:**

   ```bash
   sudo mkfs.ext4 /dev/vgdata/lvdata
   ```

5. **Mount Logical Volume:**

   ```bash
   sudo mkdir /mnt/lvdata
   sudo mount /dev/vgdata/lvdata /mnt/lvdata
   ```

## Conclusion

In this tutorial, we've gone through the essential steps of configuring local storage on RHEL, including partitioning disks, creating file systems, and using LVM to manage logical volumes. These tasks form the backbone of system administration in a RHEL environment, ensuring data is organized and accessible. Mastery of these skills is crucial for anyone preparing for the RHCSA exam and for effective management of Linux systems in production.