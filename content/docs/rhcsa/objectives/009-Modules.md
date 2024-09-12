# Tech Tutorial: Understand Core Components of Ansible - Modules

Ansible, a powerful IT automation tool, simplifies complex configuration tasks, ensures consistency across large environments, and automates the deployment of applications. It’s agentless, relying on the existing SSH infrastructure which makes it easy to deploy. Moreover, it uses a simple language, YAML, in the form of Ansible Playbooks to describe automation jobs.

## Exam Objective: Modules

One of the core components of Ansible are modules. Modules are the units of work in Ansible. Each module is a piece of code for accomplishing a specific task. Essentially, when you run a playbook, Ansible finds the tasks in it, then finds the corresponding modules for those tasks, and executes them.

### Introduction

In this tutorial, we will delve into how to use Ansible modules effectively with practical examples on Red Hat Enterprise Linux (RHEL). We'll cover some commonly used modules and provide detailed code examples to help you understand how to integrate them into your playbooks.

### Prerequisites

- A RHEL server set up with Ansible installed.
- Basic knowledge of YAML and Ansible terminology.

### Step-by-Step Guide

#### Step 1: Setting Up Your Environment

Before we proceed, ensure that Ansible is installed on your RHEL system. You can install Ansible with the following command:

```bash
sudo yum install ansible
```

Verify the installation:

```bash
ansible --version
```

#### Step 2: Understanding Basic Modules

Let's start by exploring some basic but powerful Ansible modules:

1. **ping**: Tests connectivity and that Ansible can log in to the managed hosts.
2. **command**: Executes a command on a remote node.
3. **shell**: Executes commands in nodes via shell.
4. **copy**: Copies files from the local machine to a remote node.
5. **yum**: Manages packages with the `yum` package manager, ensuring that they are installed, updated, or removed.

#### Step 3: Detailed Code Examples

##### Example 1: Checking Connectivity with `ping` Module

Create a simple playbook to check the connectivity of your managed hosts.

```yaml
---
- name: Test Connectivity
  hosts: all
  tasks:
    - name: Ping test
      ping:
```

Run the playbook using:

```bash
ansible-playbook test_ping.yml
```

##### Example 2: Using the `command` Module

Let's say you want to check the disk usage on your remote RHEL servers.

```yaml
---
- name: Check Disk Usage
  hosts: all
  tasks:
    - name: Check disk space
      command: df -h
      register: disk_space

    - name: Print disk space
      debug:
        msg: "{{ disk_space.stdout_lines }}"
```

##### Example 3: Installing a Package with `yum` Module

This example playbook will ensure that the "tree" package is installed on all your RHEL hosts.

```yaml
---
- name: Ensure the tree package is installed
  hosts: all
  tasks:
    - name: Install tree
      yum:
        name: tree
        state: present
```

#### Step 4: Putting It All Together

Now, let’s create a playbook that combines different tasks, utilizing various modules:

```yaml
---
- name: Comprehensive Example
  hosts: all
  become: yes
  tasks:
    - name: Install vim
      yum:
        name: vim
        state: present

    - name: Create a directory
      file:
        path: /example_directory
        state: directory

    - name: Copy a file
      copy:
        src: /localpath/sample.txt
        dest: /example_directory/sample.txt
```

### Conclusion

Modules are the foundation of Ansible's functionality, enabling a wide range of tasks from simple pings to complex configurations and deployments. By mastering modules, you can automate almost any aspect of your system configurations and application deployments in a RHEL environment.

Remember, the key to effective Ansible playbook writing is understanding the parameters each module accepts and the context in which it operates. Continuously explore the extensive library of modules provided by Ansible to expand your automation capabilities.

Happy automating!