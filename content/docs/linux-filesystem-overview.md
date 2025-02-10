---
date: 2025-02-07
weight: 2.1
linktitle: Linux Filesystem Overview
title: Linux Filesystem Overview
---
![a conifer twig](/linux-development-git-branch.png)
# The Linux Filesystem: A Comprehensive Guide

The Linux filesystem is a structured hierarchy that organizes files and directories in a predictable way. Understanding its layout, structure, and key components is crucial for system administrators, developers, and power users.

## Introduction

A filesystem in Linux determines how files are stored, accessed, and managed. It provides a logical structure to organize data efficiently.

## Filesystem Hierarchy Standard (FHS)

The **Filesystem Hierarchy Standard (FHS)** defines the structure of directories and files in Unix-like operating systems. It ensures consistency across distributions.

## Key Directories in Linux

### `/`
The root directory, the starting point of the Linux filesystem.

### `/bin`
Essential user binaries (e.g., `ls`, `cp`, `mv`).

### `/boot`
Bootloader-related files (e.g., `grub`, `vmlinuz`).

### `/dev`
Device files (e.g., `/dev/sda`, `/dev/null`).

### `/etc`
System configuration files.

### `/home`
User home directories.

### `/lib`, `/lib64`
Essential shared libraries.

### `/mnt` & `/media`
Mount points for external devices.

### `/opt`
Optional software packages.

### `/proc`
Virtual filesystem with system and process information.

### `/root`
Home directory of the root user.

### `/sbin`
System binaries (e.g., `fsck`, `mount`).

### `/tmp`
Temporary files.

### `/usr`
User binaries, libraries, and documentation.

### `/var`
Variable data (logs, caches, etc.).

---

## Filesystem Types

Linux supports various filesystems, each suited for different use cases:

- **ext4**: Default in most distributions, journaling support.
- **XFS**: High-performance, suitable for large-scale storage.
- **Btrfs**: Advanced features like snapshots and subvolumes.
- **ZFS**: High redundancy, self-healing.
- **tmpfs**: RAM-based filesystem, used for temporary storage.
- **NFS**: Network File System for sharing files over networks.

---

## Filesystem Mounting

To access a filesystem, it must be **mounted**:

```bash
# Mount a device to a directory
mount /dev/sdb1 /mnt

# Unmount a device
umount /mnt
```

To make mounts persistent, edit `/etc/fstab`:

```bash
/dev/sdb1  /mnt  ext4  defaults  0  2
```

---

## Filesystem Permissions

Linux employs a permission model:

- **Owner, Group, Others**
- **Read (r), Write (w), Execute (x)**

```bash
# Change file permissions
chmod 755 file.txt

# Change file ownership
chown user:group file.txt
```

---

## Filesystem Management Commands

### Viewing Disk Usage
```bash
df -h  # Show disk usage in human-readable format
du -sh /home/user  # Show directory size
```

### Creating and Formatting Filesystems
```bash
mkfs.ext4 /dev/sdb1  # Create an ext4 filesystem
```

### Checking and Repairing Filesystems
```bash
fsck /dev/sdb1  # Check and repair a filesystem
```

---

## Advanced Filesystem Topics

### Logical Volume Management (LVM)
LVM allows flexible disk management:

```bash
pvcreate /dev/sdb1
vgcreate my_vg /dev/sdb1
lvcreate -L 10G -n my_lv my_vg
mkfs.ext4 /dev/my_vg/my_lv
```

### Filesystem Encryption
For security, encrypt filesystems with LUKS:

```bash
cryptsetup luksFormat /dev/sdb1
cryptsetup open /dev/sdb1 my_encrypted_volume
```

### Snapshots with Btrfs
Btrfs supports snapshots for rollback capability:

```bash
btrfs subvolume snapshot /home /home_snapshot
```

---

## Conclusion

Understanding the Linux filesystem is essential for system administration, security, and performance tuning. Mastering filesystem operations enables better control over data management and system stability.
