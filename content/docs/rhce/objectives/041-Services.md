# Tech Tutorial: Automate Standard RHCSA Tasks Using Ansible for Managing Services

## Introduction

In this tutorial, we will explore how to automate service management tasks on Red Hat Enterprise Linux (RHEL) systems using Ansible. This is particularly relevant for those preparing for the Red Hat Certified Engineer (RHCE) exam, which includes objectives related to managing services. Ansible is a powerful automation tool that can simplify the process of configuring and maintaining servers.

We will cover how to use Ansible to start, stop, restart, and check the status of services on RHEL servers. By the end of this tutorial, you will have a solid understanding of how to manage services efficiently using Ansible modules specifically designed for this purpose.

## Prerequisites

Before diving into the tutorial, ensure you have the following setup:
- One or more RHEL 8 systems to serve as Ansible hosts.
- Ansible installed on a control node (which could also be a RHEL system).
- SSH access configured from the control node to the host systems.
- Sudo privileges on the host systems for the user used by Ansible.

## Step-by-Step Guide

### Step 1: Setting Up Your Inventory File

First, create an inventory file that lists the RHEL servers you want to manage. Here is a basic example of what the inventory file might look like:

```ini
[rhel-servers]
server1.example.com
server2.example.com
```

### Step 2: Writing Your Ansible Playbook

An Ansible playbook is a YAML file where you define tasks, which include the actions you want to automate on your hosts. Save the following examples as `service_management.yml`.

#### Example 1: Ensuring a Service is Started

To ensure that a service (e.g., `httpd`) is running on all servers, use the `ansible.builtin.systemd` module:

```yaml
---
- name: Ensure the HTTPD service is running
  hosts: rhel-servers
  become: yes
  tasks:
    - name: Start httpd service
      ansible.builtin.systemd:
        name: httpd
        state: started
        enabled: yes
```

#### Example 2: Stopping a Service

To stop a service, modify the `state` to `stopped`. Here's how you could stop the `httpd` service:

```yaml
---
- name: Stop the HTTPD service
  hosts: rhel-servers
  become: yes
  tasks:
    - name: Stop httpd service
      ansible.builtin.systemd:
        name: httpd
        state: stopped
```

#### Example 3: Restarting a Service

To restart a service, use `restarted` as the state. This is useful for applying new configurations:

```yaml
---
- name: Restart the HTTPD service
  hosts: rhel-servers
  become: yes
  tasks:
    - name: Restart httpd service
      ansible.builtin.systemd:
        name: httpd
        state: restarted
```

#### Example 4: Checking the Status of a Service

To check the status of a service, you can register the result of the systemd module and display it using the `debug` module:

```yaml
---
- name: Check the status of the HTTPD service
  hosts: rhel-servers
  become: yes
  tasks:
    - name: Check httpd service status
      ansible.builtin.systemd:
        name: httpd
        state: started
      register: result

    - name: Print service status
      ansible.builtin.debug:
        msg: "The HTTPD service status is {{ result.status }}"
```

### Step 3: Running Your Playbook

Execute your playbook using the `ansible-playbook` command:

```bash
ansible-playbook service_management.yml
```

## Conclusion

In this tutorial, you've learned how to manage RHEL services using Ansible. By automating service management tasks, you can ensure consistency across multiple systems and reduce the potential for human error. This knowledge will not only help you in your RHCE exam preparation but also in real-world RHEL system administration.

Feel free to expand upon these examples by integrating them into larger playbooks that manage more complex configurations. Automation with Ansible is a powerful skill for any system administrator, particularly in environments that adhere to DevOps methodologies.