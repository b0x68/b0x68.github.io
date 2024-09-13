# Tech Tutorial: Understanding Conditional Tasks in Ansible

Ansible is a powerful automation tool that simplifies complex configuration management, application deployment, and task automation. It is especially popular in Red Hat environments, given its integration and support for Red Hat Enterprise Linux (RHEL). In this tutorial, we will focus specifically on executing conditional tasks in Ansible, which is a crucial component for the Red Hat Certified Engineer (RHCE) exam.

## Introduction

Conditional tasks in Ansible allow you to execute tasks based on certain conditions. This feature is extremely useful when you need to perform tasks on certain hosts but not others, or when certain steps in your playbook depend on the outcomes of previous steps.

## Step-by-Step Guide

### 1. Setting Up Your Environment

Before diving into conditional tasks, ensure you have Ansible installed on your RHEL system. You can install Ansible on RHEL by enabling the Red Hat Subscription Management (RHSM) repository that includes Ansible and then installing it using `yum`.

```bash
sudo subscription-manager repos --enable ansible-2-for-rhel-8-x86_64-rpms
sudo yum install ansible
```

Verify the installation by checking the version of Ansible:

```bash
ansible --version
```

### 2. Writing Your First Conditional Playbook

Let’s start with a simple example. We'll create a playbook that installs `httpd` only if it is not already installed on the system.

Create a new playbook file named `conditional_httpd.yml`:

```yaml
---
- name: Conditional httpd installation
  hosts: all
  tasks:
    - name: Check if httpd is installed
      command: rpm -q httpd
      register: httpd_installed
      ignore_errors: true

    - name: Install httpd if not installed
      yum:
        name: httpd
        state: present
      when: httpd_installed.rc != 0
```

### 3. Understanding the Playbook

- **Task 1: Check if httpd is installed**
  - We use the `command` module to check if the `httpd` package is installed.
  - The `register` directive saves the result of the command in the variable `httpd_installed`.
  - `ignore_errors: true` ensures that the playbook does not stop if the command indicates that `httpd` is not installed.

- **Task 2: Install httpd if not installed**
  - The `yum` module is used to ensure `httpd` is present.
  - The `when` condition checks the return code of the previous command (`httpd_installed.rc`). If the return code is not `0`, it means `httpd` is not installed, and hence the task will execute.

### 4. Running Your Playbook

Run the playbook against your target hosts (ensure your hosts are defined in your Ansible inventory):

```bash
ansible-playbook -i your_inventory_file conditional_httpd.yml
```

### 5. Expanding Conditional Tasks

You can use Ansible facts and other conditions to control the flow of execution. For example, you might want to perform tasks based on the operating system, checking disk space, or whether a certain file exists.

```yaml
- name: Conditional task based on OS and disk space
  hosts: all
  tasks:
    - name: Check disk space
      command: df -h / | grep / | awk '{ print $4 }'
      register: disk_space

    - name: Install tool on RHEL if sufficient disk space
      yum:
        name: some_tool
        state: present
      when:
        - ansible_distribution == 'RedHat'
        - disk_space.stdout | regex_search('(\d+)(G)') | int > 10
```

## Conclusion

Conditional tasks in Ansible allow for dynamic and context-sensitive automation scripts, making them more efficient and intelligent. By leveraging conditions, you can ensure that your automation logic adapts to the environment it runs in, reducing errors and unnecessary operations. This capability is not only powerful for daily operations but also essential for those preparing for the RHCE exam, where understanding and applying such concepts can be pivotal.

Feel free to experiment with different conditions and scenarios to better understand how Ansible behaves and how it can be tailored to meet your specific automation needs.