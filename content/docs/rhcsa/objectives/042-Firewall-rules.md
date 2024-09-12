# Tech Tutorial: Automate Standard RHCSA Tasks Using Ansible Modules for Firewall Rules

## Introduction

The Red Hat Certified System Administrator (RHCSA) exam requires the mastery of numerous system administration tasks, including the management of firewall rules, which is critical for ensuring the security and proper network functioning of RHEL systems. Ansible, an open-source automation tool, greatly simplifies and automates the management of firewall settings across multiple systems. This tutorial specifically focuses on using Ansible to manage firewall rules in a Red Hat Enterprise Linux (RHEL) environment.

## Objectives

By the end of this tutorial, you will understand how to:
1. Set up Ansible in a RHEL environment.
2. Use Ansible modules to manage firewall rules.
3. Automate the deployment of firewall rules across multiple RHEL servers.

## Prerequisites

- Basic knowledge of RHEL system administration and firewall concepts.
- RHEL 8 installed on one or more machines for testing.
- Ansible installed on a control node (which might also be one of your RHEL systems).

## Step-by-Step Guide

### Step 1: Setting Up Your Ansible Environment

First, ensure that Ansible is installed on your control node. You can install Ansible on RHEL by enabling the EPEL repository and then installing the package using `dnf`:

```bash
sudo dnf install -y epel-release
sudo dnf install -y ansible
```

Verify the installation by checking the Ansible version:

```bash
ansible --version
```

### Step 2: Define Your Inventory

Create an inventory file (e.g., `hosts.ini`) that lists the RHEL servers where you want to manage firewall rules:

```ini
[firewall-servers]
server1 ansible_host=192.168.1.101
server2 ansible_host=192.168.1.102
```

### Step 3: Manage Firewall Rules Using Ansible

Ansible uses a variety of modules to manage firewalld, the default firewall management tool used in RHEL. The `firewalld` Ansible module is used to modify firewall settings.

#### Example 1: Opening a Single Port

Create an Ansible playbook named `open_port.yml`:

```yaml
---
- name: Open HTTP port
  hosts: firewall-servers
  become: yes
  tasks:
    - name: Ensure firewalld is running
      service:
        name: firewalld
        state: started
        enabled: yes

    - name: Open port 80/tcp
      firewalld:
        port: 80/tcp
        permanent: true
        state: enabled
        immediate: true
```

Run the playbook:

```bash
ansible-playbook open_port.yml
```

#### Example 2: Blocking an IP Address

Create another playbook named `block_ip.yml`:

```yaml
---
- name: Block an IP address
  hosts: firewall-servers
  become: yes
  tasks:
    - name: Block IP address
      firewalld:
        rich_rule: 'rule family="ipv4" source address="192.168.1.200" reject'
        permanent: true
        state: enabled
        immediate: true
```

Run the playbook:

```bash
ansible-playbook block_ip.yml
```

### Step 4: Testing and Validation

After applying the firewall changes, verify them directly on your RHEL servers:

1. To check if port 80 is open:

    ```bash
    firewall-cmd --list-all
    ```

2. To check if the IP block rule is active:

    ```bash
    firewall-cmd --list-rich-rules
    ```

## Conclusion

Automating firewall rules using Ansible provides a scalable, reliable, and error-free method compared to manual configurations. By leveraging Ansible's `firewalld` module, sysadmins can ensure consistent firewall policies across all managed RHEL systems, enhancing security and compliance with organizational standards.

This tutorial covered basic scenarios to get you started with automating firewall management using Ansible. However, Ansible's capabilities allow for much more complex configurations and automations, which can be tailored to meet the specific needs of any organization.