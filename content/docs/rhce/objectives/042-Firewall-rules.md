# Tech Tutorial: Automate Standard RHCSA Tasks Using Ansible for Firewall Rules

## Introduction

In this tutorial, we'll explore how to automate the management of firewall rules using Ansible. This is particularly relevant for those preparing for the RHCSA exam, where proficiency in firewall management is crucial. Ansible provides a powerful, yet simple, automation tool that can handle complex tasks with ease. By the end of this guide, you will have a solid understanding of how to use Ansible modules to automate firewall configurations on a Linux system.

## Prerequisites

Before diving into the tutorial, ensure that you have the following:

- A working Linux environment (CentOS/RHEL 7 or 8)
- Ansible installed on a control node (your workstation or a management server)
- SSH access to one or more managed nodes
- Sudo privileges on the managed nodes

## Step-by-Step Guide

### Step 1: Install Required Packages

First, ensure that `firewalld` is installed and running on your managed nodes. You can use Ansible to ensure these prerequisites are met:

```yaml
---
- name: Ensure firewalld is installed and running
  hosts: all
  become: yes
  tasks:
    - name: Install firewalld
      yum:
        name: firewalld
        state: present

    - name: Start and enable firewalld
      service:
        name: firewalld
        state: started
        enabled: yes
```

Save this as `firewalld-setup.yml` and run it using the `ansible-playbook` command.

### Step 2: Opening a Service Port

To manage firewall rules, we'll use the `firewalld` Ansible module. Here’s how to open HTTP and HTTPS ports across your managed nodes:

```yaml
---
- name: Open HTTP and HTTPS ports
  hosts: webservers
  become: yes
  tasks:
    - name: Open HTTP port
      firewalld:
        service: http
        permanent: yes
        state: enabled
        immediate: yes

    - name: Open HTTPS port
      firewalld:
        service: https
        permanent: yes
        state: enabled
        immediate: yes
```

This playbook targets hosts under the `webservers` group and modifies the firewall rules to allow HTTP and HTTPS traffic.

### Step 3: Adding a Custom Firewall Rule

Sometimes, you might need to add a custom rule, for example, allowing access to a specific port from a certain IP address:

```yaml
---
- name: Allow access to port 8080 from specific IP
  hosts: application_servers
  become: yes
  tasks:
    - name: Allow access from specific IP to a custom port
      firewalld:
        rich_rule: 'rule family="ipv4" source address="192.168.1.100" port port="8080" protocol="tcp" accept'
        permanent: yes
        state: enabled
        immediate: yes
```

This playbook will apply a more specific rule to the hosts under `application_servers`.

### Step 4: Blocking an IP Address

To block an IP address using `firewalld`:

```yaml
---
- name: Block an IP address
  hosts: all_servers
  become: yes
  tasks:
    - name: Block IP address
      firewalld:
        rich_rule: 'rule family="ipv4" source address="10.10.10.10" drop'
        permanent: yes
        state: enabled
        immediate: yes
```

This playbook applies a firewall rule that drops all traffic from the specified IP address.

## Conclusion

Automating firewall rules with Ansible not only simplifies the process but also ensures consistency across your infrastructure. This tutorial covered the basics of using the `firewalld` module in Ansible to manage firewall rules, including opening ports, adding custom rules, and blocking specific IP addresses. By leveraging Ansible's idempotent properties, you can run these playbooks multiple times without worrying about creating duplicate rules. This makes Ansible an excellent choice for managing firewall settings in a dynamic and scalable environment.

Remember, the key to mastering Ansible automation is practice and experimentation. Try adapting the examples given to fit different scenarios and explore further the capabilities of Ansible in managing other system configurations.