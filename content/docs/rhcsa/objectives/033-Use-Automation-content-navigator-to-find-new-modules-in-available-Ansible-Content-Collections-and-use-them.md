# Tech Tutorial: Run Playbooks with Automation Content Navigator

## Introduction

In the realm of automation, efficiency and adaptability are paramount. Ansible, a popular automation tool, offers a rich ecosystem of modules and plugins through its Ansible Content Collections. The Automation Content Navigator is a powerful feature designed to help users discover and utilize these collections effectively. This tutorial is tailored for the Red Hat Certified System Administrator (RHCSA) exam and focuses exclusively on RHEL (Red Hat Enterprise Linux) compatible commands and procedures.

The aim of this tutorial is to guide you on how to use the Automation Content Navigator to find new modules within available Ansible Content Collections and how to incorporate them into your playbooks.

## Prerequisites

- A working RHEL 8 or later system.
- Ansible installed on your RHEL system (Ansible Core 2.9 or higher is recommended).
- Basic familiarity with YAML and Ansible playbook concepts.

## Step-by-Step Guide

### Step 1: Installing Ansible

First, ensure Ansible is installed on your RHEL system. You can install Ansible using the following command:

```bash
sudo dnf install ansible
```

### Step 2: Accessing Automation Content Navigator

Automation Content Navigator is integrated into the Red Hat Ansible Automation Platform. To access it, you need a Red Hat account and a subscription to the platform. Once you have access, you can navigate to the Automation Content Navigator through the Red Hat Automation Hub at `https://cloud.redhat.com/ansible/automation-hub`.

### Step 3: Exploring Ansible Content Collections

Once in the Automation Content Navigator, you can explore various Ansible Content Collections. Collections are packaged with roles, modules, and plugins. Use the search bar or browse through categories to find collections relevant to your needs.

For instance, if you are looking for networking modules, you might look into the `ansible.netcommon` collection.

### Step 4: Installing a Collection

To use a collection in your Ansible playbooks, you first need to install it. You can install collections from the Automation Hub using the `ansible-galaxy` command. For example, to install the `ansible.netcommon` collection, use:

```bash
ansible-galaxy collection install ansible.netcommon
```

### Step 5: Finding New Modules in a Collection

After installing the collection, you can find new modules by listing the contents of the collection:

```bash
ansible-doc -l -t module ansible.netcommon
```

This command lists all the modules in the `ansible.netcommon` collection, helping you discover new tools available for your automation tasks.

### Step 6: Writing a Playbook Using a New Module

Now that you have discovered new modules, you can start using them in your playbooks. Here’s a simple example of a playbook using a module from the `ansible.netcommon` collection, which ensures a VLAN is present on a network device:

```yaml
---
- name: Configure VLAN using ansible.netcommon
  hosts: all
  tasks:
    - name: Ensure VLAN 100 is present
      ansible.netcommon.net_vlan:
        vlan_id: 100
        name: "GuestNetwork"
        state: present
```

### Step 7: Running the Playbook

Save your playbook with a `.yml` extension, for example, `vlan-setup.yml`. Run the playbook using the ansible-playbook command:

```bash
ansible-playbook vlan-setup.yml
```

## Detailed Code Examples

Here is another detailed example where we utilize the `ansible.builtin.copy` module from the `ansible.builtin` collection to copy files from the local machine to remote hosts:

```yaml
---
- name: Copy files to remote hosts
  hosts: all
  tasks:
    - name: Copy a file to remote servers
      ansible.builtin.copy:
        src: /src/path/to/file.txt
        dest: /dest/path/on/remote/
        owner: root
        group: root
        mode: '0644'
```

## Conclusion

The Automation Content Navigator is a valuable tool in the Ansible ecosystem, allowing users to seamlessly discover and implement new automation modules. By following this guide, you should now be able to explore Ansible Content Collections, identify useful modules, and integrate them into your automation workflows efficiently. Remember, continual learning and adaptation are key in mastering automation with Ansible.

Happy automating!