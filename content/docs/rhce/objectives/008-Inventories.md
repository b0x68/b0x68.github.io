# Tech Tutorial: Understand Core Components of Ansible - Inventories

## Introduction

In the world of automation and configuration management, Ansible stands out due to its simplicity and ease of use. For Red Hat Certified Engineer (RHCE) exam takers, understanding how Ansible works, particularly its inventory, is crucial. An inventory is essentially a list of nodes or hosts that Ansible manages. It can be defined in a static file (usually a simple text format) or dynamically generated.

This tutorial covers the concept of inventories in Ansible, focusing on the Red Hat Enterprise Linux (RHEL) distribution. We will explore how to define and organize hosts, group them, and specify variables within inventories using practical and real-world examples.

## Step-by-Step Guide

### 1. Setting up Ansible on RHEL

Before diving into inventories, ensure that Ansible is installed on your RHEL system. You can install Ansible using the following YUM command:

```bash
sudo yum install ansible
```

### 2. Understanding the Inventory File

By default, Ansible looks for the inventory file at `/etc/ansible/hosts`. However, you can specify a custom inventory file using the `-i` option with the ansible commands.

An inventory file can be as simple as:

```ini
# /etc/ansible/hosts
192.168.1.50
192.168.1.51
```

This file lists two managed nodes by their IP addresses.

### 3. Grouping Hosts

Organizing hosts into groups can simplify managing multiple servers. Here’s an example of an inventory file with grouped hosts:

```ini
# /etc/ansible/hosts
[webservers]
webserver1.example.com
webserver2.example.com

[dbservers]
dbserver1.example.com
dbserver2.example.com
```

In this example, `webserver1.example.com` and `webserver2.example.com` are grouped under `[webservers]`, and `dbserver1.example.com` and `dbserver2.example.com` are grouped under `[dbservers]`.

### 4. Nested Groups

Ansible also supports nested groups:

```ini
# /etc/ansible/hosts
[webservers]
webserver1.example.com
webserver2.example.com

[dbservers]
dbserver1.example.com
dbserver2.example.com

[linux:children]
webservers
dbservers
```

Here, `[linux:children]` is a supergroup that includes both `[webservers]` and `[dbservers]`.

### 5. Host Variables

You can define variables specific to a host directly in the inventory file:

```ini
# /etc/ansible/hosts
[webservers]
webserver1.example.com http_port=80 max_requests=200
webserver2.example.com http_port=8080 max_requests=100
```

### 6. Group Variables

Similar to host variables, you can define variables for a whole group:

```ini
# /etc/ansible/hosts
[webservers:vars]
http_port=80
max_requests=200
```

This sets `http_port` and `max_requests` for all hosts under the `[webservers]` group.

## Detailed Code Examples

Let’s run a simple command to check the connectivity of all the servers under the `webservers` group:

```bash
ansible webservers -m ping
```

This command uses the `ping` module to ensure that all hosts in the `webservers` group are reachable.

## Conclusion

Understanding and effectively managing inventories is a foundational skill for using Ansible, especially for system administrators aiming for the RHCE certification. The ability to group hosts and define relevant variables allows for scalable and flexible configurations. By mastering inventories, you can streamline the management of numerous systems in a RHEL environment, making your automation tasks more organized and efficient.