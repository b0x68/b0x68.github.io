+++
title = "Extend existing logical volumes"
date = "2024-02-16T10:34:25-05:00"
author = "root"
cover = ""
tags = ["process", "sysadmin.", "file", "systems,", "logical", "volume>", "system.", "partitions"]
keywords = ["system", "volume.", "logical", "file", "partitions,", "group", "disk", "volumes,"]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Tutorial: Extending Existing Logical Volumes on Red Hat Certified Systems Administrator Exam 200

In this tutorial, we will be discussing the objective "Extend existing logical volumes" on the Red Hat Certified Systems Administrator Exam 200 in great depth. Logical volumes are a very important aspect of managing storage in a Red Hat Enterprise Linux environment, and being able to extend them is a crucial skill for any sysadmin. We will cover the steps involved in extending logical volumes, as well as some additional tips and best practices.

## Prerequisites

To follow along with this tutorial, you will need the following:

- A Red Hat Enterprise Linux system with LVM (Logical Volume Manager) installed
- Basic knowledge of Linux command line and some familiarity with LVM terminologies
- Sufficient disk space available to create and extend logical volumes

## Understanding Logical Volumes

Logical volumes (LVs) are virtual partitions created from physical volumes (PVs) using LVM. They are similar to traditional partitions, but with additional flexibility and features. Logical volumes can be dynamically resized, striped across multiple physical volumes for improved performance, and snapshots can be taken for data backups. Before we can extend logical volumes, it is important to have a basic understanding of how they work.

Logical volumes are organized into volume groups (VGs), which are composed of one or more physical volumes. These physical volumes can be hard drives, partitions, or other storage devices. VGs allow us to create logical volumes that span multiple physical volumes, enabling us to easily extend a logical volume by adding more physical volumes.

## Steps to Extend Logical Volumes

Now, let's go through the steps involved in extending existing logical volumes.

### 1. Check Existing Logical Volumes and Space Availability

The first step is to check the current status of logical volumes and the available space on the volume group. This will help us determine if there is enough space to extend the logical volume.

To view the existing logical volumes, use the `lvs` command. It will display a list of all the logical volumes, their size, and the volume group they belong to.

```
$ lvs 
```

To view the available space on the volume group, use the `vgs` command. This will show the total size of the volume group, the used and free space, and the number of physical volumes.

```
$ vgs 
```

### 2. Add Physical Volume to the Volume Group

If there is not enough free space in the volume group, we need to add a physical volume to it. This can be done by using the `pvcreate` command on the new physical volume. Let's assume we have added a new hard drive /dev/sdb and want to add it to the volume group vg01. The command will be as follows:

```
$ pvcreate /dev/sdb 
```

### 3. Extend the Volume Group

Once the physical volume has been added, we need to extend the volume group to include the new physical volume. This can be done by using the `vgextend` command. The syntax is as follows:

```
$ vgextend <volume group name> <physical volume>
```

In our example, the command will be:

```
$ vgextend vg01 /dev/sdb
```

### 4. Extend the Logical Volume

After extending the volume group, we can now extend the logical volume. This can be done by using the `lvextend` command. The syntax is as follows:

```
$ lvextend -L <size><unit> <logical volume>
```

The size can be specified in units such as 'G' for gigabytes, 'M' for megabytes, 'T' for terabytes, etc. Let's say we want to extend the logical volume 'lv01' by 2GB. The command will be:

```
$ lvextend -L +2G /dev/vg01/lv01 
```

Note the use of the '+' sign, which indicates that the size specified will be added to the current size of the logical volume.

### 5. Resize the File System

After extending the logical volume, we need to resize the file system so that it can make use of the newly added space. This can be done by using the appropriate command for the file system type. For example, if the file system is ext4, the command will be:

```
$ resize2fs /dev/vg01/lv01 
```

### 6. Verify the Extension

Finally, we can use the `lvdisplay` command to verify that the logical volume has been extended to the desired size.

```
$ lvdisplay /dev/vg01/lv01 
```

## Additional Tips and Best Practices

- To avoid manual resizing of file systems, it is recommended to use a Logical Volume Manager (LVM) aware file system like XFS or ext4.
- Be careful when extending logical volumes that contain active data, as any interruptions or errors during the process can result in data loss.
- vgs and lvs commands have the `--units` option, which can be used to specify the output in different units.
- It is a good practice to regularly monitor the storage usage and extend logical volumes if needed to avoid running out of disk space.

## Conclusion

In this tutorial, we have covered the steps involved in extending existing logical volumes on a Red Hat Enterprise Linux system. We have also discussed some best practices and additional tips to ensure a successful extension. Being able to extend logical volumes is an essential skill for any sysadmin, and mastering it will not only help you pass the Red Hat Certified Systems Administrator Exam 200 but also make you a more efficient and capable administrator.