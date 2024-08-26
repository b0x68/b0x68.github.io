# Tech Tutorial: Configure Local Storage

## Introduction

In Linux systems, configuring local storage correctly is crucial for system stability and performance. One of the best practices when setting up storage is to configure systems to mount file systems at boot using UUID (Universally Unique Identifier) or labels. This method is preferred because it provides a unique reference to a storage device, unlike device names like `/dev/sda1` which can change depending on the hardware configuration order.

This tutorial will guide you through the process of configuring your system to mount file systems using UUIDs and labels, ensuring your mounts are reliable and resilient to changes in the hardware setup.

## Prerequisites

- A Linux operating system (any modern distribution will suffice).
- Basic familiarity with terminal and command-line operations.
- Root or sudo access to perform administrative tasks.

## Step-by-Step Guide

### Step 1: Identifying the UUID or Label of Your Storage Device

Before you can configure the system to mount by UUID or label, you must first determine the UUID or label of the file system.

1. **List UUIDs and Labels**

   Open your terminal and type the following command to display the UUIDs and labels for all connected storage devices:

   ```bash
   lsblk -f
   ```

   This command will output a table similar to:

   ```
   NAME   FSTYPE LABEL UUID                                   MOUNTPOINT
   sda
   ├─sda1 ext4         1E0423FA056B8C30                       /
   ├─sda2 ext4   Data  3B9F58219F5779D2                       /data
   └─sda3 swap         3f6fae6e-07f8-413e-bf9f-67c4f641a5c7   [SWAP]
   ```

   - `FSTYPE` indicates the type of the file system.
   - `LABEL` is the label of the partition if it is set.
   - `UUID` is the universally unique identifier for the partition.
   - `MOUNTPOINT` shows where the partition is currently mounted.

2. **Finding specific details** 

   If you need more detailed information about a specific partition, use the `blkid` command:

   ```bash
   sudo blkid /dev/sda1
   ```

   This will output something like:

   ```
   /dev/sda1: UUID="1E0423FA056B8C30" TYPE="ext4"
   ```

### Step 2: Editing the `/etc/fstab` File

The file `/etc/fstab` contains information about where and how the partitions should be mounted. To ensure your partitions mount by UUID or label, you will need to edit this file.

1. **Open `/etc/fstab` in a text editor**:

   ```bash
   sudo nano /etc/fstab
   ```

2. **Add or modify a line for your partition**:

   To mount by UUID, format your entry like this:

   ```
   UUID=1E0423FA056B8C30 /               ext4    errors=remount-ro 0       1
   ```

   To mount by label, use:

   ```
   LABEL=Data /data               ext4    defaults        0       2
   ```

   - The first column specifies the UUID or label.
   - The second column is the mount point.
   - The third column is the file system type.
   - The fourth column contains the mount options.
   - The fifth and sixth columns are used by the `dump` and `fsck` utilities respectively.

3. **Save and close the file**.

### Step 3: Testing the Configuration

After configuring `/etc/fstab`, it's important to test the configuration to ensure there are no errors, which could prevent the system from booting correctly.

1. **Test the mount configuration**:

   ```bash
   sudo mount -a
   ```

   This command will attempt to mount all filesystems mentioned in `/etc/fstab`. If there are no errors, the command will complete silently.

2. **Check for errors**:

   If there are issues, you will see error messages in the terminal. Address these based on the information provided in the error messages.

## Conclusion

Using UUIDs or labels for mounting file systems in your Linux setup enhances the robustness of the system configuration. It helps avoid issues related to device name changes that can occur with hardware modifications. By following the steps outlined in this tutorial, you should now be able to configure your system to mount file systems more reliably at boot time.

Remember, always backup your `/etc/fstab` file before making changes to avoid system boot issues. Happy configuring!