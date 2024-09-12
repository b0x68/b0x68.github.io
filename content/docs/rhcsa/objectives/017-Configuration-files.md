# Tech Tutorial: Understand Core Components of Ansible - Configuration Files

## Introduction

In the realm of IT automation, Ansible stands out due to its simplicity and flexibility. This tutorial focuses on one of the fundamental aspects of Ansible critical for the Red Hat Certified Systems Administrator (RHCSA) exam: **Configuration Files**. Understanding how to efficiently configure Ansible will enhance your ability to manage a network of computers for automated deployment and daily operations.

Ansible configuration files are pivotal in tailoring the behavior of Ansible to meet specific operational needs. By the end of this tutorial, you should have a solid understanding of how to manipulate these files to optimize your Ansible setup.

## Prerequisites

Before diving into the details of Ansible configuration files, ensure you have the following setup on a Red Hat Enterprise Linux (RHEL) system:

- **Ansible installed** on at least one RHEL machine (which will act as the control node).
- **SSH access** configured for the control node to communicate with other RHEL nodes (which will act as managed nodes).

## Step-by-Step Guide

### 1. Locating the Ansible Configuration File

Ansible looks for the configuration file in the following order:

1. `ANSIBLE_CONFIG` (an environment variable pointing to a configuration file)
2. `ansible.cfg` in the current directory
3. `.ansible.cfg` in the home directory
4. `/etc/ansible/ansible.cfg`

You can verify which configuration file is being used by Ansible using the following command:

```bash
ansible --version
```

This command outputs several lines, one of which indicates the used configuration file:

```
config file = /etc/ansible/ansible.cfg
```

### 2. Understanding the Structure of the Configuration File

The configuration file is in INI format. Here's an example of how sections and key-value pairs are typically organized:

```ini
[defaults]
inventory = /etc/ansible/hosts
remote_user = ansible
host_key_checking = False
retry_files_enabled = False

[privilege_escalation]
become = True
become_method = sudo
become_user = root
become_ask_pass = False
```

Each section (e.g., `[defaults]`, `[privilege_escalation]`) contains specific configuration directives.

### 3. Editing the Configuration File

To edit the configuration file, use a text editor like `vi`:

```bash
sudo vi /etc/ansible/ansible.cfg
```

#### Example Modifications:

- **Change the default inventory file path:**

  ```ini
  [defaults]
  inventory = /path/to/your/custom/inventory
  ```

- **Disable host key checking** to avoid SSH key confirmation prompts. This is useful for automating tasks across many new hosts:

  ```ini
  [defaults]
  host_key_checking = False
  ```

### 4. Setting Environment Variables

Instead of directly modifying the configuration file, you can override settings using environment variables. For instance, to change the inventory file location temporarily, you can use:

```bash
export ANSIBLE_INVENTORY=/path/to/new/inventory
```

To make these changes permanent, add them to your bash profile:

```bash
echo 'export ANSIBLE_INVENTORY=/path/to/new/inventory' >> ~/.bash_profile
source ~/.bash_profile
```

## Detailed Code Examples

Let's consider a practical scenario where we need to deploy a web server on multiple RHEL nodes using Ansible:

**Step 1**: Create an inventory file at `/etc/ansible/hosts`:

```ini
[webservers]
web1 ansible_host=192.168.1.101
web2 ansible_host=192.168.1.102
```

**Step 2**: Write a playbook named `deploy_webserver.yml`:

```yaml
---
- name: Deploy Apache Web Server
  hosts: webservers
  become: yes

  tasks:
  - name: Install Apache
    yum:
      name: httpd
      state: present

  - name: Start Apache
    service:
      name: httpd
      state: started
      enabled: yes
```

**Step 3**: Run the playbook:

```bash
ansible-playbook deploy_webserver.yml
```

## Conclusion

In this tutorial, we explored the essentials of Ansible's configuration files which are crucial for tailoring Ansible to specific environments. By understanding and manipulating these files, you can achieve more efficient and controlled automation processes. As you prepare for the RHCSA exam, practice modifying and leveraging these files to deepen your understanding and proficiency in managing RHEL systems with Ansible.