# Tech Tutorial: Understand Core Components of Ansible - Conditional Tasks

## Introduction

In the realm of automation, Ansible stands out for its simplicity and scalability, which is especially true when managing configurations and deployments across multiple systems. One of the powerful features of Ansible is its ability to execute tasks conditionally. Conditional tasks in Ansible allow you to control the flow of execution based on the state of the system or the results of previous tasks. This capability is crucial for creating dynamic and responsive playbooks that adapt to diverse environments and scenarios.

In this tutorial, we will delve deep into conditional tasks in Ansible, focusing on their practical applications within a Red Hat Enterprise Linux (RHEL) environment. This is particularly relevant for those preparing for the Red Hat Certified System Administrator (RHCSA) exam.

## Step-by-Step Guide

### 1. Setting Up Your Environment

Before we dive into the conditional tasks, ensure that you have Ansible installed on your RHEL system. You can install Ansible using the following command:

```bash
sudo yum install ansible
```

Verify the installation by checking the Ansible version:

```bash
ansible --version
```

### 2. Understanding Ansible Playbooks

An Ansible playbook is a YAML file where you define what actions you want Ansible to perform. It is here that you will specify your conditional tasks. Let's start by creating a simple playbook:

```yaml
---
- hosts: all
  tasks:
    - name: Check if a file exists
      ansible.builtin.stat:
        path: /etc/redhat-release
      register: result

    - name: Display a message if the file exists
      ansible.builtin.debug:
        msg: "File exists."
      when: result.stat.exists
```

### 3. Writing Conditional Tasks

Conditional tasks in Ansible are primarily handled using the `when` statement. This statement can evaluate any valid Python expression. Let's explore more complex conditions.

#### Example: Checking Multiple Conditions

Suppose you want to execute a task only if multiple conditions are satisfied. You can use logical operators like `and`, `or`, and `not`:

```yaml
---
- hosts: all
  tasks:
    - name: Install httpd only on RHEL 8 and if it's not already installed
      ansible.builtin.yum:
        name: httpd
        state: present
      when: ansible_facts.distribution == 'RedHat' and ansible_facts.distribution_major_version == '8' and not ansible_facts.services["httpd.service"]
```

#### Example: Conditional Failures

You can also have tasks that fail based on a condition. This is useful for assertions or compliance checks:

```yaml
---
- hosts: all
  tasks:
    - name: Ensure that SELinux is set to enforcing mode
      ansible.builtin.command: getenforce
      register: selinux_status
      failed_when: selinux_status.stdout != "Enforcing"
```

### 4. Using Conditionals with Loops

Ansible allows conditionals to be used alongside loops. Here’s how you can conditionally execute tasks within a loop:

```yaml
---
- hosts: all
  vars:
    packages:
      - httpd
      - nginx
      - git
  tasks:
    - name: Install selected packages
      ansible.builtin.yum:
        name: "{{ item }}"
        state: present
      loop: "{{ packages }}"
      when: ansible_facts.distribution == 'RedHat'
```

## Conclusion

Conditional tasks are a cornerstone of writing effective and efficient Ansible playbooks. They allow you to tailor task execution to the specific circumstances of each target node, enhancing both the flexibility and the power of your automation efforts. By mastering conditional tasks, you can ensure that your playbooks can handle a wide variety of scenarios, making your infrastructure automation more robust and adaptive.

Remember, practice is key, especially for exam preparation like the RHCSA. Try to experiment with different conditions and scenarios to deepen your understanding of Ansible's capabilities within a RHEL environment. Happy automating!