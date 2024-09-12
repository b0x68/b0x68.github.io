# Tech Tutorial: Create Ansible Plays and Playbooks with Error Handling

## Introduction

In this tutorial, we will delve into how to configure error handling in Ansible plays and playbooks, an essential skill for anyone preparing for the Red Hat Certified System Administrator (RHCSA) exam. Error handling in Ansible is crucial for creating robust automation scripts that can gracefully handle unexpected situations and maintain the integrity of systems, particularly in a Red Hat Enterprise Linux (RHEL) environment.

## Step-by-Step Guide

### 1. Understanding Error Handling in Ansible

Error handling in Ansible is managed primarily through the use of blocks and rescue sections. These constructs allow you to attempt a series of tasks and define actions to take if those tasks fail. This is similar to try-except blocks in many programming languages.

### 2. Setting Up Your Environment

Before creating the playbook, ensure that Ansible is installed on your RHEL system. You can install Ansible using the following YUM command:

```bash
sudo yum install ansible
```

Make sure Ansible is installed by checking its version:

```bash
ansible --version
```

### 3. Creating a Basic Playbook

Let's start by creating a simple playbook called `example_playbook.yml`. This playbook will attempt to start a service on a remote RHEL system.

```yaml
---
- name: Start a service on a remote host
  hosts: all
  tasks:
    - name: Start httpd service
      ansible.builtin.systemd:
        name: httpd
        state: started
```

### 4. Introducing Error Handling

Now, let’s add error handling to the playbook. We will use a `block` to attempt to start the service and a `rescue` section to respond to any errors that occur.

```yaml
---
- name: Start a service with error handling
  hosts: all
  tasks:
    - name: Attempt to start httpd service
      block:
        - name: Start httpd
          ansible.builtin.systemd:
            name: httpd
            state: started
      rescue:
        - name: Send failure notification
          ansible.builtin.debug:
            msg: "Failed to start httpd service"
```

In this example, if the task to start the httpd service fails, Ansible will execute the `rescue` section and print a failure message.

### 5. Adding More Complexity

Error handling can also include multiple rescue actions, and even notifications sent through other means, such as email. Here’s how you could enhance the playbook:

```yaml
---
- name: Start a service with advanced error handling
  hosts: all
  tasks:
    - name: Attempt to start and verify httpd service
      block:
        - name: Start httpd
          ansible.builtin.systemd:
            name: httpd
            state: started
        - name: Verify httpd is running
          ansible.builtin.command: systemctl status httpd
          register: result
          failed_when: "'active (running)' not in result.stdout"
      rescue:
        - name: Send failure notification
          ansible.builtin.mail:
            host: smtp.example.com
            subject: Failed to start httpd on {{ inventory_hostname }}
            body: Here is what went wrong: {{ ansible_failed_result }}
            to: admin@example.com
            from: ansible@example.com
```

In this enhanced example, we have added a verification step after starting the service. If the service is not running, or if any step in the block fails, the playbook sends an email notification.

## Conclusion

Effective error handling in Ansible is vital for maintaining the reliability and stability of systems, especially in a controlled environment like RHEL. By using blocks and rescue sections, you can ensure that your playbooks can handle unexpected errors gracefully and keep system administrators informed of any issues that need attention. This approach is not only beneficial for passing the RHCSA exam but also for real-world system administration tasks.

Keep experimenting with different scenarios and error handling strategies to improve your playbooks' resilience and reliability.