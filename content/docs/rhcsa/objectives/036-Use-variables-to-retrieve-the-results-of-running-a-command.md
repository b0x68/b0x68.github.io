# Tech Tutorial: Create Ansible Plays and Playbooks

## Introduction

Ansible is a powerful automation tool that simplifies complex configuration tasks and consistent IT application environments management. It's widely used for configuration management, deployment, and orchestration. In this tutorial, we will focus on how to utilize Ansible to run commands and retrieve results using variables, a core concept for anyone preparing for the Red Hat Certified Systems Administrator (RHCSA) exam.

Understanding how to efficiently use variables can dramatically streamline your processes and enhance the flexibility of your playbooks. We will use only Red Hat Enterprise Linux (RHEL) commands in adherence to the exam's requirements.

## Step-by-Step Guide

### Setting Up Your Environment

Before diving into the playbook creation, ensure you have the following setup:

1. **Control Node**: A RHEL system with Ansible installed. This is where we will write and run our Ansible playbooks.
2. **Managed Nodes**: One or more RHEL systems that are managed by Ansible. Ensure SSH access and Python installed.

#### Installing Ansible on RHEL

```bash
sudo yum install ansible
```

#### Configuring SSH Access

On your control node, generate an SSH key and copy it to all managed nodes to allow password-less SSH access.

```bash
ssh-keygen -t rsa
ssh-copy-id user@managed-node
```

### Creating Your First Playbook

A playbook in Ansible defines the tasks to be executed on the managed nodes. Let’s create a simple playbook to illustrate how to run a command and use variables to capture its output.

#### Playbook Setup

Create a new file named `capture_output.yml`:

```bash
vi capture_output.yml
```

#### Playbook Content

```yaml
---
- name: Capture command output example
  hosts: all
  tasks:
    - name: Retrieve hostname
      command: hostname
      register: hostname_output

    - name: Display the hostname
      debug:
        msg: "The hostname of the machine is {{ hostname_output.stdout }}"
```

**Explanation:**
- **hosts: all** - Specifies that the playbook should run on all inventory hosts.
- **tasks:** - Begins the tasks list.
- **command: hostname** - Runs the `hostname` command (available in RHEL) on the managed nodes.
- **register: hostname_output** - Saves the output of the command into the variable `hostname_output`.
- **debug:** - Prints a message using the registered variable.

### Running the Playbook

Execute the playbook using the `ansible-playbook` command:

```bash
ansible-playbook capture_output.yml
```

### Detailed Code Examples

Let’s enhance our playbook by incorporating more RHEL-specific commands and capturing their outputs:

```yaml
---
- name: Capture multiple commands output
  hosts: all
  tasks:
    - name: Check disk usage
      command: df -h
      register: disk_usage

    - name: Get current date and time
      command: date
      register: current_date

    - name: Display results
      debug:
        msg: >
          "Disk usage on the machine: {{ disk_usage.stdout }}"
          "Current date and time on the machine: {{ current_date.stdout }}"
```

**Further Explanation:**
- `df -h` and `date` are standard commands in RHEL to check disk usage and current date/time, respectively.
- The results are registered in variables `disk_usage` and `current_date` which are then displayed using the `debug` module.

## Conclusion

In this tutorial, we explored how to create Ansible plays and playbooks specifically tailored for the RHCSA exam using RHEL commands. We learned how to run commands on managed nodes, capture their output using variables, and manipulate this data within our playbooks. Mastery of these skills will not only help in passing the RHCSA exam but also in real-world system administration tasks using Ansible in a Red Hat environment.

This approach to using Ansible enhances scalability and automation in managing a fleet of RHEL systems, making your infrastructure management more efficient and error-resistant.