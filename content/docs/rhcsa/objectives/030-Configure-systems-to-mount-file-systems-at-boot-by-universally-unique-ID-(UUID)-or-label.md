# Tech Tutorial: Configure Local Storage

## Introduction

In this tutorial, designed specifically for candidates preparing for the Red Hat Certified System Administrator (RHCSA) exam, we will cover an important aspect of system administration: configuring systems to mount file systems at boot by universally unique ID (UUID) or label. Understanding how to reliably mount file systems is crucial for maintaining the consistency and stability of Linux systems, particularly across reboots and hardware changes.

## Why Mount by UUID or Label?

When Linux boots, it needs to know where to find the file systems to mount them to the directory tree. Traditionally, file systems were mounted using device names like `/dev/sda1`. However, these device names can change due to hardware changes, reboots, or system configurations, leading to failures during boot.

Mounting by UUID or label provides a stable referencing system because:
- **UUIDs** are unique identifiers assigned to each filesystem at creation and do not change.
- **Labels** can be assigned by the user to provide a human-readable identifier.

Both methods ensure that the specific file system is mounted correctly regardless of changes in device paths.

## Step-by-Step Guide

### Prerequisites

- A Red Hat Enterprise Linux system
- Root or sudo privileges
- Basic familiarity with terminal commands and text editors like `vi` or `nano`

### Step 1: Identifying the File System

First, you need to identify the UUID or the label of the file system you intend to mount.

#### Finding the UUID

To find the UUID of your disk partitions, use the `blkid` command:

```bash
sudo blkid
```

This command will list all partitions along with their UUIDs and other information like TYPE and LABEL if they are set.

**Example Output:**

```plaintext
/dev/sda1: UUID="a1b2c3d4-e5f6-g7h8-i9j0-k11l12m13n14" TYPE="ext4"
/dev/sda2: UUID="b2c3d4e5-f6g7-h8i9-j0k1-l2m3n4o5p6q7" TYPE="xfs"
```

#### Setting or Finding the Label

If you want to use a label, you can set or check it using the `e2label` command for ext filesystems:

```bash
sudo e2label /dev/sda1
sudo e2label /dev/sda1 "NewLabel"
```

For XFS filesystems, use `xfs_admin`:

```bash
sudo xfs_admin -l /dev/sda2
sudo xfs_admin -L "NewLabel" /dev/sda2
```

### Step 2: Editing the `/etc/fstab` File

The `fstab` file in `/etc/fstab` contains the necessary information to automatically mount partitions at system startup.

#### Backup fstab

Always back up the original `fstab` file before editing:

```bash
sudo cp /etc/fstab /etc/fstab.backup
```

#### Editing fstab

Open the `fstab` file with a text editor:

```bash
sudo vi /etc/fstab
```

Add a new line or modify an existing line for your file system, specifying the UUID or LABEL. For example:

**Using UUID:**

```plaintext
UUID=a1b2c3d4-e5f6-g7h8-i9j0-k11l12m13n14 /mnt/data ext4 defaults 0 2
```

**Using LABEL:**

```plaintext
LABEL=NewLabel /mnt/data xfs defaults 0 2
```

### Step 3: Mounting the File System

After editing and saving your changes in `fstab`, mount the file system:

```bash
sudo mount -a
```

This command will mount all file systems specified in `fstab`.

### Step 4: Verify the Mount

Check that the file system is mounted correctly using:

```bash
df -h
```

Look for your mount point `/mnt/data` in the output.

## Conclusion

In this tutorial, we covered how to configure local storage to mount at boot using UUID and labels, which provides a more reliable mounting system than traditional device names. This setup helps in maintaining system stability and ensures that your file systems are correctly mounted at every boot, regardless of hardware changes.

This knowledge is not only critical for the RHCSA exam but also for real-world system administration tasks in a RHEL environment.