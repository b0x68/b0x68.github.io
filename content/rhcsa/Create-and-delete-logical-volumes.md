+++
title = "Create and delete logical volumes"
date = "2024-02-16T10:33:13-05:00"
author = "root"
cover = ""
tags = ["mounting", "group.", "volumes", "volume", "linux", "administration,", "group,", "`mount`"]
keywords = ["group.", "group", "volumes,", "(logical", "`mount`", "command", "volumes", "system"]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Red Hat Certified Systems Administrator Exam 200 Objective: Create and Delete Logical Volumes

In this tutorial, we will provide a step-by-step guide for the Red Hat Certified Systems Administrator (RHCSA) exam objective of creating and deleting logical volumes. Logical volumes are a way of managing hard drive space in a flexible and efficient manner. We will go into great depth on the concepts and commands needed to successfully complete this objective in the exam.

## Prerequisites

Before starting this tutorial, you should have a basic understanding of Linux server administration, including how to use the command line interface and how to manage storage devices. This tutorial assumes that you are using Red Hat Enterprise Linux (RHEL) as your operating system.

## Step 1: Understanding Logical Volumes

Logical volumes are a virtual storage system that allows you to combine multiple physical storage devices into one larger logical volume. This provides flexibility in managing storage space and enables features such as resizing and snapshotting. Logical volumes are a part of the LVM (Logical Volume Manager) toolset, which is used for managing storage devices in Linux.

## Step 2: Creating Physical Volumes

Before we can create logical volumes, we need to have physical volumes to work with. Physical volumes are the individual storage devices that will be combined to create logical volumes. These can be hard drives, solid state drives, or any other storage device. To create a physical volume, use the `pvcreate` command followed by the device name. For example:

```
pvcreate /dev/sdb
```

This will initialize the device for use with LVM. You can check the status of your physical volumes by using the `pvdisplay` command.

## Step 3: Creating Volume Groups

Next, we need to create a volume group, which is essentially a pool of physical volumes that will be used to create logical volumes. To create a volume group, use the `vgcreate` command followed by the desired name and the physical devices to include. For example:

```
vgcreate vg01 /dev/sdb /dev/sdc
```

This will create a volume group named `vg01` using the physical devices `/dev/sdb` and `/dev/sdc`. You can view the details of your volume groups by using the `vgdisplay` command.

## Step 4: Creating Logical Volumes

With our physical volumes and volume group set up, we can now create logical volumes within the volume group. To do this, we use the `lvcreate` command followed by the size and name of our logical volume, as well as the volume group to use. For example:

```
lvcreate -L 10G -n lv01 vg01
```

This will create a logical volume named `lv01` with a size of 10GB in the `vg01` volume group. You can view the details of your logical volumes by using the `lvdisplay` command.

## Step 5: Formatting and Mounting Logical Volumes

After creating logical volumes, we need to format them with a file system and mount them to be usable. To format a logical volume, we use the `mkfs` command followed by the file system type and the logical volume device path. For example:

```
mkfs.ext4 /dev/vg01/lv01
```

Once the logical volume is formatted, we can mount it to a desired location using the `mount` command. For example, to mount the logical volume `lv01` to the directory `/mnt/lv01`, we would use the following command:

```
mount /dev/vg01/lv01 /mnt/lv01
```

The logical volume will now be accessible at the mounted location and can be used for data storage.

## Step 6: Modifying Logical Volumes

One of the benefits of logical volumes is the ability to modify them as needed. This includes resizing and snapshotting. To resize a logical volume, use the `lvresize` command followed by the new size and logical volume path. For example:

```
lvresize -L 15G /dev/vg01/lv01
```

This will resize the logical volume `lv01` in the `vg01` volume group to be 15GB. Similarly, to create a snapshot of a logical volume, use the `lvcreate` command with the `--snapshot` option followed by the logical volume to be snapshotted and the snapshot name. For example:

```
lvcreate --snapshot /dev/vg01/lv01 -n s_lv01
```

## Step 7: Deleting Logical Volumes

When a logical volume is no longer needed, it can be deleted using the `lvremove` command followed by the logical volume path. For example:

```
lvremove /dev/vg01/lv01
```

This will delete the logical volume `lv01` from the `vg01` volume group. You can also use the `lvremove` command with the `-f` option to force the removal of the logical volume, even if it is currently mounted.

## Step 8: Conclusion

In this tutorial, we have explored how to create and delete logical volumes in Red Hat Enterprise Linux. We have covered the concepts of physical volumes, volume groups, and logical volumes, as well as the necessary commands to manage them. With this knowledge, you should be well-prepared to complete the Create and Delete Logical Volumes objective in the RHCSA exam. Good luck!