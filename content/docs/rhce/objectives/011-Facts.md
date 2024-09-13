# Tech Tutorial: Understand Core Components of Ansible - Facts

## Introduction

Ansible is a powerful automation tool widely used in the IT industry for configuration management, application deployment, task automation, and multi-node orchestration. A key feature of Ansible which enhances its versatility is the use of facts. Facts in Ansible are pieces of information derived from the system it is managing or interacting with. These facts can provide detailed data about the system’s configuration, environment, or state. In this tutorial, we will explore how to gather and utilize facts within Ansible, particularly focusing on Red Hat Enterprise Linux (RHEL) systems, aligning with the Red Hat Certified Engineer (RHCE) exam requirements.

## Step-by-Step Guide

This guide will walk you through understanding, gathering, and using Ansible facts with practical examples.

### Prerequisites

- A working RHEL server setup where Ansible is installed.
- Basic familiarity with YAML syntax and Ansible basics.
- SSH access configured for Ansible to communicate with the managed nodes.

### Step 1: Setting Up Your Inventory

Create an inventory file named `hosts` that defines the RHEL systems you want to manage:

```ini
[rhel-servers]
rhel1 ansible_host=192.168.1.101
rhel2 ansible_host=192.168.1.102
```

### Step 2: Gathering All Facts

Create a playbook named `gather_facts.yml`:

```yaml
---
- name: Gather RHEL Systems Facts
  hosts: rhel-servers
  tasks:
    - name: Collect all facts from the hosts
      ansible.builtin.setup:
```

Run the playbook using the command:

```bash
ansible-playbook -i hosts gather_facts.yml
```

This task uses the `setup` module to gather facts about each host in the `rhel-servers` group.

### Step 3: Filtering Specific Facts

Often, you might not need all facts but just specific ones. Here’s how to gather only certain facts related to networking:

```yaml
---
- name: Gather Network Facts
  hosts: rhel-servers
  tasks:
    - name: Get only network related facts
      ansible.builtin.setup:
        gather_subset: 
          - network
```

### Step 4: Using Facts in Tasks

You can use these facts within tasks to make decisions or configurations dynamically. For instance, creating a conditional task that only runs if the system is RHEL 8:

```yaml
---
- name: Conditional Task Based on OS Version
  hosts: rhel-servers
  tasks:
    - name: Check if the system is RHEL 8
      debug:
        msg: "This is a RHEL 8 system."
      when: ansible_distribution == 'RedHat' and ansible_distribution_major_version == '8'
```

### Step 5: Saving Facts to a File

To save the gathered facts for later use, you can redirect the output to a file:

```bash
ansible rhel-servers -m setup --tree /tmp/facts
```

This will save the facts in JSON format in the `/tmp/facts` directory on your control node.

## Detailed Code Examples

Let's dive deeper with a real-world scenario where facts are crucial. Consider a scenario where you need to ensure that a certain package is only installed on RHEL servers with a specific amount of RAM:

```yaml
---
- name: Ensure a package is installed on high memory machines
  hosts: rhel-servers
  tasks:
    - name: Install package on machines with more than 8GB RAM
      yum:
        name: large-package
        state: present
      when: ansible_memtotal_mb > 8192
```

In this playbook, `ansible_memtotal_mb` is a fact that contains the total memory of the host in MB. The task runs only if the machine has more than 8192 MB of RAM.

## Conclusion

In this tutorial, we explored how to use Ansible facts to gather system information and utilize it to make informed decisions in playbooks. Mastery of facts is essential for effective automation with Ansible, particularly in complex environments. As you prepare for the RHCE exam, understanding and practicing with facts will undoubtedly enhance your ability to design robust and dynamic Ansible playbooks tailored for RHEL systems.