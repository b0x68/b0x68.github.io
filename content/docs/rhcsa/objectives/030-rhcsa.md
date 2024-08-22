# Tech Tutorial: Configure Local Storage

## Introduction

In this tutorial, we will explore how to configure systems to mount file systems at boot using universally unique identifiers (UUIDs) or labels. This approach enhances the stability and predictability of file system handling, especially during boot. Using UUIDs or labels is particularly useful in environments where disks might be added or removed frequently, or when dealing with multiple storage devices.

## Why Use UUID or Labels?

- **Uniqueness**: Each file system's UUID is unique, which means even if you swap drives around, your system will still mount the correct drive at the specified mount point.
- **Consistency**: Labels can provide an easy-to-remember way to reference drives that makes scripts or configurations easier to read and maintain.

## Pre-requisites

- A Linux-based operating system.
- Familiarity with terminal and command-line operations.
- Basic understanding of file systems and their mounting.
- `sudo` or root access to the system.

## Step-by-Step Guide

### Step 1: Checking the Current File System Configuration

Before making any changes, it's important to check the current state of the file systems and their mount points.

1. **List all partitions along with their UUIDs and Labels:**

   ```bash
   lsblk -o NAME,FSTYPE,UUID,LABEL
   ```

2. **View the current mounts:**

   ```bash
   cat /etc/fstab
   ```

   `fstab` is the file that contains information about different file systems and how they should be mounted.

### Step 2: Identifying UUID and Labels

To use UUIDs or labels for mounting, you need to know what they are. You can find them using the `blkid` command:

```bash
sudo blkid
```

This will output something like:

```plaintext
/dev/sda1: UUID="a1b2c3d4" TYPE="ext4" PARTUUID="123456789"
/dev/sda2: LABEL="DataDrive" UUID="d4c3b2a1" TYPE="ext4" PARTUUID="987654321"
```

Note down the UUID or LABEL of the partition you wish to auto-mount.

### Step 3: Editing fstab File

To have a file system mounted on boot, you need to add it to your `/etc/fstab` file.

1. **Open `/etc/fstab` in a text editor:**

   ```bash
   sudo nano /etc/fstab
   ```

2. **Add a new line for your file system:**

   To mount using UUID:

   ```plaintext
   UUID=a1b2c3d4 /mnt/mydrive ext4 defaults 0 2
   ```

   To mount using a Label:

   ```plaintext
   LABEL=DataDrive /mnt/datadrive ext4 defaults 0 2
   ```

   Explanation of parameters:
   - `UUID=a1b2c3d4` or `LABEL=DataDrive`: Identifier
   - `/mnt/mydrive` or `/mnt/datadrive`: Mount point
   - `ext4`: File system type
   - `defaults`: Mount options
   - `0 2`: Dump and pass (used by `fsck`)

3. **Save and close the file.**

### Step 4: Testing the Configuration

After editing the `fstab` file, it's important to test that everything is set up correctly:

1. **Mount all filesystems:**

   ```bash
   sudo mount -a
   ```

2. **Check if the new mount was successful:**

   ```bash
   df -h
   ```

   Look for your mount point in the list.

## Conclusion

By following this tutorial, you should now be able to configure your Linux system to mount file systems at boot using UUIDs or labels. This method not only makes your system more robust to changes in hardware configuration but also helps in managing mounts in a more organized way.

Using UUIDs and labels can significantly reduce the risk of boot errors in systems with multiple storage devices, thereby improving overall system reliability and boot performance.