+++
title = "Assign physical volumes to volume groups"
date = "2024-02-16T10:33:01-05:00"
author = "root"
cover = ""
tags = ["group!", "command", "logical", "partitions", "groups.", "system", "volumes**:", "groups**:"]
keywords = ["command", "linux.", "**logical", "volumes,", "volume", "**volume", "volumes**:", "(logical"]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Red Hat Certified Systems Administrator Exam 200 Objective: Assign Physical Volumes to Volume Groups Tutorial

Welcome to this tutorial on how to assign physical volumes to volume groups in Red Hat Linux. This is an important objective from the Red Hat Certified Systems Administrator Exam 200 and this tutorial will provide a detailed overview on how to accomplish this task.

## Pre-requisites
Before we begin, there are a few pre-requisites that you should be aware of:
- Basic understanding of Red Hat Linux operating system
- Familiarity with command line interface
- Administrative privileges on the system

## Understanding LVM (Logical Volume Management)
Logical Volume Management or LVM is a method for managing storage in a Linux system. It allows for easy management and allocation of storage space by separating logical storage space from physical storage devices. LVM consists of three main components: physical volumes, volume groups, and logical volumes.

- **Physical Volumes**: These are the physical storage devices such as hard drives or solid state drives that are used to store data.
- **Volume Groups**: Volume groups are created by combining one or more physical volumes together. They act as a container for logical volumes.
- **Logical Volumes**: These are virtual partitions created within volume groups and are used to store data just like physical partitions.

## Assigning Physical Volumes to Volume Groups
Now, let's dive into the steps for assigning physical volumes to volume groups. The steps below assume that you have already created a physical volume and a volume group, if not please refer to Red Hat documentation for instructions on how to do so.

### Step 1: Identify the Physical Volumes
The first step is to identify the physical volumes that you want to assign to a volume group. You can use the `fdisk -l` command to view a list of physical volumes on your system.

### Step 2: Prepare the Physical Volumes
Before you can add physical volumes to a volume group, you must first prepare them. This can be done by using the `pvcreate` command followed by the name of the physical volume. For example: `pvcreate /dev/sdc`

### Step 3: Verify the Physical Volumes
Use the `pvdisplay` command to verify that the physical volumes have been prepared.

### Step 4: Add Physical Volumes to Volume Groups
Once the physical volumes are prepared, you can add them to a volume group using the `vgextend` command followed by the volume group name and the physical volume name. For example: `vgextend vg1 /dev/sdc`

### Step 5: Verify the Volume Group
Use the `vgdisplay` command to verify that the volume group now includes the new physical volumes.

Congratulations, you have successfully assigned physical volumes to a volume group!

## Conclusion
In this tutorial, we went through the steps of assigning physical volumes to volume groups in Red Hat Linux. This is an important skill for any Red Hat Certified Systems Administrator and it is essential to have a good understanding of LVM and its components. We hope this tutorial helped you understand this objective in depth and will help you in your journey towards becoming a Red Hat Certified Systems Administrator. Happy learning!