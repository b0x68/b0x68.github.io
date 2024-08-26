# Tech Tutorial: Configure Local Storage

## Introduction

In this tutorial, we will focus on managing local storage using Logical Volume Manager (LVM) in a Linux environment. LVM is a widely used tool that allows administrators to create, resize, and manage disk drives and other storage devices in a more flexible manner than traditional partitioning schemes. Specifically, we'll learn how to create and delete logical volumes, which are resizable storage units within a volume group.

The ability to configure logical volumes is crucial for effective storage management and ensuring that applications have the necessary space they need to operate. This tutorial is designed for system administrators and other IT professionals who need to manage disk space effectively.

## Prerequisites

To follow this tutorial, you should have:
- A Linux system with LVM support installed.
- At least one unpartitioned disk or free space available on existing disks for creating new volumes.
- Basic familiarity with terminal and command-line operations.

## Step-by-Step Guide

### 1. Installing LVM Tools

First, ensure that LVM is installed on your system. You can install LVM with the following commands:

```bash
sudo apt update
sudo apt install lvm2
```

This command works on Debian-based distributions. For other distributions, use the appropriate package manager like `yum` or `dnf`.

### 2. Preparing Physical Volumes

Before you can create logical volumes, you need to prepare at least one physical volume. Let's assume we have a new disk `/dev/sdb`.

```bash
sudo pvcreate /dev/sdb
```

This command initializes `/dev/sdb` as a physical volume that can be used by LVM.

### 3. Creating a Volume Group

A volume group is a container for logical volumes, made up of one or more physical volumes. Let's create a volume group named `vg01`.

```bash
sudo vgcreate vg01 /dev/sdb
```

This command creates a new volume group `vg01` using the physical volume `/dev/sdb`.

### 4. Creating Logical Volumes

Now, let's create a logical volume within `vg01`. Suppose we want a logical volume of 10GB named `lv01`.

```bash
sudo lvcreate -L 10G -n lv01 vg01
```

This command creates a logical volume named `lv01` with a size of 10GB within the volume group `vg01`.

### 5. Formatting and Mounting the Logical Volume

To use the logical volume, you need to format it with a file system and then mount it.

```bash
sudo mkfs.ext4 /dev/vg01/lv01
sudo mount /dev/vg01/lv01 /mnt
```

Now, the logical volume `lv01` is formatted with the ext4 file system and mounted at `/mnt`.

### 6. Deleting Logical Volumes

To delete a logical volume, first ensure it is not mounted:

```bash
sudo umount /mnt
```

Then, remove the logical volume:

```bash
sudo lvremove /dev/vg01/lv01
```

Confirm the removal when prompted.

## Detailed Code Examples

This section provides additional commands that might be useful when managing logical volumes:

- **Viewing Physical Volumes:**
  ```bash
  sudo pvdisplay
  ```
- **Viewing Volume Groups:**
  ```bash
  sudo vgdisplay
  ```
- **Viewing Logical Volumes:**
  ```bash
  sudo lvdisplay
  ```

These commands provide detailed information about the current configuration and status of your LVM setup.

## Conclusion

In this tutorial, we covered how to configure local storage using LVM by creating and deleting logical volumes. The flexibility offered by LVM makes it an invaluable tool for managing disk space, especially in dynamic environments where storage requirements can change frequently. By mastering these skills, you can efficiently manage storage resources in a Linux environment, ensuring optimal performance and scalability.