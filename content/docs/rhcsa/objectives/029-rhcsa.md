# Tech Tutorial: Configure Local Storage - Creating and Deleting Logical Volumes

In this tutorial, we will delve into how to manage storage space effectively by creating and deleting logical volumes. Logical Volume Management (LVM) is a widely used technique in Linux environments that allows administrators to create a layer of abstraction over physical storage, enabling flexible disk management without being bound to physical disk sizes.

## Introduction

Managing disk space efficiently is critical in ensuring that your systems run smoothly without running out of space unexpectedly. Logical Volume Management (LVM) provides the flexibility to allocate disks and manage storage space in a more refined way. Unlike traditional disk management where resizing disks can be disruptive and difficult, LVM allows for resizing volumes online and makes it easier to manage files and applications that require specific partitioning.

### What is a Logical Volume?

A logical volume is a virtual block device that appears as a regular hard drive to applications and the operating system. Logical volumes are created within a volume group, which aggregates physical volumes, which can be entire hard disks or disk partitions.

## Prerequisites

- A Linux system with LVM support installed. Most modern Linux distributions come with LVM support.
- At least one unused disk or disk partition available for LVM setup.
- Basic familiarity with Linux command line interface (CLI).

## Step-by-Step Guide

This guide will cover the following steps:
1. Installing LVM tools
2. Preparing physical volumes
3. Creating a volume group
4. Creating logical volumes
5. Deleting logical volumes

### Step 1: Installing LVM Tools

Before we start, ensure that the LVM2 package is installed on your system. You can install it using your distribution’s package manager.

For Debian-based systems:

```bash
sudo apt-get update
sudo apt-get install lvm2
```

For Red Hat-based systems:

```bash
sudo yum install lvm2
```

### Step 2: Preparing Physical Volumes

First, identify the disk or partition you want to use. You can list all disks and partitions using:

```bash
lsblk
```

Suppose `/dev/sdb` is the disk you want to use. Initialize it as a physical volume:

```bash
sudo pvcreate /dev/sdb
```

### Step 3: Creating a Volume Group

Create a volume group named `vg01` using the physical volume we just prepared:

```bash
sudo vgcreate vg01 /dev/sdb
```

You can confirm that the volume group is created by listing all volume groups:

```bash
sudo vgs
```

### Step 4: Creating Logical Volumes

Now, let’s create a logical volume. Here, we will create a logical volume named `lv01` in `vg01` with a size of 10GB:

```bash
sudo lvcreate -n lv01 -L 10G vg01
```

You can list the logical volumes with:

```bash
sudo lvs
```

### Step 5: Deleting Logical Volumes

To delete a logical volume, first ensure that it is not in use. Unmount any filesystems using it, and then run:

```bash
sudo lvremove /dev/vg01/lv01
```

Confirm the deletion by listing the logical volumes again:

```bash
sudo lvs
```

## Conclusion

This tutorial provided a comprehensive guide on how to create and delete logical volumes using LVM on Linux. By mastering these skills, you can efficiently manage disk space, which is crucial for maintaining system stability and scalability. With LVM, you gain the flexibility to resize and allocate storage dynamically, which is a significant advantage in complex system architectures.