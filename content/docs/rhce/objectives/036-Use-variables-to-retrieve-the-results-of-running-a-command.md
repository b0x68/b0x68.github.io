# Tech Tutorial: Create Ansible Plays and Playbooks Using Variables to Retrieve the Results of Running a Command

## Introduction

Ansible is a powerful automation tool that simplifies configuration management, application deployment, and many other administrative tasks. In this tutorial, we will focus on a specific aspect of Ansible relevant to the Red Hat Certified Engineer (RHCE) exam: using variables to retrieve the results of running a command. This capability is crucial for creating dynamic and responsive playbooks that adapt based on the state of the system or the output of prior tasks.

## Step-by-Step Guide

### Prerequisites

- A Red Hat Enterprise Linux (RHEL) system (version 8 or later recommended).
- Ansible installed on your control node (the system from which you will run Ansible commands).
- SSH access configured for a target node (another RHEL system) where commands will be executed.

### Setting Up Your Environment

1. **Install Ansible on RHEL**: If Ansible is not already installed on your RHEL system, you can install it using the following command:

   ```bash
   sudo dnf install ansible -y
   ```

2. **Configure SSH Access**: Ensure you have SSH access set up for the user that will run Ansible on your control node to your target node. This usually involves setting up SSH keys and ensuring the public key is in the `~/.ssh/authorized_keys` file on the target node.

3. **Test Ansible Connectivity**:
   
   Create an inventory file named `hosts`:

   ```ini
   [servers]
   server1 ansible_host=target_node_ip ansible_user=remote_user
   ```

   Replace `target_node_ip` with the IP address of your target node and `remote_user` with the user that will run Ansible commands.

   Test the connection using:

   ```bash
   ansible all -i hosts -m ping
   ```

### Creating the Playbook

Now, let's create a playbook that runs a command on the target node and uses a variable to store the result.

1. **Create the Playbook File**:

   Create a file named `check_disk.yml`:

   ```yaml
   ---
   - name: Check disk space on a target node
     hosts: servers
     tasks:
       - name: Get disk space usage
         command: df -h /home
         register: disk_space

       - name: Print disk space usage
         debug:
           msg: "Disk space on /home: {{ disk_space.stdout }}"
   ```

   In this playbook:
   - The `command` module runs `df -h /home` on the target node to check the disk space usage of the `/home` directory.
   - The `register` keyword saves the output of the command to the `disk_space` variable.
   - The `debug` module prints the output stored in `disk_space.stdout`.

### Running the Playbook

Execute the playbook using the following command:

```bash
ansible-playbook -i hosts check_disk.yml
```

This command runs your playbook using the inventory file `hosts` which specifies the target node details.

## Detailed Code Examples

Let’s dive deeper into some variations and real-world scenarios where capturing command output can be crucial.

### Checking Service Status

Suppose you want to check the status of a service and perform an action based on its status. Here's how you can do it:

```yaml
---
- name: Check and report service status
  hosts: servers
  tasks:
    - name: Check status of crond service
      command: systemctl status crond
      register: service_status
      ignore_errors: yes

    - name: Print service status
      debug:
        msg: "Service status: {{ service_status.stdout }}"
```

### Conclusion

Using variables to capture the output of commands in Ansible allows you to make decisions and perform actions based on the state of your systems dynamically. This approach is integral to writing flexible and efficient automation scripts, particularly in complex IT environments like those managed under RHCE standards. By mastering this skill, you enhance your ability to manage Red Hat systems effectively and prepare yourself for scenarios you may encounter in the RHCE exam and real-world tasks.

Keep experimenting with different modules and exploring Ansible's extensive documentation to further your understanding and expertise.