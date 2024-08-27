# Tech Tutorial: Automate Standard RHCSA Tasks Using Ansible for Task Scheduling

## Introduction

In this tutorial, we will explore how to automate task scheduling, a key component of the Red Hat Certified System Administrator (RHCSA) exam, using Ansible. Task scheduling in Linux is typically managed with cron jobs, and handling this through Ansible can streamline the process across multiple systems, ensuring consistency and efficiency.

Ansible, an open-source automation tool, allows us to configure systems, deploy software, and orchestrate more advanced IT tasks such as continuous deployments or zero downtime rolling updates.

## Prerequisites

Before starting, you should have the following:
- A basic understanding of Linux systems and the command line.
- One or more target Linux servers where you have root access.
- Ansible installed on a control node (which could also be your workstation).

## Step-by-Step Guide

### Step 1: Setting Up Your Environment

First, ensure Ansible is installed on your control node. You can install Ansible on a Linux machine using the following command:

```bash
sudo apt-get install ansible
```

Next, set up the inventory file (`/etc/ansible/hosts`) by adding the IP addresses or hostnames of your Linux servers:

```ini
[servers]
192.168.1.50
192.168.1.51
```

### Step 2: Writing Your First Playbook

Create a new file named `schedule-task.yml`. This is where we will define what we want Ansible to do.

```yaml
---
- name: Schedule a cron job on remote servers
  hosts: servers
  become: yes

  tasks:
    - name: Ensure a cron job exists
      ansible.builtin.cron:
        name: "Backup job"
        minute: "0"
        hour: "2"
        job: "/usr/bin/zip -r /backup/$(date +%Y%m%d)_backup.zip /important/data"
        state: present
```

This playbook includes one task, which ensures a cron job is present on all servers listed under the `servers` group in your Ansible inventory.

### Step 3: Running the Playbook

Execute the playbook using the following command:

```bash
ansible-playbook schedule-task.yml
```

### Step 4: Verifying the Cron Job

You can verify that the cron job has been added by logging into one of your managed nodes and running:

```bash
crontab -l
```

You should see the cron job listed:

```
#Ansible: Backup job
0 2 * * * /usr/bin/zip -r /backup/$(date +%Y%m%d)_backup.zip /important/data
```

## Detailed Code Examples

The `ansible.builtin.cron` module is highly versatile. Below are more examples of how it can be used to manage cron jobs:

### Example 1: Removing a Cron Job

To remove a previously added cron job, modify the state to `absent`.

```yaml
tasks:
  - name: Remove the backup job
    ansible.builtin.cron:
      name: "Backup job"
      state: absent
```

### Example 2: Managing Cron Files

For more complex scheduling, you might prefer to manage entire cron files:

```yaml
tasks:
  - name: Deploy custom cron file
    ansible.builtin.copy:
      src: /path/to/mycronfile
      dest: /etc/cron.d/mycronfile
    notify:
      - restart cron

handlers:
  - name: restart cron
    ansible.builtin.service:
      name: cron
      state: restarted
```

This example deploys a custom cron file and ensures the cron service is restarted to apply changes.

## Conclusion

Using Ansible to manage cron jobs across multiple servers can significantly simplify system administration. It ensures that task scheduling is consistent across the infrastructure, reduces the potential for human error, and can be seamlessly integrated into larger automation workflows. As you continue to work with Ansible, you'll find it an invaluable tool for managing not just cron jobs but numerous other aspects of system administration.