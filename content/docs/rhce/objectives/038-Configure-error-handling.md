# Tech Tutorial: Create Ansible Plays and Playbooks for Error Handling

## Introduction

Ansible is a powerful tool for automation in IT systems, and one of its key features in managing operations is its robust error handling capabilities. Understanding how to configure error handling in Ansible is crucial for ensuring that your automation tasks can gracefully recover or respond appropriately when something goes wrong. In this tutorial, we'll explore how to effectively manage errors in Ansible plays and playbooks, specifically focusing on Red Hat Enterprise Linux (RHEL)-compatible configurations, as required for the Red Hat Certified Engineer (RHCE) exam.

## Step-by-Step Guide

### Prerequisites

To follow this tutorial, you will need:
- A RHEL system (version 7 or 8) set up with network access.
- Ansible installed on your RHEL system. You can install it using `sudo yum install ansible`.
- SSH access configured for the managed nodes from the control node.

### Basic Playbook Structure

Before diving into error handling, let's review the basic structure of an Ansible playbook. A playbook is composed of one or more "plays," which target specific hosts and define tasks to be executed on those hosts.

Here is a simple example of a playbook:

```yaml
---
- name: Example Playbook
  hosts: all
  tasks:
    - name: Check if a file exists
      ansible.builtin.stat:
        path: /etc/redhat-release
      register: result

    - name: Print the result
      debug:
        msg: "File exists!"
      when: result.stat.exists
```

### Configuring Error Handling

#### Ignoring Errors

Sometimes, you may want to continue executing a playbook even if a task fails. You can achieve this by using the `ignore_errors` directive.

Example:

```yaml
---
- name: Ignore Error Example
  hosts: all
  tasks:
    - name: Attempt to read a non-existent file
      ansible.builtin.command: cat /nonexistentfile
      ignore_errors: yes

    - name: Print a message
      debug:
        msg: "This task will run even if the previous task fails."
```

In this example, even if the command to read the non-existent file fails, the playbook will not stop execution because of the `ignore_errors: yes` setting.

#### Using Block and Rescue

A more sophisticated method of handling errors in Ansible is to use `block` and `rescue` sections. This is analogous to `try/catch` in many programming languages.

Example:

```yaml
---
- name: Block and Rescue Example
  hosts: all
  tasks:
    - block:
        - name: Attempt to start a service
          ansible.builtin.service:
            name: httpd
            state: started
      rescue:
        - name: Send an alert mail
          ansible.builtin.mail:
            host: smtp.example.com
            subject: "Service failed to start"
            body: "Failed to start HTTPD service on {{ inventory_hostname }}"
            to: admin@example.com
            from: ansible@example.com

      always:
        - name: Always do this
          debug:
            msg: "This task always runs, regardless of previous errors."
```

Here, if starting the `httpd` service fails, the tasks in the `rescue` section will execute. The `always` section is optional and, if used, will run after the block/rescue sections regardless of whether there was an error or not.

## Detailed Code Examples

In a real-world scenario, error handling becomes crucial, especially when dealing with critical services or operations. Let's consider a scenario where you are tasked with deploying updates across multiple servers.

```yaml
---
- name: Update and Restart Services
  hosts: webservers
  tasks:
    - block:
        - name: Update all packages
          yum:
            name: '*'
            state: latest
        - name: Restart the network service
          service:
            name: network
            state: restarted
      rescue:
        - name: Send failure notification
          ansible.builtin.mail:
            host: smtp.yourcompany.com
            subject: "Failed to update on {{ inventory_hostname }}"
            body: "The update process failed on {{ inventory_hostname }}"
            to: sysadmin@yourcompany.com
            from: ansible@yourcompany.com
      always:
        - name: Check disk space
          ansible.builtin.shell: df -h
          register: disk_space
        - name: Display disk space
          debug:
            var: disk_space.stdout_lines
```

This playbook ensures that all servers are updated, the network service is restarted, and adequate disk space is checked post-operation, with appropriate notifications sent on failures.

## Conclusion

Effective error handling in Ansible is essential for building reliable and resilient automation scripts. By using `ignore_errors`, `block`, `rescue`, and `always`, you can ensure that your playbooks handle unexpected situations gracefully and keep your systems running smoothly. As you prepare for the RHCE exam, mastering these techniques will be invaluable in demonstrating your competency in using Ansible for real-world system administration in RHEL environments.