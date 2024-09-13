# Tech Tutorial: Understand Core Components of Ansible

## Introduction

Ansible is a powerful automation tool that simplifies configuration management, application deployment, and task automation. It uses a straightforward YAML syntax and connects over SSH without requiring agent installation on the remote systems. This tutorial aims to help you use Ansible's documentation effectively to find information about its modules and commands, focusing specifically on the context of Red Hat Enterprise Linux (RHEL), in preparation for the Red Hat Certified Engineer (RHCE) exam.

## Step-by-Step Guide

### 1. Accessing Ansible Documentation

Before diving into specific commands and modules, it's crucial to understand how to access and use the Ansible documentation. Ansible documentation can be accessed in several ways:

#### Online Documentation

The most comprehensive resource is the [official Ansible documentation site](https://docs.ansible.com/ansible/latest/index.html). This site includes user guides, installation guides, and detailed descriptions of all modules and plugins.

#### Command Line Access

On a RHEL system, after installing Ansible, you can also access documentation from the command line using the `ansible-doc` command. For example, to see information about the `yum` module, you would run:

```bash
ansible-doc yum
```

This command displays usage, parameters, examples, and much more about the `yum` module directly in your terminal.

### 2. Understanding Core Components

Ansible's core components include modules, tasks, plays, playbooks, facts, variables, and inventories. Below, we'll explore how to find information about these components using the `ansible-doc` command.

#### Modules

Modules are the units of work in Ansible. Each module has a specific purpose, such as managing packages with the `yum` module or controlling services with the `systemd` module. To find more about a specific module, use `ansible-doc` followed by the module name. Here's how to look up the `firewalld` module, which is pertinent to managing firewall rules in RHEL:

```bash
ansible-doc firewalld
```

#### Playbooks

Playbooks are the files where Ansible code is written, usually in YAML format. Although `ansible-doc` doesn't provide direct documentation on playbook writing, it can be useful for finding module-specific usage that can be written into playbooks.

### 3. Detailed Code Examples

Let's create a simple playbook that updates all packages on a RHEL system using the `yum` module and then ensures that the `httpd` service is running using the `systemd` module.

```yaml
---
- name: Update all packages and start httpd
  hosts: all
  become: yes

  tasks:
    - name: Ensure all packages are up to date
      yum:
        name: "*"
        state: latest

    - name: Ensure the httpd service is running
      systemd:
        name: httpd
        state: started
        enabled: yes
```

In this example:
- `hosts: all` specifies that the playbook runs on all inventory hosts.
- `become: yes` escalates privileges.
- The `yum` task updates all packages.
- The `systemd` task ensures `httpd` is running and enabled on boot.

### 4. Using `ansible-doc` to Explore More Examples

For more real-world examples, use the `-s` flag with `ansible-doc` to show playbook snippets. For instance:

```bash
ansible-doc -s yum
```

This command will show you how to use the `yum` module within a playbook context.

## Conclusion

Understanding how to navigate and utilize the Ansible documentation is crucial for effective automation with Ansible, especially in professional environments like those managed under RHEL policies. This tutorial has introduced how to access module and command documentation with `ansible-doc`, and provided a simple playbook example. As you prepare for the RHCE exam, make frequent use of `ansible-doc` to familiarize yourself with the modules and options available in Ansible, ensuring you're well-prepared for practical automation challenges.