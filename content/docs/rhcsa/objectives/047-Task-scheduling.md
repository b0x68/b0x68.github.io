# Automate Standard RHCSA Tasks Using Ansible: Focus on Task Scheduling

## Introduction

In the realm of system administration, particularly for Red Hat Certified System Administrator (RHCSA) exam candidates, mastering task automation is crucial. Ansible, a powerful IT automation tool, simplifies complex configuration tasks, ensures consistency across systems, and enhances productivity by automating routine tasks. This tutorial focuses on leveraging Ansible for scheduling tasks on Red Hat Enterprise Linux (RHEL), an essential skill for any RHCSA.

## Why Ansible for Task Scheduling?

Ansible provides a user-friendly approach to manage servers through its declarative language, allowing administrators to define 'what' should be done rather than 'how' to do it. For task scheduling, Ansible can interact with cron, the time-based job scheduler in Unix-like operating systems, including RHEL, to ensure tasks are run at scheduled times.

## Prerequisites

- A RHEL 8 or later system
- Ansible 2.9 or higher installed on a control node (can be the same as the managed node)
- SSH access configured between the control node and the managed nodes (if different)

## Step-by-Step Guide

### 1. Setting Up Your Environment

First, ensure that Ansible is installed on your control node. If not, you can install it using the following command:

```bash
sudo dnf install ansible
```

Verify the installation by checking the Ansible version:

```bash
ansible --version
```

### 2. Configuring Ansible Inventory

Create or edit your Ansible inventory file (`/etc/ansible/hosts`) to include the RHEL nodes you intend to manage:

```ini
[rhel-servers]
rhel-node1 ansible_host=192.168.1.10
rhel-node2 ansible_host=192.168.1.11
```

### 3. Writing Your First Ansible Playbook for Task Scheduling

Create a new YAML file for your playbook (`schedule-task.yml`). Here, we will create a playbook to schedule a backup script to run daily.

```yaml
---
- name: Schedule daily backup task
  hosts: rhel-servers
  become: yes
  tasks:
    - name: Ensure a backup script is present
      copy:
        src: /path/to/local/backup-script.sh
        dest: /usr/local/bin/backup-script.sh
        mode: '0755'

    - name: Schedule cron job for daily backups
      ansible.builtin.cron:
        name: "Daily backup job"
        user: root
        job: "/usr/local/bin/backup-script.sh"
        minute: "0"
        hour: "2"
        day: "*"
        month: "*"
        weekday: "*"
```

### 4. Running Your Ansible Playbook

Execute the playbook using the following command:

```bash
ansible-playbook schedule-task.yml
```

This command will configure the cron job on all the servers listed under `rhel-servers` in your inventory file.

## Detailed Code Examples

### Example: Scheduling a Log Cleanup Task

Let's say you need to schedule a task to clean up logs every week. Here’s how you can write a playbook for this:

```yaml
---
- name: Schedule weekly log cleanup
  hosts: rhel-servers
  become: yes
  tasks:
    - name: Schedule log cleanup every Sunday
      ansible.builtin.cron:
        name: "Weekly log cleanup"
        user: root
        job: "find /var/log -type f -mtime +7 -delete"
        minute: "0"
        hour: "3"
        weekday: "0"
```

### 5. Managing Cron Jobs

To remove a cron job, you can use the `state: absent` parameter:

```yaml
- name: Remove scheduled log cleanup
  ansible.builtin.cron:
    name: "Weekly log cleanup"
    user: root
    state: absent
```

## Conclusion

Automating task scheduling in RHEL using Ansible not only streamlines operations but also ensures that critical tasks are performed consistently and without manual intervention. This tutorial covered the basics of using Ansible for task scheduling, including setting up cron jobs to run scripts at specified times. As you prepare for the RHCSA exam, incorporating these practices will enhance your proficiency in both Ansible and system administration.