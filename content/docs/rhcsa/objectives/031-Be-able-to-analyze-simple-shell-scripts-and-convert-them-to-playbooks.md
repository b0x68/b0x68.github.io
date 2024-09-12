# Tech Tutorial: Configure Ansible Managed Nodes

In this tutorial, we will delve into how to convert simple shell scripts into Ansible playbooks, a vital skill for the Red Hat Certified System Administrator (RHCSA) exam. This process is crucial for automating system configurations effectively using Ansible, a powerful IT automation tool. We'll focus exclusively on Red Hat Enterprise Linux (RHEL) environments.

## Introduction

Ansible is an open-source automation tool that simplifies cloud provisioning, configuration management, application deployment, intra-service orchestration, and many other IT needs. 

Learning how to convert shell scripts to Ansible playbooks can help you leverage Ansible's idempotent properties (where desired system states are achieved without over-applying configurations), improve scalability, and enhance the readability and maintenance of your automation scripts.

## Prerequisites

- A working RHEL 8 or RHEL 9 environment.
- Ansible installed on a control node (your workstation or a management server).
- One or more managed nodes with SSH access configured.
- Sudo privileges on the managed nodes for running administrative commands.

## Step-by-Step Guide

### Step 1: Setting Up Your Environment

Ensure Ansible is installed on your control node. You can install Ansible on RHEL by using the following commands:

```bash
sudo subscription-manager repos --enable ansible-2-for-rhel-8-x86_64-rpms
sudo dnf install ansible -y
```

Verify the installation by checking the Ansible version:

```bash
ansible --version
```

### Step 2: Understanding the Shell Script

Consider a simple shell script that updates all packages and installs Apache on a RHEL server:

```bash
#!/bin/bash
sudo dnf update -y
sudo dnf install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd
```

### Step 3: Creating the Ansible Playbook

Convert the shell script into an Ansible playbook. Here is how you can structure it:

```yaml
---
- name: Update and install Apache
  hosts: all
  become: yes
  tasks:
    - name: Update all packages
      dnf:
        name: '*'
        state: latest

    - name: Install Apache
      dnf:
        name: httpd
        state: present

    - name: Start and enable Apache
      systemd:
        name: httpd
        state: started
        enabled: yes
```

### Explanation:

- **hosts: all** - The playbook will run on all inventory hosts.
- **become: yes** - Execute tasks with administrative privileges.
- **dnf module** - Used instead of the `dnf` command for idempotent package management.
- **systemd module** - Used to manage the state of the "httpd" service, ensuring it's running and enabled at boot.

### Step 4: Running the Playbook

Create an inventory file named `hosts`:

```ini
[webservers]
192.168.1.101
192.168.1.102
```

Run the playbook:

```bash
ansible-playbook -i hosts update_and_install_apache.yml
```

## Conclusion

Converting shell scripts to Ansible playbooks not only standardizes deployment and configuration scripts across the infrastructure but also enhances the security and efficiency of operations. The playbook provided is idempotent, meaning repeated executions will not change the system's state beyond the desired outcome, reducing potential errors and inconsistencies.

With this skill, you can ensure that your infrastructure automation is robust, scalable, and maintainable, meeting the high standards expected in RHEL environments.

Continue practicing by identifying other common administrative tasks in your environment that can benefit from being managed via Ansible. This approach not only prepares you for the RHCSA exam but also significantly contributes to your professional development as a system administrator.