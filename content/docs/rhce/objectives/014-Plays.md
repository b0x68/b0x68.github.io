# Tech Tutorial: Understanding Plays in Ansible

## Introduction

In the landscape of IT automation, Ansible stands out due to its simplicity and versatility. For Red Hat Certified Engineer (RHCE) exam candidates, mastering the concept of "plays" in Ansible is crucial. Plays are the core building blocks of any Ansible playbook. They define a series of tasks that are executed on defined hosts, using selected variables and handlers. In this tutorial, we'll dive deep into understanding and creating plays in Ansible, specifically focusing on examples applicable to Red Hat Enterprise Linux (RHEL).

## Step-by-Step Guide

### Prerequisites

To follow along with this tutorial, you need:
- A RHEL server (physical or virtual) for testing.
- Ansible installed on a control node, which could also be your RHEL server.

#### Install Ansible on RHEL

To install Ansible on RHEL, you can use the following command:

```bash
sudo yum install ansible -y
```

### Understanding Plays

A "play" in an Ansible playbook is a collection of tasks that are executed sequentially on a particular set of hosts. Each play must specify:
- Which hosts to target.
- What tasks to run.

### Creating a Basic Play

Let's start by creating a simple playbook that includes one play. The play will install Apache (`httpd`) on a RHEL server.

1. Create a file named `install_apache.yml`:

```yaml
---
- name: Install Apache Web Server
  hosts: webservers
  become: yes
  tasks:
    - name: Ensure Apache is installed
      yum:
        name: httpd
        state: present
```

### Explanation

- `---` indicates the beginning of a YAML file.
- `name:` gives a descriptive name to the play.
- `hosts:` specifies on which hosts the tasks should be run. In this case, it's a group called `webservers`.
- `become: yes` tells Ansible to use privilege escalation (sudo by default) to execute tasks.
- `tasks:` is a list of tasks to be executed.

Each task in the list has a `name:` and uses a module (`yum` in this case) with parameters (`name: httpd` and `state: present`).

### Running the Playbook

Before running the playbook, you must define the `webservers` group in your inventory file (typically `/etc/ansible/hosts`):

```ini
[webservers]
192.168.1.10
192.168.1.20
```

Now execute the playbook using the ansible-playbook command:

```bash
ansible-playbook install_apache.yml
```

### Detailed Code Examples

#### Adding Multiple Tasks

You can add more tasks to the same play. Let's extend the previous playbook to start and enable the `httpd` service:

```yaml
---
- name: Install Apache Web Server
  hosts: webservers
  become: yes
  tasks:
    - name: Ensure Apache is installed
      yum:
        name: httpd
        state: present

    - name: Ensure Apache is running and enabled
      systemd:
        name: httpd
        state: started
        enabled: yes
```

#### Using Handlers

Handlers are tasks that run at the end of a play if notified by another task. Let's modify the playbook to use a handler to restart Apache if it's already installed but not running:

```yaml
---
- name: Install Apache Web Server
  hosts: webservers
  become: yes
  tasks:
    - name: Ensure Apache is installed
      yum:
        name: httpd
        state: present
      notify:
       - restart apache

  handlers:
    - name: restart apache
      systemd:
        name: httpd
        state: restarted
        enabled: yes
```

## Conclusion

Understanding plays in Ansible is fundamental for automating tasks across multiple systems efficiently. This tutorial covered the basics of creating and running plays, adding multiple tasks, and using handlers to manage services like Apache on RHEL systems. Mastery of these concepts is essential for the RHCE exam and will significantly aid in managing real-world infrastructure projects using Ansible.