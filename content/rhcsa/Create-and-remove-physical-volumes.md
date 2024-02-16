+++
title = "Create and remove physical volumes"
date = "2024-02-16T11:47:53-05:00"
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


# Red Hat Certified Systems Administrator Exam 200 Objective: "Create and remove physical volumes" Tutorial

## Introduction
A physical volume (PV) is a partition or a disk on a physical hard drive that is used by the Linux Logical Volume Manager (LVM). It is the first step in setting up LVM and plays a crucial role in managing storage on Red Hat Enterprise Linux systems. This tutorial will provide a step-by-step guide on how to create and remove physical volumes, which is one of the objectives for the Red Hat Certified Systems Administrator Exam (EX200).

## Prerequisites
Before we begin, make sure you have a basic understanding of Linux commands and have access to a Red Hat Enterprise Linux system. Additionally, it is recommended to have some knowledge of LVM concepts such as logical volumes and volume groups.

## Step 1: Checking existing physical volumes
First, we need to check if there are any existing physical volumes on our system. This can be done by running the `pvs` command, which will display a list of all physical volumes and their attributes, such as size and mount point.

```
$ pvs
```

If there are no existing physical volumes, the output will be blank.

## Step 2: Creating a physical volume
To create a physical volume, we first need to identify the drive or partition we want to use. This can be done by using the `fdisk -l` command, which lists all available drives and their partitions.

```
$ fdisk -l
```

Once we have identified the drive or partition, we can use the `pvcreate` command to create the physical volume.

```
$ pvcreate /dev/sdb
```

This will initialize the drive or partition as a physical volume and assign a unique identifier (PV UUID) to it.

## Step 3: Displaying the newly created physical volumes
To verify that the physical volume has been successfully created, we can use the `pvs` command again.

```
$ pvs
```

The output should now show the new physical volume along with its attributes.

## Step 4: Adding a physical volume to a volume group
The next step is to add the physical volume to a volume group (VG). A volume group is a collection of physical volumes that are managed together.

To add our new physical volume to an existing volume group, we can use the `vgextend` command.

```
$ vgextend vg0 /dev/sdb
```

This will add our new physical volume to the `vg0` volume group. If we wanted to create a new volume group with only our new physical volume, we could use the `vgcreate` command instead.

## Step 5: Displaying the volume groups
To verify that the physical volume has been added to the volume group, we can use the `vgs` command. This will display a list of all volume groups and their attributes.

```
$ vgs
```

Our new physical volume should now be listed as part of the volume group we specified.

## Step 6: Removing a physical volume
If we want to remove a physical volume from a volume group, we can use the `pvremove` command. This will remove the physical volume from the specified volume group and all the data on the physical volume will be lost.

```
$ pvremove /dev/sdb
```

## Step 7: Removing a volume group
To remove a volume group, we can use the `vgremove` command. This will remove the specified volume group and all associated logical volumes and physical volumes.

```
$ vgremove vg0
```

## Conclusion
In this tutorial, we have covered the basics of creating and removing physical volumes. This is an essential skill for any Red Hat Certified Systems Administrator, as it is a crucial step in managing storage using LVM. Now, you are ready to confidently tackle this objective in the Red Hat Certified Systems Administrator Exam (EX200). 