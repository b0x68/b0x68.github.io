# Tech Tutorial: Create Ansible Plays and Playbooks

## Introduction

Ansible is an open-source automation tool that simplifies cloud provisioning, configuration management, application deployment, intra-service orchestration, and many other IT needs. This tutorial focuses on a specific Ansible capability: using variables to retrieve the results of running a command. This feature is particularly useful for capturing dynamic data from your managed nodes and using it within your playbooks for further tasks.

## Prerequisites

Before proceeding with this tutorial, you should have the following:
- Basic understanding of YAML syntax.
- Ansible installed on your control machine.
- One or more managed nodes (servers) that your control machine can access over SSH.
- Proper SSH key setup for Ansible to communicate with the managed nodes without requiring a password.

## Step-by-Step Guide

### Step 1: Setting Up Your Inventory

Create an inventory file named `hosts` that lists the nodes you want to manage. For example:

```ini
[webservers]
192.168.1.100
192.168.1.101

[dbservers]
192.168.1.110
```

### Step 2: Writing Your First Playbook

Create a file named `check_disk_space.yml`. This playbook will check the disk space on the servers listed under `[webservers]`.

```yaml
---
- name: Check Disk Space
  hosts: webservers
  tasks:
    - name: Get Disk Space
      command: df -h / | tail -n 1 | awk '{print $4}'
      register: disk_space

    - name: Print Disk Space
      debug:
        msg: "Available disk space on {{ inventory_hostname }} is {{ disk_space.stdout }}"
```

### Explanation

- **command**: The `command` module is used to execute commands on a remote node.
- **register**: This keyword is used to store the output of a command into a variable. In this case, `disk_space` is the variable where the output is stored.
- **debug**: The `debug` module is used to print messages to the console.

### Step 3: Running the Playbook

Run the playbook using the following command:

```bash
ansible-playbook -i hosts check_disk_space.yml
```

This command will execute the playbook on the hosts under `[webservers]` as defined in your inventory file.

## Detailed Code Examples

### Example: Checking Service Status

Suppose you want to check if a particular service is running on all servers and report its status. Here’s how you could write the playbook:

```yaml
---
- name: Check Service Status
  hosts: all
  tasks:
    - name: Check status of nginx
      command: systemctl status nginx
      register: service_status

    - name: Print service status
      debug:
        msg: "Status of nginx on {{ inventory_hostname }}: {{ service_status.stdout_lines }}"
```

This playbook will check the status of nginx on all hosts and print the output.

### Example: Extracting Specific Data

If you need to extract specific data from the command output, Ansible's powerful filtering capabilities come into play.

```yaml
---
- name: Get specific package version
  hosts: all
  tasks:
    - name: Get nginx version
      command: nginx -v
      register: nginx_version
      ignore_errors: true

    - name: Parse nginx version
      set_fact:
        nginx_version_extracted: "{{ nginx_version.stderr_lines[0].split(' ')[2] }}"

    - name: Print nginx version
      debug:
        msg: "The nginx version on {{ inventory_hostname }} is {{ nginx_version_extracted }}"
```

## Conclusion

Using variables to store the results of command executions in Ansible is a powerful technique that can significantly enhance your automation tasks. By capturing this dynamic output, you can make your playbooks intelligent and responsive to the state of your managed nodes. Experiment with these examples, and explore how you can integrate them into larger automation workflows to maximize the efficiency and reliability of your IT infrastructure.