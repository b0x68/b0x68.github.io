# Tech Tutorial: Automate Standard RHCSA Tasks Using Ansible for Storage Devices

## Introduction

In the Red Hat Certified System Administrator (RHCSA) exam, efficient management of storage devices is a crucial skill. Automation tools like Ansible can significantly streamline this process. This tutorial focuses on using Ansible modules designed specifically for managing storage on systems running Red Hat Enterprise Linux (RHEL). We’ll cover how to automate tasks such as partitioning disks, creating filesystems, and managing logical volumes.

## Prerequisites

Before you start, ensure you have the following:
- A RHEL 8 system configured for testing.
- Ansible installed on a control node (which can be your RHEL system or another machine).
- Sudo privileges on the managed node(s).

## Step-by-Step Guide

### Step 1: Setup Ansible

First, install Ansible on your control node if it's not already installed:

```bash
sudo dnf install ansible
```

Next, create an inventory file `/etc/ansible/hosts` and add the RHEL server you are managing:

```ini
[rhel]
192.168.1.100 ansible_ssh_user=rhuser ansible_ssh_pass=rhpassword
```

*Note: Replace the IP address and credentials with those applicable to your environment.*

### Step 2: Automate Disk Partitioning

Let's start by automating the creation of a new disk partition.

1. **Create an Ansible Playbook**: Create a file named `partition_disk.yml`.

```yaml
---
- name: Partition Disk
  hosts: rhel
  become: yes
  tasks:
    - name: Create a primary partition
      community.general.parted:
        device: /dev/sdb
        number: 1
        state: present
        part_start: 0%
        part_end: 100%
        part_type: primary
```

*Note: Ensure `/dev/sdb` is the correct disk and it is not already partitioned.*

2. **Run the playbook**:

```bash
ansible-playbook partition_disk.yml
```

### Step 3: Creating Filesystems

After partitioning the disk, the next step is to create a filesystem on the partition.

1. **Update your playbook** to add a new task:

```yaml
    - name: Create an ext4 filesystem on /dev/sdb1
      community.general.filesystem:
        fstype: ext4
        dev: /dev/sdb1
```

2. **Execute the playbook again**:

```bash
ansible-playbook partition_disk.yml
```

### Step 4: Manage Logical Volumes

Ansible can also be used to configure LVM. Here's how to create a volume group and a logical volume.

1. **Modify your playbook** to include LVM tasks:

```yaml
    - name: Create a volume group
      community.general.lvg:
        vg: vg01
        pvs: /dev/sdb1

    - name: Create a logical volume
      community.general.lvol:
        vg: vg01
        lv: lv01
        size: 50%VG
```

2. **Run your playbook**:

```bash
ansible-playbook partition_disk.yml
```

## Detailed Code Examples

The playbook `partition_disk.yml` now looks like this:

```yaml
---
- name: Automate Storage Management
  hosts: rhel
  become: yes
  tasks:
    - name: Create a primary partition
      community.general.parted:
        device: /dev/sdb
        number: 1
        state: present
        part_start: 0%
        part_end: 100%
        part_type: primary

    - name: Create an ext4 filesystem on /dev/sdb1
      community.general.filesystem:
        fstype: ext4
        dev: /dev/sdb1

    - name: Create a volume group
      community.general.lvg:
        vg: vg01
        pvs: /dev/sdb1

    - name: Create a logical volume
      community.general.lvol:
        vg: vg01
        lv: lv01
        size: 50%VG
```

## Conclusion

Using Ansible for automating storage management tasks not only simplifies the process but also reduces the risk of human errors, especially in large-scale environments. By following the steps in this tutorial, you can start automating the management of storage devices in your RHEL environment, ensuring consistency and efficiency in your operations. As you become more comfortable with Ansible, consider expanding your automation to include other aspects of RHEL system administration.