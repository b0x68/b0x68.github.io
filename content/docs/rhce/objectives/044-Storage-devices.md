# Automate Storage Device Management in RHEL with Ansible

In this tutorial, we will explore how to automate common Red Hat Certified System Administrator (RHCSA) tasks related to storage devices using Ansible. The focus will exclusively be on RHEL (Red Hat Enterprise Linux) systems, ensuring all commands and modules are compatible with this distribution as required by the RHCE (Red Hat Certified Engineer) exam objectives.

## Introduction

Managing storage devices efficiently is critical in any system administration role, especially in enterprise environments. Ansible, an open-source automation tool, simplifies this process by enabling administrators to automate the configuration and management of storage devices across multiple systems.

This tutorial will cover:
1. Setting up Ansible for RHEL
2. Automating the creation and management of physical volumes, volume groups, and logical volumes
3. Formatting and mounting filesystems
4. Ensuring idempotency and error handling in Ansible playbooks

## Prerequisites

- A RHEL 8 or later system
- Ansible 2.9 or later installed on a control node (which can be the same as the managed node)
- Sudo privileges on the managed node(s)

## Step-by-Step Guide

### Step 1: Setting Up Ansible

First, ensure that Ansible is installed on your control node:

```bash
sudo dnf install ansible
```

Create an inventory file `/etc/ansible/hosts` and add the managed node(s):

```ini
[storage-servers]
rhel-server ansible_host=192.168.1.100
```

Test the connection:

```bash
ansible -m ping rhel-server
```

### Step 2: Creating Physical Volumes

Create a playbook `create_pv.yml` to automate the creation of physical volumes:

```yaml
- hosts: storage-servers
  become: true
  tasks:
    - name: Install required packages
      dnf:
        name: lvm2
        state: present

    - name: Creating Physical Volume
      community.general.lvg:
        pvs: /dev/sdb
        state: present
```

Run the playbook:

```bash
ansible-playbook create_pv.yml
```

### Step 3: Creating Volume Groups and Logical Volumes

Extend the playbook to create a volume group and a logical volume:

```yaml
    - name: Creating Volume Group
      community.general.lvg:
        vg: vg_data
        pvs: /dev/sdb
        state: present

    - name: Creating Logical Volume
      community.general.lvol:
        vg: vg_data
        lv: lv_data
        size: 20G
        state: present
```

### Step 4: Formatting and Mounting Filesystems

Now add tasks to format the logical volume and mount it:

```yaml
    - name: Formatting the Logical Volume
      community.general.filesystem:
        fstype: xfs
        dev: /dev/vg_data/lv_data

    - name: Mounting the Logical Volume
      ansible.builtin.mount:
        path: /data
        src: /dev/vg_data/lv_data
        fstype: xfs
        state: mounted
        opts: defaults
```

### Step 5: Ensure Idempotency

Ensure that the playbook is idempotent by handling conditions where the disk might already be partitioned or the filesystem might already be mounted:

```yaml
    - name: Check if /dev/sdb is already a PV
      community.general.lvg:
        pvs: /dev/sdb
        state: query
      register: pv_check

    - name: Creating Physical Volume
      community.general.lvg:
        pvs: /dev/sdb
        state: present
      when: pv_check.vgs == []
```

## Conclusion

In this tutorial, we've covered how to automate the management of storage devices in RHEL using Ansible. By using Ansible playbooks, we can efficiently handle the creation, configuration, and mounting of physical volumes, volume groups, and logical volumes, ensuring our configurations are repeatable and reliable. This approach not only saves time but also reduces the risk of human errors in managing critical storage resources.

For further reading and more complex scenarios, consider exploring additional Ansible modules and options, or integrating these tasks into larger automation workflows. Remember, automation is key to modern, efficient system administration in enterprise environments.