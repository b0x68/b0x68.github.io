# Tech Tutorial: Configure Ansible Managed Nodes

## Introduction

In this tutorial, we will delve into how to configure privilege escalation on managed nodes using Ansible, specifically focusing on Red Hat Enterprise Linux (RHEL) systems. Privilege escalation is critical when executing tasks that require higher privileges than those provided by the default user. Ansible, a powerful automation tool, simplifies this process across multiple nodes, enhancing both efficiency and scalability.

Understanding and configuring privilege escalation is essential for systems administrators looking to automate the management of RHEL systems securely and effectively. This tutorial is particularly tailored for those preparing for the Red Hat Certified Engineer (RHCE) exam, focusing exclusively on RHEL commands and methodologies.

## Step-by-Step Guide

### Prerequisites

- A control node with Ansible installed. The control node is the machine from which Ansible will be run.
- One or more managed nodes running RHEL. These nodes are the target systems that Ansible will manage.
- SSH access configured between the control node and the managed nodes.
- Sudo privileges on the managed nodes for the user that Ansible will use.

### 1. Configuring Ansible Control Node

First, ensure that Ansible is installed on your control node. You can install Ansible on a RHEL system using the following command:

```bash
sudo yum install ansible
```

Verify the installation by checking the Ansible version:

```bash
ansible --version
```

### 2. Setting Up SSH Keys

To allow Ansible to communicate with your managed nodes, set up SSH keys for passwordless authentication:

On the control node, generate an SSH key pair:

```bash
ssh-keygen -t rsa
```

Copy the public key to each managed node:

```bash
ssh-copy-id user@managed-node-address
```

### 3. Testing Connection

Ensure that Ansible can connect to the managed nodes via SSH. Create an inventory file `/etc/ansible/hosts` and add your managed nodes:

```ini
[managed_nodes]
192.168.1.101
192.168.1.102
```

Test the connection using the `ping` module:

```bash
ansible managed_nodes -m ping
```

### 4. Configuring Privilege Escalation

To configure privilege escalation, you need to edit the Ansible configuration file `/etc/ansible/ansible.cfg` or define privilege escalation settings in your playbook.

Open the Ansible configuration file:

```bash
sudo vi /etc/ansible/ansible.cfg
```

Locate the `[privilege_escalation]` section and ensure the following settings are configured:

```ini
[privilege_escalation]
become=True
become_method=sudo
become_user=root
become_ask_pass=False
```

This configuration tells Ansible to use `sudo` for privilege escalation, switching to the root user without asking for a password.

### 5. Creating a Playbook for Privileged Tasks

Create a playbook `site.yml` that includes tasks requiring elevated privileges:

```yaml
---
- hosts: managed_nodes
  become: yes
  tasks:
    - name: Install the latest version of Apache
      yum:
        name: httpd
        state: latest
```

Run the playbook:

```bash
ansible-playbook site.yml
```

### Detailed Code Examples

Here is a detailed example of a playbook that not only installs Apache but also ensures that the service is enabled and started:

```yaml
---
- hosts: managed_nodes
  become: yes
  tasks:
    - name: Install the latest version of Apache
      yum:
        name: httpd
        state: latest

    - name: Ensure Apache is enabled and running
      systemd:
        name: httpd
        enabled: yes
        state: started
```

This playbook demonstrates the use of the `systemd` module to manage services on RHEL nodes, encompassing both installation and service management in a privileged context.

## Conclusion

In this tutorial, we covered how to configure privilege escalation on managed nodes in Ansible, focusing on RHEL systems. We went through setting up Ansible, configuring SSH keys for secure communication, and editing Ansible configurations to enable privilege escalation. We also explored creating a playbook that performs privileged tasks on managed nodes.

Understanding and implementing privilege escalation in Ansible is crucial for automating tasks that require administrative privileges securely and efficiently, particularly in a RHEL environment. This knowledge is not only applicable to daily tasks of a systems administrator but also essential for those preparing for the RHCE exam.