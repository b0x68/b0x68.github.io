# Tech Tutorial: Automate Standard RHCSA Tasks using Ansible for Service Management

## Introduction

In this tutorial, we will explore how to automate common Red Hat Certified System Administrator (RHCSA) tasks related to managing services on Linux systems using Ansible. Ansible is a powerful automation tool that simplifies complex configuration, deployment, and orchestration tasks. It is particularly useful for managing services across multiple systems, ensuring consistency and reliability.

We will focus on the manipulation of system services, including starting, stopping, and ensuring the enabled state or disabled state of services on a system managed by systemd.

## Prerequisites

To follow along with this tutorial, you should have:
- Basic understanding of Linux system administration.
- Familiarity with command-line operations and the systemd service manager.
- A working installation of Ansible on a control node (your workstation or a management server).
- One or more managed nodes (servers you wish to automate tasks on), with SSH access configured for Ansible.

## Step-by-Step Guide

In this section, we'll cover how to automate tasks related to system services using Ansible modules such as `systemd` and `service`.

### 1. Setting Up Your Ansible Environment

First, ensure that Ansible is installed on your control node and that you can communicate with your managed nodes via SSH. Here's a quick setup:

```bash
# Install Ansible on a RHEL-based system
sudo yum install ansible

# On Debian-based systems
sudo apt install ansible

# Create or edit your inventory file
nano /etc/ansible/hosts
```

Add your managed nodes under a group in the inventory file:

```ini
[servers]
server1 ansible_host=192.168.1.100
server2 ansible_host=192.168.1.101
```

Test the connectivity:

```bash
ansible all -m ping
```

### 2. Managing Services with Ansible

#### Starting a Service

To ensure a service, e.g., `httpd` (Apache web server), is running on all servers:

```yaml
- hosts: servers
  tasks:
    - name: Ensure Apache is running
      ansible.builtin.systemd:
        name: httpd
        state: started
```

#### Stopping a Service

To stop a service, modify the `state`:

```yaml
- hosts: servers
  tasks:
    - name: Stop Apache service
      ansible.builtin.systemd:
        name: httpd
        state: stopped
```

#### Enabling a Service at Boot

To ensure the service starts on boot:

```yaml
- hosts: servers
  tasks:
    - name: Enable Apache to start at boot
      ansible.builtin.systemd:
        name: httpd
        enabled: yes
```

#### Disabling a Service at Boot

Similarly, to disable a service from starting at boot:

```yaml
- hosts: servers
  tasks:
    - name: Disable Apache from starting at boot
      ansible.builtin.systemd:
        name: httpd
        enabled: no
```

### 3. Handling Service Status

You might want to check the status of a service across multiple nodes. Here’s how you can do that:

```yaml
- hosts: servers
  tasks:
    - name: Check the status of Apache
      ansible.builtin.systemd:
        name: httpd
        state: started
      register: result

    - debug:
        msg: "Status of Apache: {{ result.status }}"
```

### 4. Example Playbook

Combine the tasks to create a playbook:

```yaml
- hosts: servers
  become: yes
  tasks:
    - name: Manage Apache Service
      ansible.builtin.systemd:
        name: httpd
        state: started
        enabled: yes
      register: service_status

    - name: Output the Status
      debug:
        msg: "Apache service state: {{ service_status.state }}"
```

## Conclusion

In this tutorial, we’ve covered how to manage Linux system services using Ansible. By leveraging the `systemd` module, you can automate the process of starting, stopping, enabling, and disabling services across multiple systems efficiently. This ensures that your systems are managed consistently and reduces the risk of human error, making your infrastructure management smoother and more reliable.