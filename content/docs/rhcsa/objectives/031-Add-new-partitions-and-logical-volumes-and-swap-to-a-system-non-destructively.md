# Tech Tutorial: Configure Local Storage on RHEL

## Introduction

In this tutorial, we will explore how to manage local storage on a Red Hat Enterprise Linux (RHEL) system. Specifically, we will learn how to add new partitions and logical volumes, and configure swap space non-destructively. This skill is crucial for system administrators looking to manage storage effectively while ensuring system stability and scalability.

## Prerequisites

- A RHEL installed system (version 7 or 8)
- Root or sudo access
- Basic understanding of Linux command line interface

## Step-by-Step Guide

### Step 1: Preparing the Disk

Before adding new partitions or logical volumes, you need to identify the available disks. Use the `lsblk` command to list all block devices:

```bash
sudo lsblk
```

Look for a disk with free space or no partitions. For this tutorial, we assume `/dev/sdb` is the target disk.

### Step 2: Creating a New Partition

We will use `fdisk` to create a new primary partition on `/dev/sdb`.

1. Start `fdisk` on `/dev/sdb`:

    ```bash
    sudo fdisk /dev/sdb
    ```

2. Press `n` to create a new partition.
3. Choose `p` for primary partition.
4. Enter the partition number (e.g., `1`).
5. Specify the first and last sectors or simply press Enter to use the default, which utilizes the entire disk.
6. Press `w` to write the changes to the disk.

Verify the new partition with `lsblk`:

```bash
sudo lsblk
```

### Step 3: Creating a Physical Volume

After creating the partition, convert it into a physical volume (PV) for use in a logical volume:

```bash
sudo pvcreate /dev/sdb1
```

Verify the physical volume:

```bash
sudo pvs
```

### Step 4: Creating a Volume Group

Create a new volume group (VG) by adding the physical volume to it:

```bash
sudo vgcreate vgdata /dev/sdb1
```

Check the created volume group:

```bash
sudo vgs
```

### Step 5: Adding a Logical Volume

Now, create a logical volume (LV) within the `vgdata` volume group:

```bash
sudo lvcreate -n lvdata -L 10G vgdata
```

This command creates a logical volume named `lvdata` with a size of 10GB.

Verify the logical volume:

```bash
sudo lvs
```

### Step 6: Formatting and Mounting the Logical Volume

Format the logical volume with the ext4 filesystem:

```bash
sudo mkfs.ext4 /dev/vgdata/lvdata
```

Create a mount point and mount the logical volume:

```bash
sudo mkdir /mnt/data
sudo mount /dev/vgdata/lvdata /mnt/data
```

Ensure the mount is permanent by adding it to `/etc/fstab`:

```plaintext
/dev/vgdata/lvdata /mnt/data ext4 defaults 0 0
```

### Step 7: Configuring Swap Space

To add swap:

1. Create a swap logical volume:

    ```bash
    sudo lvcreate -n lvswap -L 2G vgdata
    ```

2. Make the logical volume a swap area:

    ```bash
    sudo mkswap /dev/vgdata/lvswap
    ```

3. Activate the swap:

    ```bash
    sudo swapon /dev/vgdata/lvswap
    ```

4. Add it to `/etc/fstab` for permanence:

    ```plaintext
    /dev/vgdata/lvswap swap swap defaults 0 0
    ```

Verify the swap is active:

```bash
sudo swapon -s
```

## Conclusion

In this tutorial, we've covered how to efficiently manage local storage on a RHEL system by creating partitions, physical volumes, volume groups, logical volumes, and configuring swap space, all without disrupting the system. These steps are essential for system administrators preparing for the RHCSA or managing RHEL systems in production environments. Remember, practice and familiarity with system tools are key to effective and efficient system administration.