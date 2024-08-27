# Tech Tutorial: Understand Core Components of Ansible - Handling Task Failure

## Introduction

Ansible is a powerful automation tool that simplifies complex tasks and streamlines IT operations. One of the critical aspects of managing automation scripts is handling task failures gracefully. In this tutorial, we'll explore how to effectively manage and respond to failures in Ansible tasks. This knowledge is crucial for maintaining the reliability and robustness of your automation workflows.

## Step-by-Step Guide

### 1. Understanding Error Handling in Ansible

Ansible provides several mechanisms to handle errors during playbook execution. These include `ignore_errors`, `failed_when`, `rescue` blocks in blocks, and more. We'll go through each of these mechanisms with detailed examples.

### 2. Setup Your Environment

Before we dive into the examples, ensure you have Ansible installed on your system. You can install Ansible on most Linux distributions using the package manager or `pip`.

```bash
sudo apt update
sudo apt install ansible
```

Or using pip:

```bash
pip install ansible
```

### 3. Basic Error Handling: `ignore_errors`

Sometimes, you might want to ignore errors from a task and continue with the rest of the playbook. The `ignore_errors` directive allows you to do this.

**Example:**

```yaml
- name: Example of ignoring errors
  hosts: all
  tasks:
    - name: Try to read a non-existent file
      command: cat /path/to/nonexistent/file
      ignore_errors: true
    - name: Print a message
      debug:
        msg: "This task will be executed even if the previous task fails."
```

### 4. Conditional Failure: `failed_when`

`failed_when` allows you to define custom conditions under which a task should be considered failed.

**Example:**

```yaml
- name: Example of conditional failure
  hosts: all
  tasks:
    - name: Check disk usage
      command: df -H | grep /dev/sda1
      register: disk_usage
      failed_when: "'90%' in disk_usage.stdout"
```

This task checks the disk usage and fails if the output includes '90%', indicating the disk is nearly full.

### 5. Using Blocks for Exception Handling

Blocks allow you to group tasks and handle errors more efficiently using `rescue` and `always` sections.

**Example:**

```yaml
- name: Handle errors with blocks
  hosts: all
  tasks:
    - block:
        - name: Attempt to start a service
          systemd:
            name: myservice
            state: started
      rescue:
        - name: Send an alert mail
          mail:
            to: admin@example.com
            subject: Service start failed
            body: Starting the service failed on {{ inventory_hostname }}
      always:
        - name: Execute this regardless of success or failure
          debug:
            msg: "This is a cleanup step"
```

### 6. Retrying Tasks

Sometimes, especially in cases of intermittent issues (like network latency), you might want to retry a task a few times before considering it a failure.

**Example:**

```yaml
- name: Retry task example
  hosts: all
  tasks:
    - name: Attempt to connect to a host
      command: ping -c 1 example.com
      register: result
      until: result.rc == 0
      retries: 5
      delay: 2
```

This task will retry pinging `example.com` up to 5 times with a delay of 2 seconds between retries.

## Conclusion

In this tutorial, we explored various ways to handle task failures in Ansible. By using `ignore_errors`, `failed_when`, handling exceptions with blocks, and retrying tasks, you can make your Ansible playbooks more robust and reliable. Effective error handling is crucial for smooth automation and can save time and resources in long-term operations. Practice these strategies in your playbooks to enhance their performance and fault tolerance.

Happy automating with Ansible!