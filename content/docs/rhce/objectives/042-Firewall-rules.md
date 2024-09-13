# Automate Standard RHCSA Tasks Using Ansible: Managing Firewall Rules

## Introduction

In the realm of Red Hat Certified Engineer (RHCE) exam preparation, understanding how to automate system administration tasks is crucial. One such task is the management of firewall rules, which is a fundamental aspect of securing systems. In this tutorial, we focus on using Ansible, a powerful automation tool, to manage firewall rules on systems running Red Hat Enterprise Linux (RHEL).

Ansible simplifies complex configuration tasks and ensures consistent environments. Specifically, we will use Ansible modules designed to interact with firewalld, the default firewall management tool on RHEL.

## Prerequisites

- A basic understanding of Linux system administration and firewall concepts.
- One or more RHEL 8 machines (can be virtual machines).
- Ansible installed on a control node (which can also be one of the RHEL machines).

## Step-by-Step Guide

### Step 1: Setting Up Your Environment

First, ensure that `firewalld` is installed and running on your RHEL nodes. You can check this by running:

```bash
sudo systemctl status firewalld
```

If it's not installed or running, you can install and start it using:

```bash
sudo dnf install firewalld
sudo systemctl start firewalld
sudo systemctl enable firewalld
```

On your control node (the machine where Ansible is installed), you need to set up SSH key-based authentication for the RHEL nodes. This allows Ansible to communicate and control the nodes without needing password authentication each time.

### Step 2: Create Ansible Inventory

Create an inventory file on your control node. This file lists all the hosts you want to manage with Ansible.

```ini
# inventory.ini
[rhel]
192.168.56.101
192.168.56.102

[rhel:vars]
ansible_ssh_user=your_user
ansible_ssh_private_key_file=/path/to/your/key
```

### Step 3: Writing Your First Ansible Playbook

Create a playbook `firewall-rules.yml` that configures the necessary firewall settings.

```yaml
---
- name: Configure Firewall Rules
  hosts: rhel
  become: yes
  tasks:
    - name: Ensure firewalld is running
      service:
        name: firewalld
        state: started
        enabled: yes

    - name: Open HTTP service port
      firewalld:
        service: http
        permanent: true
        state: enabled
        immediate: yes

    - name: Allow custom port 8080/tcp
      firewalld:
        port: 8080/tcp
        permanent: true
        state: enabled
        immediate: yes
```

This playbook performs the following tasks:
- Ensures that `firewalld` is running on the target machines.
- Opens the standard HTTP service port (80/tcp) by enabling it in the firewall.
- Adds a custom rule to allow traffic on port 8080/tcp.

### Step 4: Running the Playbook

Run the playbook using the following command:

```bash
ansible-playbook -i inventory.ini firewall-rules.yml
```

### Step 5: Verifying the Configuration

To verify that the rules have been applied, log into one of your RHEL nodes and check the active firewalld rules:

```bash
sudo firewall-cmd --list-all
```

## Detailed Code Examples

### Adding Multiple Services

To enable multiple services at once, you can extend the playbook with additional tasks:

```yaml
- name: Enable multiple services
  firewalld:
    service: "{{ item }}"
    permanent: true
    state: enabled
    immediate: yes
  loop:
    - https
    - mysql
```

### Removing a Service

To remove a service from the firewall:

```yaml
- name: Remove SSH service from firewall
  firewalld:
    service: ssh
    permanent: true
    state: disabled
    immediate: yes
```

## Conclusion

In this tutorial, we have covered how to automate the management of firewall rules on RHEL systems using Ansible. By harnessing the power of Ansible modules like `firewalld`, you can ensure your firewall configurations are consistent and reproducible across numerous systems, an essential skill for any system administrator preparing for the RHCE exam. Automation not only saves time but also reduces the possibility of human error, making your systems more secure and reliable.