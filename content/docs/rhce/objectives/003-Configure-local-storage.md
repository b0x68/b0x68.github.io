# Tech Tutorial: Configure Local Storage as a Red Hat Certified System Administrator

## Introduction

In this tutorial, we will delve into the essential skills required for configuring local storage on a system, a critical competency for the Red Hat Certified System Administrator (RHCSA). Managing storage effectively is foundational for ensuring that applications and services run smoothly, making it a vital area of knowledge.

We'll cover different aspects of local storage configuration, including creating and managing physical storage, creating file systems, mounting file systems, and ensuring persistent mounting through the system's file table (`/etc/fstab`).

## Step-by-Step Guide

### Prerequisites

- A Red Hat Enterprise Linux 8 installed system.
- Root privileges or access via the `sudo` command.

### 1. Understanding and Listing Block Devices

Before you configure any storage, identify the block devices attached to your system using the `lsblk` command.

```bash
lsblk
```

You should see output similar to this:

```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda      8:0    0   10G  0 disk 
├─sda1   8:1    0    1G  0 part /boot
└─sda2   8:2    0    9G  0 part 
  ├─cl-root 253:0 0  7G  0 lvm  /
  └─cl-swap 253:1 0  2G  0 lvm  [SWAP]
```

### 2. Creating Physical Volumes

Physical volumes are used in LVM (Logical Volume Management) to abstract the management of the disk devices. To create a physical volume, use the `pvcreate` command.

Suppose `/dev/sdb` is a new, unformatted disk:

```bash
sudo pvcreate /dev/sdb
```

Verify it with:

```bash
sudo pvs
```

### 3. Creating Volume Groups

Volume groups are made up of physical volumes. Create a volume group named `vgdata`:

```bash
sudo vgcreate vgdata /dev/sdb
```

Check your volume group:

```bash
sudo vgs
```

### 4. Creating Logical Volumes

Create a logical volume of size 5G named `lvdata` within `vgdata`:

```bash
sudo lvcreate -n lvdata -L 5G vgdata
```

Verify creation:

```bash
sudo lvs
```

### 5. Creating File Systems

You can create different types of file systems. Here, we'll make an ext4 file system on the `lvdata` logical volume.

```bash
sudo mkfs.ext4 /dev/vgdata/lvdata
```

### 6. Mounting File Systems

To use the newly created file system, you need to mount it:

```bash
sudo mkdir /mnt/data
sudo mount /dev/vgdata/lvdata /mnt/data
```

Check the mounted file system:

```bash
df -hT
```

### 7. Persistent Mounting using `/etc/fstab`

To ensure the file system is mounted automatically at boot, add it to `/etc/fstab`:

```bash
echo '/dev/vgdata/lvdata /mnt/data ext4 defaults 0 2' | sudo tee -a /etc/fstab
```

## Conclusion

You have now learned how to configure local storage on a Red Hat system, covering everything from physical volume creation to ensuring persistent mounts through `fstab`. These steps are crucial for managing system storage resources efficiently and are integral skills for a Red Hat Certified System Administrator.

By mastering these tasks, you ensure that your systems are set up with robust and flexible storage solutions, ready to meet the demands of different applications and services. Keep practicing these skills to deepen your understanding and enhance your system administration proficiency.