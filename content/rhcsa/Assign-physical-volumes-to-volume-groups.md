+++
title = "Assign physical volumes to volume groups"
date = "2024-02-16T11:48:01-05:00"
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


# Assigning Physical Volumes to Volume Groups

## Introduction
In this tutorial, we will dive deep into the objective of "Assign physical volumes to volume groups" as part of the Red Hat Certified Systems Administrator Exam. This objective covers one of the essential tasks in system administration, which is managing storage devices and organizing them into logical volumes for efficient storage management. In this tutorial, we will cover the concepts of physical volumes, volume groups, and the steps involved in assigning physical volumes to volume groups.

## Understanding Physical Volumes
A physical volume, also known as a PV, is a partition or a storage device that is used to store data in a Logical Volume Manager (LVM) environment. In other words, it is a physical storage device that can be used to create logical volumes. Some commonly used LVM physical volumes include disks, hard drives, partitions, and RAID devices. These physical volumes are necessary for creating and allocating logical volumes to store data.

## What is a Volume Group?
A volume group, also known as a VG, is a collection of one or more physical volumes that are grouped together to act as a pool of storage space. A volume group provides a logical abstraction layer that allows us to manage multiple physical volumes as a single entity. Logical volumes are created from volume groups, and they are used to store data or act as physical partitions for the operating system. In summary, volume groups act as a bridge between physical and logical volumes, allowing the storage space to be organized and managed efficiently.

## Steps to Assign Physical Volumes to Volume Groups
Now that we have a basic understanding of physical volumes and volume groups let's dive into the steps involved in assigning physical volumes to volume groups.

1. Identify available physical volumes: The first step is to identify the physical volumes that are available on the system. This can be done by using the `fdisk -l` command, which will display the list of all physical volumes connected to the system.

2. Create a new volume group: If there are no existing volume groups, we can create a new one using the `vgcreate` command. This command takes two arguments, the name of the volume group and one or more physical volumes that will be added to the group. For example, `vgcreate newvg /dev/sdb /dev/sdc` will create a new volume group named "newvg" and add physical volumes /dev/sdb and /dev/sdc to it.

3. Add physical volumes to an existing volume group: To add physical volumes to an existing volume group, we use the `vgextend` command. This command takes two arguments, the name of the volume group and one or more physical volumes that will be added to the group. For example, `vgextend existingvg /dev/sdd` will add the physical volume /dev/sdd to the existing volume group "existingvg".

4. Remove physical volumes from a volume group: If you want to remove a physical volume from a volume group, you can use the `pvmove` command. This command moves all the data from the specified physical volume to other physical volumes in the volume group, essentially removing the physical volume from the group.

## Conclusion
In this tutorial, we have covered the objective of "Assign physical volumes to volume groups" in great depth. We have learned about physical volumes and volume groups, and how they are used in managing storage devices in a logical volume manager environment. We also discussed the steps involved in assigning physical volumes to volume groups, including creating new volume groups, adding physical volumes to existing groups, and removing physical volumes from volume groups. By mastering this objective, you will be better equipped to manage storage devices in a production environment and successfully pass the Red Hat Certified Systems Administrator Exam.