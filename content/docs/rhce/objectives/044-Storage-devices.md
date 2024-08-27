# Automate Standard RHCSA Tasks Using Ansible Modules for Storage Devices

In the RHCSA (Red Hat Certified System Administrator) exam, efficient management of storage devices is a crucial skill. Ansible, a powerful automation tool, can simplify and automate tasks related to storage management. In this tutorial, we will explore how to use Ansible modules to handle common storage tasks such as partitioning disks, formatting filesystems, and managing logical volumes.

## Introduction

Ansible is an open-source automation tool that can be used for configuration management, application deployment, task automation, and much more. It uses a simple syntax written in YAML called playbooks. Ansible is agentless, meaning it does not require any software to be installed on the nodes it manages. Instead, it uses SSH to communicate with the nodes.

For storage management, Ansible provides various modules that can be used to automate tasks related to disk partitions, filesystems, and logical volume management. This can significantly reduce the risk of human errors, save time during setups or maintenance, and ensure consistency across multiple systems.

## Prerequisites

Before you start, you will need the following:
- A machine with Ansible installed.
- One or more managed nodes (these can be any system that supports SSH and Python).
- Sudo privileges on the managed nodes.

## Step-by-Step Guide

### Step 1: Setting Up Your Inventory

Create an inventory file that lists the nodes you want to manage. Here's an example:

```ini
[storage-nodes]
node1 ansible_host=192.168.1.101
node2 ansible_host=192.168.1.102
```

### Step 2: Writing Your Ansible Playbook

We’ll create a playbook that covers three main tasks:
1. Creating a disk partition.
2. Creating a filesystem on that partition.
3. Creating and managing a logical volume.

#### Task 1: Creating a Disk Partition

We'll use the `community.general.parted` module, which allows us to manipulate partition tables. Here's an example task to create a primary partition:

```yaml
- name: Create a primary partition
  community.general.parted:
    device: /dev/sdb
    number: 1
    state: present
    part_start: 0%
    part_end: 100%
    part_type: primary
```

#### Task 2: Creating a Filesystem

Next, we'll use the `ansible.builtin.filesystem` module to create a filesystem on the newly created partition:

```yaml
- name: Create ext4 filesystem on /dev/sdb1
  ansible.builtin.filesystem:
    fstype: ext4
    dev: /dev/sdb1
```

#### Task 3: Creating and Managing Logical Volumes

We'll use the `community.general.lvol` and `community.general.vg` modules for logical volume management. First, create a volume group, then a logical volume:

```yaml
- name: Create volume group
  community.general.vg:
    vg: vg01
    pvs: /dev/sdb1
    state: present

- name: Create logical volume
  community.general.lvol:
    vg: vg01
    lv: lv01
    size: 10G
    state: present
```

### Step 3: Running the Playbook

Save your playbook as `storage.yml` and run it with:

```bash
ansible-playbook -i inventory storage.yml
```

## Conclusion

Using Ansible for automating tasks related to storage devices can streamline the setup and management of storage in your infrastructure. By integrating these tasks into Ansible playbooks, you can ensure they are performed consistently and without manual intervention, thereby reducing errors and saving time.

This tutorial covered basic scenarios to get you started with disk partitioning, filesystem creation, and logical volume management using Ansible. As you become more familiar with Ansible and its modules, you can expand your playbooks to cover more complex scenarios and further automate your environment.