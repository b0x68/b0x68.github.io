# Tech Tutorial: Configure Local Storage

## Introduction

In this tutorial, we will delve into the basics of disk management in Linux systems, particularly focusing on how to assign physical volumes to volume groups. This task is a fundamental component of managing Logical Volume Manager (LVM), which offers considerable flexibility over traditional partitioning methods in Linux.

LVM allows for the resizing of partitions in live systems, spanning storage over multiple disks, and the ability to snapshot volumes. Understanding how to assign physical volumes to volume groups is crucial for anyone looking to manage storage efficiently in a Linux environment.

## Prerequisites

Before diving into the tutorial, ensure you have the following:
- A Linux system with root or sudo privileges
- At least one unpartitioned disk or unallocated space available
- LVM2 package installed (It usually comes pre-installed in most Linux distributions)

You can install LVM2 on Debian-based systems using:

```bash
sudo apt-get install lvm2
```

And on RedHat-based systems using:

```bash
sudo yum install lvm2
```

## Step-by-Step Guide

### Step 1: Checking for Available Disks

First, we need to identify the disks available on the system that can be used to create physical volumes. You can list all disks and their partitions using:

```bash
sudo fdisk -l
```

Look for disks with no partitions or free space.

### Step 2: Creating Physical Volumes

Once you have identified a suitable disk, you can create a physical volume on it. Let's assume the disk is `/dev/sdb`.

Create a physical volume using:

```bash
sudo pvcreate /dev/sdb
```

You can verify the creation by listing all physical volumes:

```bash
sudo pvs
```

or

```bash
sudo pvdisplay
```

### Step 3: Creating a Volume Group

Now that the physical volume is ready, the next step is to create a volume group. You can create a volume group named `vg01` using:

```bash
sudo vgcreate vg01 /dev/sdb
```

Verify the creation of the volume group:

```bash
sudo vgs
```

or

```bash
sudo vgdisplay
```

### Step 4: Assigning Physical Volumes to Volume Groups

If you have additional physical volumes, you can extend the volume group by adding more physical volumes. Suppose you have another disk `/dev/sdc` prepared as a physical volume:

```bash
sudo vgextend vg01 /dev/sdc
```

Check the updated volume group:

```bash
sudo vgdisplay vg01
```

You should see that the size of `vg01` has increased, indicating that the new physical volume has been successfully added.

## Detailed Code Examples

Here's a more detailed example of creating and managing a volume group with multiple disks:

1. **Preparing two disks:**

   ```bash
   sudo pvcreate /dev/sdb
   sudo pvcreate /dev/sdc
   ```

2. **Creating a volume group with these disks:**

   ```bash
   sudo vgcreate vg02 /dev/sdb /dev/sdc
   ```

3. **Extending the volume group later with another disk:**

   ```bash
   sudo pvcreate /dev/sdd
   sudo vgextend vg02 /dev/sdd
   ```

4. **Listing details of the volume group:**

   ```bash
   sudo vgdisplay vg02
   ```

## Conclusion

Managing local storage using LVM and volume groups in Linux is a powerful technique. It allows administrators to handle disk space more flexibly and efficiently than traditional partitioning. By mastering the ability to assign and manage physical volumes and volume groups, you can ensure optimal utilization of disk resources, facilitate easy backups, and improve system recoverability.

Remember, the key to effective LVM management lies in careful planning of volume groups and logical volumes according to the needs of your applications and data storage requirements.