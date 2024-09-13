# Tech Tutorial: Configure Local Storage on RHEL

## Introduction

In this tutorial, we focus on how to create and delete logical volumes in a Red Hat Enterprise Linux (RHEL) environment. Logical volumes are an essential aspect of managing storage resources in Linux, providing flexibility and ease of management that traditional partitions do not offer. This guide will be particularly useful for those preparing for the Red Hat Certified System Administrator (RHCSA) exam, as it adheres strictly to RHEL-specific commands and procedures.

Logical Volume Management (LVM) in Linux allows for the dynamic resizing of volumes and the ability to create snapshots, among other features. By the end of this tutorial, you will know how to set up and manage logical volumes on a RHEL system.

## Prerequisites

- A system running RHEL 7 or RHEL 8
- Administrative access to the system
- Basic familiarity with Linux command-line interface

## Step-by-Step Guide

### Step 1: Installing LVM Tools

Before you can start working with logical volumes, ensure that the LVM2 package is installed on your system. You can install it using the following command:

```bash
sudo yum install lvm2
```

### Step 2: Preparing Physical Volumes

A physical volume (PV) is a physical storage device that can be used in LVM. It could be an entire hard disk, a hard disk partition, or even an LVM logical volume in another VG (Volume Group). To prepare a new physical volume, use the `pvcreate` command:

```bash
sudo pvcreate /dev/sdb1
```

Replace `/dev/sdb1` with the actual device name of your storage device.

### Step 3: Creating a Volume Group

A volume group (VG) is a collection of physical volumes. The VG is where you create logical volumes. To create a new volume group named `vg01`, including the previously created physical volume, use the `vgcreate` command:

```bash
sudo vgcreate vg01 /dev/sdb1
```

### Step 4: Creating Logical Volumes

To create a logical volume, use the `lvcreate` command. The following command creates a logical volume named `lv01` in the volume group `vg01` with a size of 10GB:

```bash
sudo lvcreate -n lv01 -L 10G vg01
```

This command specifies the name of the logical volume with `-n`, the size with `-L`, and the volume group.

### Step 5: Formatting and Mounting the Logical Volume

After creating the logical volume, you can format it using a filesystem of your choice (e.g., ext4):

```bash
sudo mkfs.ext4 /dev/vg01/lv01
```

Next, create a directory to mount the logical volume:

```bash
sudo mkdir /mnt/data
```

Mount the logical volume:

```bash
sudo mount /dev/vg01/lv01 /mnt/data
```

### Step 6: Deleting Logical Volumes

To delete a logical volume, first, ensure it is unmounted:

```bash
sudo umount /mnt/data
```

Then remove the logical volume using `lvremove`:

```bash
sudo lvremove /dev/vg01/lv01
```

Confirm the deletion when prompted.

## Conclusion

This tutorial covered how to create and manage logical volumes in a RHEL environment, from installing necessary tools to creating and deleting logical volumes. Mastering these tasks is crucial for effective storage management and is an essential skill for any system administrator, especially those preparing for the RHCSA exam.

Remember that managing logical volumes allows for greater flexibility in handling storage needs and can significantly ease the management of disk space on a Linux server. Keep practicing these commands and explore further LVM features such as snapshots and resizing volumes to enhance your system administration skills.