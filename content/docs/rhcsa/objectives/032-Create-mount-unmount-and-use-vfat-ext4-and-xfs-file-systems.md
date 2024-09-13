# Tech Tutorial: Create and Configure File Systems on Red Hat Enterprise Linux

Welcome to this detailed technical tutorial designed for candidates preparing for the Red Hat Certified System Administrator (RHCSA) exam. This tutorial aims to cover key competencies in managing file systems on Red Hat Enterprise Linux (RHEL), specifically focusing on creating, mounting, unmounting, and using vfat, ext4, and xfs file systems.

## Introduction

File systems are an integral part of any operating system. They determine how data is stored and retrieved by the OS. For the RHCSA exam, it is crucial to understand how to work with different types of file systems. This guide will focus on three popular file systems used in RHEL:

- **VFAT**: A compatible file system with FAT32, useful for compatibility with various systems, including Windows.
- **EXT4**: An evolution of the earlier EXT file systems, providing deep directory structures and large file sizes.
- **XFS**: A high-performance file system designed for high scalability.

In this tutorial, we’ll go through the process of creating, mounting, unmounting, and using these file systems on RHEL.

## Step-by-Step Guide

### 1. Installing Necessary Tools

Before you begin, ensure your system has the necessary tools installed. Use `yum` to install utilities like `parted` and `xfsprogs`:

```bash
sudo yum install parted xfsprogs
```

### 2. Creating a File System

#### Creating VFAT File System

1. Identify the device where you want to create the file system. For example, `/dev/sdb1`.
2. Use the `mkfs.vfat` command to create a VFAT file system:

```bash
sudo mkfs.vfat /dev/sdb1
```

#### Creating EXT4 File System

1. If you haven’t already created a partition, use `parted` or another tool to partition your disk.
2. Create an EXT4 file system:

```bash
sudo mkfs.ext4 /dev/sdb2
```

#### Creating XFS File System

1. Similarly, ensure you have a partition ready. Here, we use `/dev/sdb3`.
2. Use the following command to create an XFS file system:

```bash
sudo mkfs.xfs /dev/sdb3
```

### 3. Mounting a File System

To mount a file system, use the `mount` command. Ensure you have a directory to mount the file system to.

```bash
sudo mkdir /mnt/myvfat
sudo mount -t vfat /dev/sdb1 /mnt/myvfat

sudo mkdir /mnt/myext4
sudo mount -t ext4 /dev/sdb2 /mnt/myext4

sudo mkdir /mnt/myxfs
sudo mount -t xfs /dev/sdb3 /mnt/myxfs
```

### 4. Unmounting a File System

When you’re done working with the file systems, it’s a good practice to unmount them:

```bash
sudo umount /mnt/myvfat
sudo umount /mnt/myext4
sudo umount /mnt/myxfs
```

## Detailed Code Examples

### Example: Checking Disk Space Usage

After mounting the file systems, you may want to check how much disk space each file system is using. Use the `df` command:

```bash
df -hT
```

### Example: Managing File System Mounts at Boot

To automate the mounting process at boot, you’ll need to edit `/etc/fstab`. Here’s how you might add an entry for the ext4 file system:

1. Open `/etc/fstab` in a text editor:
   ```bash
   sudo vi /etc/fstab
   ```
2. Add the following line:
   ```
   /dev/sdb2 /mnt/myext4 ext4 defaults 0 2
   ```

This line tells the system to mount `/dev/sdb2` at `/mnt/myext4` using the ext4 file system with default options.

## Conclusion

In this tutorial, you have learned how to create, mount, unmount, and manage VFAT, EXT4, and XFS file systems on Red Hat Enterprise Linux. These skills are essential for any system administrator, especially those preparing for the RHCSA exam. Practice these commands and ensure you understand how these file systems differ and what their advantages are. Good luck with your certification!