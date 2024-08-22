# Tech Tutorial: Configure Local Storage

## Introduction

Local storage configuration is a critical skill for system administrators and IT professionals, particularly when dealing with physical volumes in a Linux environment. This tutorial focuses on an essential exam objective: **Create and Remove Physical Volumes**. We will explore how to manage physical volumes using the Logical Volume Manager (LVM) on a Linux system, which allows for flexible management of disk space.

## Prerequisites

Before proceeding, ensure you have the following:
- A Linux system (CentOS, Ubuntu, or any other distribution)
- At least one non-mounted disk or disk partition available for experiments
- Root or sudo access

## Step-by-Step Guide

### Step 1: Installing LVM Tools

First, we need to make sure that the LVM2 package is installed on our system. You can install it using the package manager of your Linux distribution.

For **Debian/Ubuntu** systems:

```bash
sudo apt update
sudo apt install lvm2
```

For **CentOS/RHEL** systems:

```bash
sudo yum install lvm2
```

### Step 2: Checking Available Disks

Before creating physical volumes, identify the disks available on your system using `lsblk`:

```bash
lsblk
```

Look for disks without mount points (not mounted), which are available for LVM.

### Step 3: Create Physical Volumes

To create a physical volume, you use the `pvcreate` command. Suppose you have a disk named `/dev/sdb` that is not mounted and is available for use.

```bash
sudo pvcreate /dev/sdb
```

You can verify that the physical volume was successfully created by running:

```bash
sudo pvs
```

or 

```bash
sudo pvdisplay
```

### Step 4: Removing Physical Volumes

To remove a physical volume, it should not be part of any volume group. If it's part of a group, you must remove it from the group first (which is beyond this tutorial's scope).

Suppose `/dev/sdb` is the physical volume you want to remove:

First, ensure it's not part of any volume group:

```bash
sudo pvs
```

Next, use `pvremove`:

```bash
sudo pvremove /dev/sdb
```

If the physical volume is removed successfully, `pvremove` will not return any error.

## Detailed Code Examples

Here's a more complex scenario where you create multiple physical volumes and eventually remove them.

**Creating multiple physical volumes:**

Suppose you have three disks: `/dev/sdb`, `/dev/sdc`, and `/dev/sdd`.

```bash
sudo pvcreate /dev/sdb /dev/sdc /dev/sdd
sudo pvs
```

**Removing these physical volumes:**

First, check if they are part of any volume group:

```bash
sudo vgs
```

If they are free, remove them:

```bash
sudo pvremove /dev/sdb /dev/sdc /dev/sdd
```

## Conclusion

This tutorial covered the basics of creating and removing physical volumes using LVM in Linux. Mastering these operations is foundational for managing storage effectively in Linux environments. By practicing these commands, you can prepare for related exam objectives and develop skills that are crucial for real-world system administration. Always remember to perform these operations in a test environment or on non-critical systems to avoid data loss.