# Tech Tutorial: Configure Ansible Managed Nodes

## Introduction

In this tutorial, we will focus on an essential skill for the Red Hat Certified Engineer (RHCE) exam: analyzing simple shell scripts and converting them to Ansible playbooks. Ansible is a popular automation tool used for configuration management, application deployment, and task automation. By converting shell scripts into Ansible playbooks, you can leverage Ansible’s idempotency and manage configurations more efficiently across multiple systems.

## Step-by-Step Guide

### Prerequisites

- A Control Node: A Red Hat Enterprise Linux (RHEL) system with Ansible installed.
- One or more Managed Nodes: RHEL systems that are managed by the control node.

Ensure SSH access from the control node to the managed nodes using key-based authentication for seamless operation.

### Analyzing a Shell Script

Suppose we have a basic shell script that installs Apache, starts the service, and ensures it runs on boot:

```bash
#!/bin/bash
yum install -y httpd
systemctl start httpd.service
systemctl enable httpd.service
```

Our goal is to convert this script into an Ansible playbook.

### Creating the Ansible Playbook

1. **Create the Inventory File**

First, list your managed nodes in an inventory file (`hosts.ini`):

```ini
[webservers]
server1.example.com
server2.example.com
```

2. **Write the Playbook**

Create a file named `install_httpd.yml`:

```yaml
---
- name: Install and start Apache
  hosts: webservers
  become: yes
  tasks:
  - name: Install Apache
    yum:
      name: httpd
      state: present

  - name: Ensure Apache is running and enabled
    systemd:
      name: httpd
      state: started
      enabled: yes
```

### Explanation of the Playbook

- `hosts: webservers`: Specifies the group of hosts from the inventory file.
- `become: yes`: Escalates privileges (equivalent to `sudo`).
- `yum`: The module for installing packages. `state: present` ensures the package is installed.
- `systemd`: Manages the service state. Ensures Apache (`httpd`) is started and enabled on boot.

### Running the Playbook

Execute the playbook using the ansible-playbook command:

```bash
ansible-playbook -i hosts.ini install_httpd.yml
```

This command initiates the playbook, connecting to the specified hosts in `hosts.ini` and executing the defined tasks.

## Detailed Code Examples

Let's expand our playbook to include more tasks, such as setting up a basic HTML page:

```yaml
---
- name: Configure Apache web servers
  hosts: webservers
  become: yes
  tasks:
  - name: Install Apache
    yum:
      name: httpd
      state: present

  - name: Start and enable Apache
    systemd:
      name: httpd
      state: started
      enabled: yes

  - name: Deploy a custom index page
    copy:
      content: "<html><body><h1>Welcome to our server!</h1></body></html>"
      dest: /var/www/html/index.html
      owner: root
      group: root
      mode: '0644'
```

This additional task (`Deploy a custom index page`) uses the `copy` module to create a simple HTML page, setting appropriate file permissions and ownership.

## Conclusion

Converting shell scripts to Ansible playbooks can streamline and standardize system configurations across multiple nodes while taking advantage of Ansible's powerful features such as idempotency and easy scalability. This tutorial covered the basic conversion of a script that installs and manages Apache on RHEL systems, but the principles can be applied to more complex scripts and diverse scenarios within the RHCE exam scope and beyond. With practice, you can efficiently convert and optimize scripts to enhance your automation strategies with Ansible.