# Automate RHCSA Security Tasks Using Ansible on RHEL

## Introduction

Security automation is a critical aspect of managing enterprise environments effectively, ensuring consistent application of security policies across a wide range of systems. In this tutorial, we will explore how to automate various RHCSA security tasks using Ansible, specifically focusing on Red Hat Enterprise Linux (RHEL) systems. This approach not only enhances security but also reduces the possibility of human error and saves time for system administrators.

## Prerequisites

Before proceeding, ensure you have the following setup:

- A control node with Ansible installed. This can be any system where Ansible is installed and from which it will orchestrate the configuration tasks.
- One or more RHEL 8 systems as managed nodes.
- SSH access and appropriate privileges on all managed nodes.

## Step-by-Step Guide

### 1. Setting Up Ansible on RHEL

First, ensure Ansible is installed on your control node, which could also be a RHEL system:

```bash
sudo dnf install ansible -y
```

Create an inventory file `/etc/ansible/hosts` and add your RHEL managed nodes:

```ini
[rhel-nodes]
192.168.1.101
192.168.1.102
```

### 2. Configuring SSH Key-Based Authentication

To facilitate Ansible's communication with managed nodes, set up SSH key-based authentication:

```bash
ssh-keygen -t rsa
ssh-copy-id -i ~/.ssh/id_rsa.pub root@192.168.1.101
ssh-copy-id -i ~/.ssh/id_rsa.pub root@192.168.1.102
```

### 3. Ansible Playbook for Security Tasks

Create a YAML file named `security.yml` for the Ansible playbook which will include tasks related to security configurations.

#### Task 1: Ensuring SELinux is Enabled and Enforcing

SELinux is a security module that provides a mechanism for supporting access control security policies. Here's how to ensure it is enabled and set to enforcing mode:

```yaml
---
- name: Ensure SELinux is enforcing
  hosts: rhel-nodes
  become: true

  tasks:
    - name: Ensure SELinux is not disabled
      selinux:
        state: enforcing
```

#### Task 2: Managing User Accounts and Password Policies

Ensuring that password policies and user account security are compliant with organizational standards is crucial.

```yaml
  tasks:
    - name: Ensure password expiration is 90 days
      pamd:
        name: system-auth
        type: password
        control: sufficient
        module_path: pam_unix.so
        module_arguments: remember=5 minlen=12
        state: updated

    - name: Create a secure user account
      user:
        name: secureuser
        password: "{{ 'securepassword' | password_hash('sha512') }}"
        comment: Secure User Account
```

#### Task 3: Configuring Firewall Settings

Firewalls are essential for defining which services are visible on your network. In RHEL, `firewalld` is the default firewall management tool.

```yaml
  tasks:
    - name: Ensure firewalld is running
      service:
        name: firewalld
        state: started
        enabled: yes

    - name: Open default secure SSH port
      firewalld:
        service: ssh
        permanent: true
        state: enabled
```

### 4. Running the Playbook

Execute the playbook to apply these security settings across all specified RHEL nodes:

```bash
ansible-playbook security.yml
```

## Conclusion

In this tutorial, we've automated several key security tasks for RHEL systems using Ansible. By leveraging Ansible, system administrators can ensure that all RHEL systems in their environment adhere to the same security standards, efficiently and consistently. This not only improves security but also simplifies management and enhances compliance across the infrastructure.

Remember, the examples provided here should be tailored as per your organizational security policies and requirements. Automation is a powerful tool, and with great power comes great responsibility—always test in a controlled environment before deploying into production.