+++
title = "Create and delete logical volumes"
date = "2024-02-16T11:48:08-05:00"
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


Table of Contents
1. Introduction
2. Understanding Logical Volumes
3. Creating Logical Volumes
4. Managing Logical Volumes
5. Deleting Logical Volumes
6. Conclusion

1. Introduction
The Red Hat Certified Systems Administrator (RHCSA) Exam is a professional certification that validates the skills and knowledge required to perform essential tasks in Red Hat Enterprise Linux (RHEL) environments. One of the objectives of this exam is "Create and delete logical volumes". In this tutorial, we will go into great depth on this objective, explaining what logical volumes are, how to create and manage them, and how to delete them.

2. Understanding Logical Volumes
Before we dive into creating and deleting logical volumes, let's first understand what they are. Logical volumes are virtual partitions that can be created on top of physical volumes (hard drives, solid state drives, etc.) in a Linux system. They provide a flexible and efficient way of managing storage in a system, allowing administrators to easily resize, move, and add volumes as needed.

3. Creating Logical Volumes
To create a logical volume, we first need to have a physical volume available. This can be a partition, a whole disk, or a RAID device. Once we have the physical volume, we can use the "lvcreate" command to create a logical volume.

Syntax: lvcreate -n <lvol_name> -L <size> <vg_name>

- "-n" specifies the name of the logical volume
- "-L" specifies the size of the logical volume
- "<vg_name>" specifies the volume group where the logical volume will be created

Example: lvcreate -n mylv -L 50G myvg
This command will create a logical volume named "mylv" with a size of 50GB in the "myvg" volume group.

4. Managing Logical Volumes
Once a logical volume is created, we can use the "lvdisplay" command to view its details, such as size, name, volume group, and mount point. We can also use the "lvresize" command to resize a logical volume, or the "lvmove" command to move a logical volume to a different physical volume.

Syntax:
- lvdisplay <lvol_path>: displays detailed information about a specific logical volume
- lvresize -L <size> <lvol_path>: resizes a logical volume to the specified size
- lvmove <lvol_path> <new_pv>: moves a logical volume to a different physical volume

Example:
- lvdisplay /dev/myvg/mylv
- lvresize -L 100G /dev/myvg/mylv
- lvmove /dev/myvg/mylv /dev/sdb1

5. Deleting Logical Volumes
To delete a logical volume, we can use the "lvremove" command. It is important to note that deleting a logical volume will permanently delete all data stored on that volume, so it should be done with caution.

Syntax: lvremove <lvol_path>

Example: lvremove /dev/myvg/mylv

6. Conclusion
In this tutorial, we covered the "Create and delete logical volumes" objective of the Red Hat Certified Systems Administrator Exam. We discussed what logical volumes are, how to create and manage them, and how to delete them. Logical volumes are a key component in managing storage in a Linux system, and mastering this objective will contribute to a successful performance on the RHCSA Exam. 