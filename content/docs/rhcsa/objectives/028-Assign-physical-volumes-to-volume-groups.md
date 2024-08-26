# Tech Tutorial: Configure Local Storage - Assign Physical Volumes to Volume Groups

## Introduction

In the realm of Linux system administration, managing storage effectively is crucial for performance and data integrity. Logical Volume Management (LVM) is a widely used technique that provides a higher-level view of the disk storage on a system than the traditional view of disks and partitions. This abstraction makes it easier to extend storage, create backups, and more. In this tutorial, we will focus on a specific aspect of LVM: assigning physical volumes to volume groups.

## Prerequisites

Before proceeding with this tutorial, you should have the following:

- A Linux system with root privileges.
- At least one unallocated disk or unallocated space available.
- LVM tools installed. You can install them on most distributions with the package manager.

For example, on Ubuntu or Debian-based systems:

```bash
sudo apt-get update
sudo apt-get install lvm2
```

## Step-by-Step Guide

### Step 1: Checking Available Disks

First, identify the disks available on your system that you can use for LVM.

```bash
sudo fdisk -l
```

Look for disks with no partitions, which typically could be listed as `/dev/sdb` or `/dev/sdc`.

### Step 2: Creating Physical Volume

Once you have identified an available disk, the next step is to create a physical volume (PV). Suppose `/dev/sdb` is the disk you want to use:

```bash
sudo pvcreate /dev/sdb
```

This command initializes `/dev/sdb` as a physical volume. To verify the creation, use:

```bash
sudo pvs
```

or

```bash
sudo pvdisplay
```

### Step 3: Creating a Volume Group

Now, create a volume group (VG). A volume group is a container for one or more physical volumes. Let's create a volume group named `vgdata`:

```bash
sudo vgcreate vgdata /dev/sdb
```

This command creates a new volume group named `vgdata` and assigns the physical volume `/dev/sdb` to this group. To check the volume group, use:

```bash
sudo vgs
```

or

```bash
sudo vgdisplay
```

### Step 4: Adding More Physical Volumes

If you have another disk, say `/dev/sdc`, and you want to extend the existing volume group `vgdata`, you can add this new physical volume to the volume group:

```bash
sudo pvcreate /dev/sdc
sudo vgextend vgdata /dev/sdc
```

This sequence of commands first initializes `/dev/sdc` as a physical volume and then adds it to the `vgdata` volume group.

### Step 5: Verifying the Configuration

After adding physical volumes to a volume group, it is a good practice to verify the setup:

```bash
sudo vgdisplay vgdata
```

This command will show detailed information about `vgdata`, including the list of physical volumes that make up the volume group.

## Conclusion

In this tutorial, you learned how to assign physical volumes to volume groups using LVM on Linux. This process is fundamental for effective storage management, allowing for flexibility in how storage is allocated and used. By mastering these skills, you can ensure efficient use of disk resources, improve system performance, and maintain easier data management and backup processes.

Remember, always backup important data before making changes to disk configurations to avoid unintentional data loss.