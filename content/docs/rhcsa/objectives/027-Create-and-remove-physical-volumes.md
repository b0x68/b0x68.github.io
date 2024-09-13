# Tech Tutorial: Configure Local Storage on RHEL

## Exam Objective: Create and remove physical volumes

In this tutorial, we will focus on how to create and remove physical volumes on a Red Hat Enterprise Linux (RHEL) system. Understanding how to manage storage devices is a critical skill for any systems administrator, especially for those preparing for the Red Hat Certified System Administrator (RHCSA) exam.

### Introduction

Physical volumes are the building blocks of the Logical Volume Manager (LVM) in Linux. LVM allows for flexible disk management, enabling resizing of partitions and combining of multiple disks into logical groups. In this guide, we'll cover the necessary steps to manage physical volumes including creation, inspection, and deletion.

### Prerequisites

- A system running Red Hat Enterprise Linux 8 or later.
- Administrative privileges (typically through the `root` user).
- At least one unformatted disk or disk partition available for use.

### Step-by-Step Guide

#### 1. Checking Available Disks

Before creating a physical volume, you need to identify the available storage devices. Use the `lsblk` command to list all block devices along with their mount points (if any).

```bash
lsblk
```

Look for devices that have no mount points as these are available for creating new physical volumes.

#### 2. Creating Physical Volumes

Once you've identified an available disk, you can create a physical volume. Suppose `/dev/sdb` is the disk you want to use. Use the `pvcreate` command:

```bash
pvcreate /dev/sdb
```

This command initializes `/dev/sdb` as a physical volume. For creating multiple physical volumes at once, you can specify multiple devices:

```bash
pvcreate /dev/sdc /dev/sdd
```

#### 3. Verifying Physical Volumes

After creating physical volumes, you can verify them using the `pvdisplay` command. This command shows details about the physical volume such as size, physical extent size, and volume group (if assigned).

```bash
pvdisplay /dev/sdb
```

Alternatively, use `pvs` for a concise display:

```bash
pvs
```

#### 4. Removing Physical Volumes

If you need to remove a physical volume, first ensure that it's not part of an active volume group. If it is, you'll need to remove or move the data to another physical volume first.

Assuming `/dev/sdb` is not part of any volume group, you can remove it using the `pvremove` command:

```bash
pvremove /dev/sdb
```

This command will delete the physical volume from the system. If the disk was previously part of a volume group, ensure all associated logical volumes and the volume group itself have been properly managed before running `pvremove`.

### Detailed Code Examples

Here are some detailed examples of commands used in this tutorial:

- **List block devices:**
  ```bash
  lsblk
  # Output might include /dev/sda, /dev/sdb, etc.
  ```

- **Create a physical volume:**
  ```bash
  pvcreate /dev/sdb
  # Output: "Physical volume "/dev/sdb" successfully created."
  ```

- **Display physical volume details:**
  ```bash
  pvdisplay /dev/sdb
  # Output includes details about the PV, such as size and VG association.
  ```

- **Remove a physical volume:**
  ```bash
  pvremove /dev/sdb
  # Output: "Labels on physical volume "/dev/sdb" successfully wiped."
  ```

### Conclusion

Managing physical volumes is a fundamental task for any systems administrator working with RHEL. By following the steps outlined in this tutorial, you can successfully create, inspect, and remove physical volumes, providing a solid foundation for more advanced LVM operations. Always ensure to back up important data before modifying disk structures to prevent data loss.