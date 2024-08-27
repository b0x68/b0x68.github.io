# Tech Tutorial: Create and Configure File Systems

## Introduction

In this tutorial, we will delve into how to create and configure file systems on a Linux system, specifically focusing on Red Hat Enterprise Linux. As a fundamental task for a Red Hat Certified System Administrator (RHCSA), understanding file systems is crucial for effective system management. This includes creating, mounting, unmounting, and maintaining persistent file system configurations.

## Prerequisites

- A Red Hat Enterprise Linux 8 installation
- Root privileges or access via the `sudo` command

## Step-by-Step Guide

### Step 1: Listing Current File Systems

Before creating new file systems, it's important to understand what is already available. Use the `lsblk` command to list all block devices and their mount points if applicable:

```bash
lsblk
```

### Step 2: Creating a New Partition

For creating a new file system, you first need a new partition. We will use `fdisk` for creating a new partition.

1. List available disks:
   ```bash
   fdisk -l
   ```
2. Start `fdisk` on a specific disk, e.g., `/dev/sda`:
   ```bash
   sudo fdisk /dev/sda
   ```
3. Follow the interactive menu to create a new partition. Typical commands within `fdisk` are:
   - `n` to create a new partition
   - `p` for primary partition
   - `1` for partition number
   - Then specify the start and end blocks
   - `w` to write the new partition table to disk

### Step 3: Creating a File System

After partitioning, you need to create a file system on the partition. Assume we created `/dev/sda1`:

1. Create an ext4 file system:
   ```bash
   sudo mkfs.ext4 /dev/sda1
   ```
   Replace `ext4` with `xfs` or another file system type if desired.

### Step 4: Mounting the File System

To use the new file system, mount it:

1. Create a mount point:
   ```bash
   sudo mkdir /mnt/newdisk
   ```
2. Mount the file system:
   ```bash
   sudo mount /dev/sda1 /mnt/newdisk
   ```

### Step 5: Ensuring Persistence through `fstab`

Mounts created via the `mount` command are temporary. To make the mount persist through reboots, you need to add it to `/etc/fstab`:

1. Open `/etc/fstab` in a text editor:
   ```bash
   sudo nano /etc/fstab
   ```
2. Add the following line:
   ```
   /dev/sda1    /mnt/newdisk   ext4    defaults    0   2
   ```
3. Save and close the file. Test the entry:
   ```bash
   sudo mount -a
   ```
   This command will mount all filesystems mentioned in `fstab`.

### Step 6: Checking and Repairing File Systems

Use `fsck` to check and repair file systems (not mounted or mounted read-only):
```bash
sudo umount /mnt/newdisk
sudo fsck /dev/sda1
sudo mount /dev/sda1 /mnt/newdisk
```

## Detailed Code Examples

Here’s a complete script that automates the creation of a partition, formats it, and updates `fstab`:

```bash
#!/bin/bash
echo "Starting disk preparation..."
sudo fdisk /dev/sda << EEOF
n
p
1

+1G
w
EEOF

echo "Creating file system..."
sudo mkfs.ext4 /dev/sda1

echo "Creating mount point..."
sudo mkdir /mnt/newdisk

echo "Updating fstab..."
echo "/dev/sda1    /mnt/newdisk   ext4    defaults    0   2" | sudo tee -a /etc/fstab

echo "Mounting all file systems..."
sudo mount -a

echo "Disk preparation complete."
```

## Conclusion

In this tutorial, we covered the essential steps for creating and configuring file systems on a Red Hat system, which is a critical skill for any system administrator. By following the steps outlined, you can efficiently manage disk resources and ensure data is correctly stored and retrieved in a Linux environment. Remember, always back up critical data before modifying disk partitions or file systems.