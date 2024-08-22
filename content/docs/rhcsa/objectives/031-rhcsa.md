# Tech Tutorial: Configure Local Storage

## Introduction

In this tutorial, we will delve into managing local storage on a Linux system. Specifically, we will focus on adding new partitions, logical volumes, and configuring swap space non-destructively. This is crucial for systems administration and for anyone preparing for certifications that require knowledge of disk management and filesystem configuration.

## Prerequisites

Before proceeding, ensure you have:
- A Linux system (CentOS, Ubuntu, Fedora, etc.)
- Sufficient unpartitioned disk space
- Root or sudo privileges
- Basic familiarity with the command line

## Tools and Concepts

- **fdisk/gdisk**: Command-line utilities for disk partitioning.
- **Logical Volume Manager (LVM)**: Flexible storage management solution.
- **mkswap/swapon**: Utilities to manage swap space.

## Step-by-Step Guide

### Step 1: Checking the Current Disk Layout

First, let’s identify the available disks and their current partitioning.

```bash
lsblk
```

This command lists all block devices and their mount points if applicable. Look for devices without mount points or partitions as candidates for partitioning.

### Step 2: Partitioning the Disk

Assuming `/dev/sdb` is the target disk:

1. **Using fdisk for MBR partitioning:**

```bash
sudo fdisk /dev/sdb
```

- Press `n` to create a new partition.
- Press `p` for primary partition.
- Choose the partition number (1-4).
- Specify the start and end sectors.
- Press `w` to write the changes.

2. **Using gdisk for GPT partitioning:**

```bash
sudo gdisk /dev/sdb
```

- Press `n` to create a new partition.
- Choose the partition number.
- Specify the start and end sectors or sizes (e.g., +20G for a 20 GB partition).
- Press `w` to write the changes.

### Step 3: Creating the Filesystem

Create a filesystem on the new partition:

```bash
sudo mkfs.ext4 /dev/sdb1
```

### Step 4: Setting Up Logical Volumes

1. **Creating Physical Volume:**

```bash
sudo pvcreate /dev/sdb1
```

2. **Creating Volume Group:**

```bash
sudo vgcreate vg1 /dev/sdb1
```

3. **Creating Logical Volume:**

```bash
sudo lvcreate -n lv1 -L 10G vg1
```

4. **Creating Filesystem on Logical Volume:**

```bash
sudo mkfs.ext4 /dev/vg1/lv1
```

### Step 5: Mounting the Filesystem

Mount the new filesystem:

```bash
sudo mkdir /mnt/new_partition
sudo mount /dev/vg1/lv1 /mnt/new_partition
```

Verify the mount:

```bash
df -h /mnt/new_partition
```

### Step 6: Configuring Swap Space

1. **Creating Swap on a new partition:**

Assume `/dev/sdb2` is intended for swap.

```bash
sudo mkswap /dev/sdb2
sudo swapon /dev/sdb2
```

2. **Ensure the swap is permanent:**

Add the following line to `/etc/fstab`:

```plaintext
/dev/sdb2 none swap sw 0 0
```

Verify the swap:

```bash
sudo swapon -s
```

## Conclusion

You have successfully learned how to add new partitions and logical volumes, and configure swap space without disrupting the existing system setup. These skills are essential for effective systems management, allowing for flexible and efficient storage management.

Remember, always back up important data before making changes to disk configurations and test configurations in a safe environment when possible.