# Tech Tutorial: Configure Local Storage

## Introduction

In the realm of system administration, managing local storage is a fundamental skill. This tutorial focuses on creating and removing physical volumes, which are critical steps in managing disk storage using the Linux Logical Volume Manager (LVM). LVM is a widely used technique in Linux environments to manage disk space flexibly.

In this tutorial, we will cover the basics of physical volumes, including their creation and deletion. We will use real-world scenarios and examples to illustrate these actions, ensuring that you can apply these skills in practical settings.

## Prerequisites

Before proceeding, ensure you have the following:
- A Linux system with administrative access.
- At least one additional storage device or disk partition available for experiments.
- The `lvm2` package installed. You can install it using `sudo apt-get install lvm2` on Debian-based systems or `sudo yum install lvm2` on RPM-based systems.

## Step-by-Step Guide

### Step 1: Checking Available Disks

Before creating a physical volume, it's important to identify the available disks or partitions. Use the `lsblk` command to list all block devices along with their mount points and sizes.

```bash
lsblk
```

Look for devices that do not have a mount point, as these are available for creating new physical volumes.

### Step 2: Creating a Physical Volume

Once you have identified a suitable disk or partition (let’s say `/dev/sdb`), you can convert it into a physical volume. Ensure that the device is not currently mounted or in use.

```bash
sudo pvcreate /dev/sdb
```

This command initializes `/dev/sdb` as a physical volume. After execution, you can use the `pvs` command to display a summary of physical volumes:

```bash
pvs
```

### Step 3: Verifying the Physical Volume

To verify that your physical volume was successfully created and to see details about it, use the `pvdisplay` command:

```bash
sudo pvdisplay /dev/sdb
```

This will show detailed information about the physical volume like its size, UUID, and more.

### Step 4: Removing a Physical Volume

If you need to remove a physical volume (be sure that it is no longer required and not part of any volume group), use the `pvremove` command. First, ensure the physical volume is not in use:

```bash
sudo pvremove /dev/sdb
```

This command will delete the physical volume on `/dev/sdb`. You can verify it's removed by running `pvs` again and ensuring it no longer appears in the list.

## Detailed Code Examples

Let’s consider a scenario where you have a new disk `/dev/sdc` and you need to configure it as a physical volume:

1. **List all current physical volumes and identify the new disk:**

    ```bash
    lsblk
    ```

2. **Initialize `/dev/sdc` as a physical volume:**

    ```bash
    sudo pvcreate /dev/sdc
    ```

3. **Check the details of the new physical volume:**

    ```bash
    sudo pvdisplay /dev/sdc
    ```

4. **If needed, remove the physical volume `/dev/sdc`:**

    ```bash
    sudo pvremove /dev/sdc
    ```

## Conclusion

This tutorial provided a step-by-step guide on how to create and remove physical volumes in a Linux environment using LVM. Understanding these procedures is crucial for efficient disk space management and data organization on servers or workstations. Always ensure that data is backed up before manipulating disk partitions or volumes to avoid accidental data loss. With these skills, you can now confidently manage physical volumes in your Linux systems.