# Tech Tutorial: Create Ansible Plays and Playbooks

## Introduction

In the realm of automation, Ansible is a powerful tool that simplifies complex configuration management, application deployment, and task automation. For those preparing for the Red Hat Certified Engineer (RHCE) exam, understanding how to effectively use Ansible conditionals to control play execution is crucial. This tutorial will guide you through the process of using conditionals in Ansible, specifically tailored for Red Hat Enterprise Linux (RHEL) environments.

## Step-by-Step Guide

### Prerequisites

Before diving into the tutorial, ensure that you have the following setup:

1. **RHEL 8** or later installed on at least two machines (one as an Ansible control node and the others as managed nodes).
2. **Ansible installed** on the control node. You can install Ansible using the following command:
   ```bash
   sudo dnf install ansible
   ```
3. **SSH access** set up between the control node and the managed nodes. 

### Setting Up Your Inventory File

Create an Ansible inventory file named `hosts`:
```ini
[webservers]
webserver1 ansible_host=192.168.1.101
webserver2 ansible_host=192.168.1.102

[dbservers]
dbserver1 ansible_host=192.168.1.201
```

### Creating Your First Playbook with Conditionals

We'll create a playbook that demonstrates how to use conditionals to control task execution based on certain criteria.

#### Scenario

Suppose you want to ensure that a package called `httpd` (Apache HTTP Server) is installed on all web servers but only start the service on machines that do not already have it running.

#### Step 1: Creating the Playbook

Create a file named `webserver-setup.yml`:

```yaml
---
- name: Ensure httpd is installed and started
  hosts: webservers
  become: yes

  tasks:
  - name: Install httpd
    yum:
      name: httpd
      state: present

  - name: Check if httpd is running
    command: systemctl is-active httpd
    register: httpd_status
    ignore_errors: true

  - name: Start httpd service if not running
    service:
      name: httpd
      state: started
    when: httpd_status.stdout != "active"
```

#### Explanation

1. **Task 1: Install httpd** - This task uses the `yum` module to ensure the `httpd` package is installed.
2. **Task 2: Check if httpd is running** - We run a command to check if the `httpd` service is active and register the output in the variable `httpd_status`. The `ignore_errors: true` is used to ensure the playbook does not fail if the service is not found.
3. **Task 3: Start httpd service if not running** - This task starts the `httpd` service only if it is not already active, as determined by the `when` conditional.

### Running the Playbook

To run the playbook, use the following command on your control node:
```bash
ansible-playbook -i hosts webserver-setup.yml
```

## Detailed Code Examples

Let's delve a bit deeper with more complex conditionals.

### Example: Ensuring a Specific Kernel Version

Suppose you want to ensure that your servers are running a specific kernel version before deploying an application that depends on this version.

Create a playbook named `check-kernel-version.yml`:

```yaml
---
- name: Check and report kernel version
  hosts: all
  become: yes

  tasks:
    - name: Get kernel version
      command: uname -r
      register: kernel_version

    - name: Print warning if kernel version is not 4.18.0-240.el8
      debug:
        msg: "WARNING: Kernel version is not 4.18.0-240.el8, please update."
      when: kernel_version.stdout != "4.18.0-240.el8"
```

This playbook will print a warning message if the kernel version does not match the required version.

## Conclusion

Using conditionals in Ansible allows for more dynamic and context-sensitive automation tasks. By employing conditionals, you can make your automation processes more efficient and error-resistant, ensuring that actions are only taken when appropriate. This is a critical skill for anyone aspiring to become a Red Hat Certified Engineer, as it enables robust and adaptable configuration management in RHEL environments.