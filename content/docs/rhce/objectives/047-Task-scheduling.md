# Automate Standard RHCSA Tasks Using Ansible: Focus on Task Scheduling

In this tutorial, we will delve into automating common Red Hat Certified System Administrator (RHCSA) tasks specifically focusing on task scheduling using Ansible. Ansible, a powerful IT automation tool, simplifies complex configuration tasks and reduces the potential for human error. Since task scheduling is a critical component in system administration, automating this can significantly enhance system efficiency and reliability.

## Introduction

Task scheduling in RHEL environments typically involves managing cron jobs. Cron is a time-based job scheduler in Unix-like operating systems, and RHEL is no exception. System administrators use cron to schedule jobs (commands or scripts) to run periodically at fixed times, dates, or intervals. Ansible provides a seamless method to manage cron jobs through its `cron` module.

## Prerequisites

Before proceeding, ensure you have the following setup:

- A RHEL-based system where you have root or sudo privileges.
- Ansible installed on a control node (which can be your local machine or a separate management server).
- SSH access configured from the control node to the RHEL target node.

## Step-by-Step Guide

### Step 1: Setting Up Ansible

First, ensure Ansible is installed on your control node. If not, you can install it using the following command:

```bash
sudo yum install ansible
```

Next, configure Ansible to communicate with your RHEL node. Create or edit the `/etc/ansible/hosts` inventory file to include your RHEL server:

```ini
[rhel-servers]
rhel-node1 ansible_host=192.168.1.100
```

### Step 2: Creating the Ansible Playbook

Create a new YAML file for your playbook. This playbook will define the tasks that Ansible will execute on the target RHEL system.

```yaml
---
- name: Schedule tasks using Ansible
  hosts: rhel-servers
  become: yes
  tasks:
    - name: Ensure a script runs daily
      cron:
        name: "Daily backup job"
        job: "/usr/local/bin/backup.sh"
        minute: "0"
        hour: "2"
        user: root
```

This playbook contains a single task which ensures that a script (`/usr/local/bin/backup.sh`) runs daily at 2:00 AM.

### Step 3: Running the Playbook

Execute the playbook using the `ansible-playbook` command:

```bash
ansible-playbook schedule_tasks.yml
```

### Step 4: Verifying the Cron Job

To verify that the cron job has been correctly scheduled, SSH into the RHEL server and list the cron jobs:

```bash
ssh root@192.168.1.100
crontab -l
```

You should see the newly scheduled cron job listed.

## Detailed Code Examples

### Example: Scheduling a Weekly Database Cleanup Job

Here’s how you can schedule a weekly database cleanup using Ansible's cron module:

```yaml
---
- name: Schedule weekly database cleanup
  hosts: rhel-servers
  become: yes
  tasks:
    - name: Schedule weekly database cleanup job
      cron:
        name: "Weekly DB cleanup"
        job: "/usr/local/bin/db_cleanup.sh"
        weekday: "6"
        hour: "3"
        user: root
```

This playbook schedules the `db_cleanup.sh` script to run every Saturday at 3:00 AM.

### Example: Removing a Cron Job

If you need to remove a cron job, you can use the `cron` module with `state: absent`:

```yaml
---
- name: Remove scheduled job
  hosts: rhel-servers
  become: yes
  tasks:
    - name: Remove the daily backup job
      cron:
        name: "Daily backup job"
        state: absent
```

## Conclusion

Using Ansible to automate task scheduling on RHEL systems not only simplifies management but also ensures consistency across multiple systems. By leveraging Ansible's `cron` module, you can easily manage cron jobs, ensuring that your scheduled tasks run precisely and reliably. This approach reduces manual intervention and helps maintain system integrity and performance.

As you continue to explore Ansible, consider integrating more complex playbooks and roles to manage a broader range of system administration tasks effectively.