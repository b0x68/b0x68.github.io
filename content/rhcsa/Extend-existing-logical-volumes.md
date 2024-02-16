+++
title = "Extend existing logical volumes"
date = "2024-02-16T11:49:17-05:00"
author = "root"
cover = ""
tags = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
keywords = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Red Hat Certified Systems Administrator: "Extend existing logical volumes" Exam Objective

The objective for this part of the Red Hat Certified Systems Administrator exam is to demonstrate your knowledge and skills in extending existing logical volumes in a Red Hat Enterprise Linux environment. Logical volumes are one way to manage storage in a Linux system by combining multiple physical volumes into a single abstract volume. This allows for more flexibility in managing storage space and resizing volumes as needed.

In this tutorial, we will cover the steps and commands necessary to extend an existing logical volume in a Red Hat Enterprise Linux system, including preparation, resizing, and verification.

## Prerequisites

Before attempting to extend a logical volume, it is important to make sure your system meets the following prerequisites:

- You are logged in as a user with root or sudo privileges
- The logical volume you want to extend must have free space available in its volume group
- Any data on the logical volume should be backed up in case of any issues

## Step 1: Checking Volume Group and Logical Volume Information

The first step is to gather information about the volume group and logical volume that you want to extend. This can be done using the `lvdisplay` command, which will display detailed information about all logical volumes on the system.

```
lvdisplay
```

You will get an output similar to the following:

```
--- Logical volume ---
LV Path                /dev/sys/volume1
LV Name                volume1
VG Name                sys
LV Size                10.00 GiB
Current LE             2560
Segments               1
Allocation             inherit
Read ahead sectors     auto
- currently set to     256
Block device           253:3

--- Volume group ---
VG Name                sys
System ID
Format                 lvm2
Metadata Areas         2
Metadata Sequence No  11
VG Access              read/write
VG Status              resizable
MAX LV                 0
Cur LV                 5
Open LV                5
Max PV                 0
Cur PV                 2
Act PV                 2
VG Size                127.99 GiB
PE Size                4.00 MiB
Total PE               32766
Alloc PE / Size        27366 / <106.99 GiB
Free  PE / Size        5400 / 21.00 GiB
VG UUID                abcdefgh-ijkl-mnop-1234-567890123456
```

Note the information under the "Logical volume" and "Volume group" sections. In this example, we can see that the volume group named "sys" has 21.00 GiB of free space available, while the logical volume named "volume1" has a size of 10.00 GiB and is located within the "sys" volume group.

## Step 2: Preparing the Volume Group

Before we can resize the logical volume, we need to extend the volume group to include the unallocated free space. This can be done using the `vgextend` command, followed by the volume group name and the device name of the new physical volume.

```
vgextend sys /dev/sdb
```

This will add the new physical volume to the "sys" volume group, making the additional space available for use.

## Step 3: Extending the Logical Volume

Now that the volume group has been extended, we can proceed to extend the logical volume. This is done using the `lvextend` command, followed by the name of the logical volume and the size to which you want to extend it.

```
lvextend -L +5G /dev/sys/volume1
```

In this example, we are increasing the size of the logical volume named "volume1" by 5 GB. You can also use absolute values for the size, such as "20G" for a 20 GB extension.

## Step 4: Resizing the File System

Once the logical volume has been extended, we need to make sure the file system on it is also extended to use the additional space. This can be done using the `resize2fs` command for ext4 file systems, or `xfs_growfs` for XFS file systems.

```
# For ext4 file systems
resize2fs /dev/sys/volume1

# For XFS file systems
xfs_growfs /dev/sys/volume1
```

This will resize the file system on the logical volume to match its new size, making the additional space available for use.

## Step 5: Verifying the Logical Volume Extension

To verify that the logical volume has been successfully extended, you can use the `lvdisplay` command again and compare the size to the previous output.

```
lvdisplay
```

You should see that the size of the logical volume has been increased to the value you specified in the previous step.

## Conclusion

In this tutorial, we have covered the steps and commands necessary to extend an existing logical volume in a Red Hat Enterprise Linux system. By following these steps, you should now have a better understanding of how to manage storage in your Linux environment and be prepared for the "Extend existing logical volumes" objective on the Red Hat Certified Systems Administrator exam.