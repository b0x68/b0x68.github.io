# Tech Tutorial: Configure Local Storage

## Introduction

In this tutorial, we will focus on configuring local storage in a Red Hat Enterprise Linux (RHEL) environment, specifically targeting the RHCSA exam objective of assigning physical volumes to volume groups. Understanding how to manage physical volumes and volume groups is crucial for effective storage management and data organization in Linux systems.

Physical volumes (PV) are the building blocks for storage devices in Linux, and volume groups (VG) are pooled entities of one or more physical volumes. This configuration allows for greater flexibility in managing storage space.

## Prerequisites

- A system running RHEL 8 or later.
- Root privileges or access via the `sudo` command.
- At least one unused storage device to practice creating physical volumes and volume groups.

## Step-by-Step Guide

### Step 1: Identifying Available Storage Devices

Before creating physical volumes, it's essential to identify the storage devices available on your system. You can use the `lsblk` command to list all block devices along with their mount points if any.

```bash
lsblk
```

Output might look something like this:

```plaintext
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda      8:0    0   20G  0 disk 
├─sda1   8:1    0    1G  0 part /boot
└─sda2   8:2    0   19G  0 part 
sdb      8:16   0  100G  0 disk 
```

In this example, `sdb` is the unused disk that we'll use to create our physical volume.

### Step 2: Creating a Physical Volume

To create a physical volume, we use the `pvcreate` command. Ensure the selected device is not already in use or contains important data, as this process will prepare it for LVM usage, potentially erasing existing data.

```bash
sudo pvcreate /dev/sdb
```

You should see an output like this:

```plaintext
Physical volume "/dev/sdb" successfully created.
```

### Step 3: Creating a Volume Group

Once the physical volume is ready, the next step is to create a volume group. You can create a volume group using the `vgcreate` command. Here, we will name our volume group `vg01`.

```bash
sudo vgcreate vg01 /dev/sdb
```

Output:

```plaintext
Volume group "vg01" successfully created
```

### Step 4: Verifying the Volume Group

To verify that your volume group has been created and includes the correct physical volumes, use the `vgdisplay` command.

```bash
sudo vgdisplay vg01
```

This command provides detailed information about the volume group, including its size, extents, and physical volumes included.

### Detailed Code Examples

#### Adding More Physical Volumes to an Existing Volume Group

If you later add another disk to the system and want to extend the existing volume group, you can create a PV on the new disk and extend the volume group.

```bash
sudo pvcreate /dev/sdc
sudo vgextend vg01 /dev/sdc
```

#### Displaying Physical Volumes

To see details about the physical volumes, use:

```bash
sudo pvdisplay
```

This command shows information about each physical volume, such as its size, the volume group it belongs to, and allocation information.

## Conclusion

In this tutorial, you have learned how to configure local storage by assigning physical volumes to volume groups in a RHEL environment. This knowledge is essential for the RHCSA exam and practical for managing storage in professional settings. By mastering these steps, you can efficiently manage disk space, ensuring data is organized and utilized effectively. Stay tuned for more tutorials that delve deeper into other aspects of storage management.