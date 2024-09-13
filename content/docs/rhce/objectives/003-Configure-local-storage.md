# Tech Tutorial: Configuring Local Storage on Red Hat Enterprise Linux

## Introduction

In this tutorial, we are focusing on one of the critical objectives for the Red Hat Certified System Administrator (RHCSA) exam: configuring local storage. The ability to manage storage devices effectively is a fundamental skill for system administrators. We will cover how to list, create, and delete partitions on both MBR and GPT disks, create and manage logical volumes, and configure systems to mount file systems at or during boot.

## Step-by-Step Guide

### Prerequisites

- A running Red Hat Enterprise Linux 8 system.
- Sufficient permissions (typically root) to perform system configurations.
- A spare storage device or virtual disk to practice on.

### 1. List Existing Storage Devices

Before making any changes, it's essential to understand the current storage setup. The `lsblk` command lists all block devices in a tree-like format.

```bash
lsblk
```

### 2. Partitioning Disks

#### MBR vs. GPT Disks

- **MBR (Master Boot Record)**: Supports up to 2TB disks and up to four primary partitions.
- **GPT (GUID Partition Table)**: Supports larger disks and up to 128 primary partitions.

#### Using `fdisk` for MBR

`fdisk` is a common utility for partitioning MBR disks.

```bash
# Start fdisk on /dev/sdx (replace 'x' with your device letter)
sudo fdisk /dev/sdx
```

Within `fdisk`, you can use:
- `m` to display the menu of commands.
- `n` to create a new partition.
- `d` to delete a partition.
- `w` to write changes to disk.

#### Using `gdisk` for GPT

`gdisk` functions similarly to `fdisk` but is used for GPT disks.

```bash
# Start gdisk on /dev/sdx
sudo gdisk /dev/sdx
```

Commands in `gdisk` are similar to `fdisk`.

### 3. Creating File Systems

After partitioning the disk, the next step is creating a file system.

#### Common File Systems

- **ext4**: `mkfs.ext4`
- **xfs**: `mkfs.xfs`

```bash
# Create an ext4 file system on partition /dev/sdx1
sudo mkfs.ext4 /dev/sdx1

# Create an xfs file system on partition /dev/sdx2
sudo mkfs.xfs /dev/sdx2
```

### 4. Mounting File Systems

To use the file systems, they must be mounted.

```bash
# Create a mount point
sudo mkdir /mnt/data

# Mount the file system
sudo mount /dev/sdx1 /mnt/data
```

#### Automating Mounts with `/etc/fstab`

To ensure the file system is mounted on boot, add an entry to `/etc/fstab`.

```bash
# Example /etc/fstab entry
/dev/sdx1    /mnt/data    ext4    defaults    0    2
```

### 5. Managing Logical Volumes (LVM)

LVM allows for flexible volume management.

#### Creating Physical Volume

```bash
sudo pvcreate /dev/sdx1
```

#### Creating Volume Group

```bash
sudo vgcreate vgdata /dev/sdx1
```

#### Creating Logical Volume

```bash
sudo lvcreate -n lvdata -L 10G vgdata
```

#### Creating File System on Logical Volume

```bash
sudo mkfs.ext4 /dev/vgdata/lvdata
```

#### Mounting Logical Volume

```bash
sudo mkdir /mnt/lvdata
sudo mount /dev/vgdata/lvdata /mnt/lvdata
```

## Conclusion

Understanding and managing local storage is crucial for system administrators. This tutorial covered the basics of disk partitioning, file system creation, and logical volume management on Red Hat Enterprise Linux. For the RHCSA exam, ensure you practice these tasks until you are comfortable with both the commands and concepts. Remember, hands-on experience is invaluable when preparing for Red Hat certifications.