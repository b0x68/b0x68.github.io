# Tech Tutorial: Understand Core Components of Ansible - Loops

**Exam Objective:** Loops

## Introduction

In this tutorial, we will delve into an essential aspect of Ansible, one of the most popular automation tools used in systems administration and DevOps - **Loops**. Specifically designed for the Red Hat Certified Engineer (RHCE) exam, this guide will focus entirely on practical, real-world examples using Red Hat Enterprise Linux (RHEL) as the primary operating system.

Loops in Ansible are powerful constructs that allow you to repeat a particular task multiple times. This can be beneficial when you need to manage a series of resources similarly or apply a configuration across multiple items.

## Step-by-Step Guide

### 1. Setting Up Your Environment

Before diving into the Ansible loops, ensure you have an Ansible control node and one or more managed nodes running RHEL. Here’s a quick setup:

- **Control Node:** A RHEL system with Ansible installed.
- **Managed Nodes:** One or more RHEL systems that you will manage with Ansible.

Install Ansible on the control node using the following command:

```bash
sudo dnf install ansible
```

Ensure SSH access from the control node to the managed nodes for seamless automation.

### 2. Understanding Basic Loop Structure

The simplest form of a loop in Ansible uses the `loop` keyword. Let's start with a basic example:

#### Example: Create Multiple Users

Create a new playbook named `create_users.yml`.

```yaml
---
- name: Create multiple users
  hosts: all
  tasks:
    - name: Ensure users are present
      user:
        name: "{{ item }}"
        state: present
      loop:
        - alice
        - bob
        - carol
```

This playbook loops over the list provided under the `loop` keyword and creates users on the target machines.

### 3. Advanced Loop Examples

#### Using `with_items`

This is another way to implement loops, which is very similar to `loop` but specific to certain modules.

```yaml
---
- name: Install multiple packages
  hosts: all
  tasks:
    - name: Ensure packages are installed
      yum:
        name: "{{ item }}"
        state: present
      with_items:
        - httpd
        - vim
        - tree
```

This playbook installs multiple packages on RHEL systems using the `yum` module.

#### Looping Over Hashes/Dictionaries

When you need to loop over a dictionary, you can use the `dict2items` filter.

```yaml
---
- name: Add several users with attributes
  hosts: all
  vars:
    users:
      alice:
        uid: 1001
        shell: /bin/bash
      bob:
        uid: 1002
        shell: /bin/zsh
  tasks:
    - name: Ensure users with attributes are present
      user:
        name: "{{ item.key }}"
        uid: "{{ item.value.uid }}"
        shell: "{{ item.value.shell }}"
        state: present
      loop: "{{ lookup('dict', users).items() }}"
```

This playbook creates users with specific `uid` and `shell` attributes, demonstrating how to handle more complex data structures.

### 4. Error Handling in Loops

You can manage errors within loops using the `ignore_errors` directive or by handling failures more gracefully with `rescue` blocks in blocks.

```yaml
---
- name: Attempt to execute potentially failing commands
  hosts: all
  tasks:
    - block:
        - command: "{{ item }}"
          loop:
            - 'echo "This will succeed"'
            - 'exit 1'  # This command will fail
      rescue:
        - debug:
            msg: "A command failed, but we're moving on!"
```

## Conclusion

In this tutorial, we explored the essential aspects of using loops in Ansible, focusing on practical examples tailored for RHEL as required for the RHCE exam. Mastery of loops enhances your ability to write more dynamic and efficient playbooks, significantly reducing code redundancy and making your automation tasks more manageable and scalable. As you prepare for the exam, practice these examples and experiment with variations to deepen your understanding of Ansible's capabilities.