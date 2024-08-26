# Tech Tutorial: Configure Local Storage

## Introduction

In this tutorial, we will explore how to add new partitions, logical volumes, and swap space to a system non-destructively. This skill is crucial for systems administrators who need to manage storage resources effectively without impacting system uptime or data integrity.

We will use Linux as our operating system for this tutorial, leveraging tools such as `fdisk`, `parted`, `LVM` (Logical Volume Manager), and `mkswap`.

## Prerequisites

- A Linux system with root privileges.
- A hard drive or a partition with unallocated space.

## Step-by-Step Guide

### Step 1: Check Current Disk Layout

First, check the current disk layout. This will help us understand the available disks and partitions.

```bash
lsblk
```

### Step 2: Create a New Partition

Assuming `/dev/sdb` is the disk with available space, we will create a new partition.

1. **Launch `fdisk`**:

    ```bash
    sudo fdisk /dev/sdb
    ```

2. **Create a new partition**:
    - Type `n` for a new partition.
    - Choose `p` for primary.
    - Enter partition number (e.g., `3`).
    - Specify the start and end sectors or accept defaults.

3. **Write the changes**:
    - Type `w` to write the changes to the disk.

4. **Verify the new partition**:

    ```bash
    sudo fdisk -l /dev/sdb
    ```

### Step 3: Creating a Physical Volume

Now create a Physical Volume on the new partition.

```bash
sudo pvcreate /dev/sdb3
```

### Step 4: Creating a Volume Group

Create or extend an existing Volume Group.

1. **Create a new Volume Group** (if one does not exist):

    ```bash
    sudo vgcreate vg01 /dev/sdb3
    ```

2. **Extend an existing Volume Group**:

    ```bash
    sudo vgextend vg01 /dev/sdb3
    ```

### Step 5: Adding Logical Volumes

Create a new Logical Volume within the Volume Group.

```bash
sudo lvcreate -L 10G -n lv01 vg01
```

### Step 6: Formatting and Mounting the Logical Volume

1. **Format the logical volume**:

    ```bash
    sudo mkfs.ext4 /dev/vg01/lv01
    ```

2. **Create a mount point and mount the volume**:

    ```bash
    sudo mkdir /mnt/data
    sudo mount /dev/vg01/lv01 /mnt/data
    ```

3. **Automatically mount at boot**:
    - Edit `/etc/fstab` and add the following line:

    ```
    /dev/vg01/lv01 /mnt/data ext4 defaults 0 2
    ```

### Step 7: Adding Swap Space

1. **Create the swap space**:

    ```bash
    sudo mkswap /dev/vg01/lv01
    ```

2. **Enable the swap space**:

    ```bash
    sudo swapon /dev/vg01/lv01
    ```

3. **Make the swap permanent**:
    - Edit `/etc/fstab` and add:

    ```
    /dev/vg01/lv01 swap swap defaults 0 0
    ```

## Conclusion

This tutorial covered the essentials of adding new partitions, logical volumes, and configuring swap space in a non-destructive manner. By following the steps outlined, you can effectively manage storage on a Linux system, ensuring optimal utilization and performance.

Remember, while these steps provide a general guideline, different environments and requirements might necessitate adjustments or additional considerations. Always backup critical data before making significant changes to the disk configuration.