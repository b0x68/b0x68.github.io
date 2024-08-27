# Automate Standard RHCSA Security Tasks Using Ansible

## Introduction

In the realm of system administration, particularly under Red Hat Certified System Administrator (RHCSA) standards, managing security configurations across numerous systems can be daunting. Ansible, an open-source automation tool, simplifies this task by automating the configuration and management of security settings in a scalable and repeatable manner. This tutorial will guide you through using Ansible to automate several common security-related tasks aligned with RHCSA objectives.

## Prerequisites

To follow along with this tutorial, you should have:

- A basic understanding of Linux system administration.
- One or more Red Hat Enterprise Linux (RHEL) or CentOS systems.
- Ansible installed on a control node (which could be one of your RHEL/CentOS systems).

## Step-by-Step Guide

### Setting Up Your Environment

1. **Install Ansible on the Control Node**:
   Ensure Ansible is installed on your control node. You can install Ansible using the following command:

   ```bash
   sudo yum install ansible
   ```

2. **Configure Ansible Inventory**:
   Edit `/etc/ansible/hosts` and add your managed nodes under a group `[rhcsa_security]`:

   ```ini
   [rhcsa_security]
   server1.example.com
   server2.example.com
   ```

### Detailed Code Examples

#### 1. Configuring User Password Policies

Ensuring that user password policies meet specific security criteria is crucial. Ansible can automate the configuration of password policies using the `pam_pwquality` module.

**Example Ansible Playbook: `password_policy.yml`**

```yaml
---
- name: Configure Password Quality Requirements
  hosts: rhcsa_security
  become: yes

  tasks:
    - name: Set password quality control
      pam_pwquality:
        minlen: 12
        dcredit: -1
        ucredit: -1
        lcredit: -1
        ocredit: -1
        retry: 3
        enforce_for_root: yes
        state: present
```

This playbook sets the minimum length of the password to 12 characters and requires at least one digit, one uppercase letter, one lowercase letter, and one special character.

#### 2. Ensuring SSH Security

Configuring SSH securely is another critical task. The `ansible.builtin.lineinfile` module can ensure specific settings in `sshd_config`.

**Example Ansible Playbook: `secure_ssh.yml`**

```yaml
---
- name: Secure SSH Configuration
  hosts: rhcsa_security
  become: yes

  tasks:
    - name: Disable root SSH login
      ansible.builtin.lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^PermitRootLogin'
        line: 'PermitRootLogin no'
        state: present

    - name: Disable empty passwords
      ansible.builtin.lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^PermitEmptyPasswords'
        line: 'PermitEmptyPasswords no'
        state: present

    - name: Use only Protocol 2
      ansible.builtin.lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^Protocol'
        line: 'Protocol 2'
        state: present

    - name: Restart SSH service
      ansible.builtin.systemd:
        name: sshd
        state: restarted
```

This playbook configures SSH to disallow root logins, empty passwords, and ensures that only SSH Protocol 2 is used. It also restarts the SSH service to apply changes.

### Conclusion

Ansible provides a robust framework for automating various security-related configurations and tasks. By leveraging Ansible modules like `pam_pwquality` and `ansible.builtin.lineinfile`, system administrators can ensure that their systems comply with security best practices and RHCSA standards efficiently and consistently.

This tutorial covered only a couple of the many possible security automations. Expanding on these foundations, you can continue to explore other Ansible modules and playbooks to secure other aspects of your systems in alignment with RHCSA or even more stringent security requirements. Automation not only saves time but also enhances the reliability and consistency of system configurations across a large environment.