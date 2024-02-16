+++
title = "Create and remove physical volumes"
date = "2024-02-16T10:32:53-05:00"
author = "root"
cover = ""
tags = ["disks/partitions", "system", "group", "partition", "partition,", "group.", "user", "systems"]
keywords = ["group.", "group", "systems", "volume.", "commands.", "partition,", "`fdisk`", "logical"]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Tutorial: Creating and Removing Physical Volumes in Red Hat Certified Systems Administrator Exam

In this tutorial, we will go through the process of creating and removing physical volumes in Red Hat Certified Systems Administrator Exam 200 Objective. As a Red Hat Certified Systems Administrator, it is essential to have a thorough understanding of creating and managing physical volumes to effectively utilize the storage space available on your system.

## Prerequisites

- A Red Hat Enterprise Linux (RHEL) system
- Basic knowledge of Linux commands and disk management
- Root access or a user with sudo privileges

## What are Physical Volumes?

Physical volumes (PVs) are essentially block devices, such as hard drives or solid-state drives, that are designated as storage space for Logical Volumes (LVs) in the Red Hat Logical Volume Manager (LVM). PVs can be combined to form a Volume Group (VG), which then serves as a storage pool for creating and managing LVs.

## Step 1: Checking Existing Physical Volumes

Before creating new physical volumes, it is essential to check the existing ones on your system to get an overview of the storage space available. To do this, use the `pvdisplay` command, which will provide details about all the physical volumes currently in use on your system.

```bash
[root@server ~]# pvdisplay
```

## Step 2: Creating a Physical Volume

To create a new physical volume, you will first need to have an unpartitioned disk or partition available. You can check this using `fdisk` or `lsblk` commands.

Once you have identified the unpartitioned disk or partition, you can use the `pvcreate` command to initialize it as a physical volume.

```bash
[root@server ~]# pvcreate /dev/sdb
```

This command will create a physical volume named `/dev/sdb`, which is now available for use in a VG.

You can also create multiple physical volumes at once by passing in the names of the disks/partitions separated by spaces.

```bash
[root@server ~]# pvcreate /dev/sdb /dev/sdc /dev/sdd
```

## Step 3: Adding Physical Volumes to a Volume Group

To make use of the newly created physical volumes, you will need to add them to a Volume Group. A Volume Group serves as a virtual pool of storage space that can span across multiple physical volumes.

To add physical volumes to an existing Volume Group, use the `vgextend` command followed by the name of the Volume Group and the name(s) of the physical volumes to be added.

```bash
[root@server ~]# vgextend vg_sys /dev/sdb /dev/sdc
```

This command will add the physical volumes `/dev/sdb` and `/dev/sdc` to the Volume Group named `vg_sys`.

## Step 4: Removing Physical Volumes from Volume Group

If you need to remove a physical volume from a Volume Group, you can use the `vgreduce` command followed by the name of the Volume Group and the name(s) of the physical volumes to be removed.

```bash
[root@server ~]# vgreduce vg_sys /dev/sdc
```

This command will remove the physical volume `/dev/sdc` from the Volume Group named `vg_sys`.

## Step 5: Deleting Physical Volumes

If you no longer need a physical volume, you can delete it using the `pvremove` command followed by the name of the physical volume.

```bash
[root@server ~]# pvremove /dev/sdb
```

This command will remove all LVM structures from the physical volume `/dev/sdb` and render it back to its original partition condition.

**Note:** Deleting a physical volume will permanently remove all data stored on it, so use this command with caution.

## Conclusion

Congratulations! You have now learned how to create, add, remove, and delete physical volumes in Red Hat Certified Systems Administrator Exam 200 Objective. This skill is essential for effectively managing storage space on your system, and practicing these steps will prepare you for the exam and real-world scenarios. Remember to handle all LVM commands with care, as they deal with critical system components.