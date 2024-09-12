# Tech Tutorial: Understand Core Components of Ansible - Variables

### Introduction

Ansible is a powerful automation tool that simplifies complex configuration tasks and system administration activities. A key feature of Ansible that enhances its flexibility and usability is the use of variables. In this tutorial, we'll explore how to utilize variables effectively within Ansible, specifically targeting Red Hat Enterprise Linux (RHEL), which is critical for those preparing for the Red Hat Certified System Administrator (RHCSA) exam.

### Step-by-Step Guide

#### 1. Understanding Variables in Ansible

Variables in Ansible are essentially values that can change depending on the context. They are used to manage differences between systems, environments, or any other changeable data. In Ansible, variables can be defined in various places including in inventory files, playbook files, included files, and roles.

#### 2. Defining Variables

Variables can be defined in several ways within Ansible:

- **Inventory Variables:** These are set in the inventory file and typically used to define information specific to hosts.
- **Playbook Variables:** Defined at the playbook level and are generally applicable to all tasks in the playbook.
- **Role Variables:** These variables are specific to roles, allowing reusability and customization of roles.

#### 3. Using Variables in Playbooks

To effectively use variables within your playbooks, you need to understand how to define, call, and manage them in different scenarios.

### Detailed Code Examples

#### Example 1: Defining Variables in an Inventory File

Create an inventory file named `hosts`:

```ini
[webservers]
webserver1 ansible_host=192.168.1.101 ansible_user=root example_variable="Hello from Webserver 1"

[dbservers]
dbserver1 ansible_host=192.168.1.102 ansible_user=root example_variable="Hello from DB Server 1"
```

#### Example 2: Using Variables in a Playbook

Create a simple playbook named `example_playbook.yml`:

```yaml
---
- hosts: all
  tasks:
    - name: Print a variable
      debug:
        msg: "{{ example_variable }}"
```

Run the playbook:

```bash
ansible-playbook -i hosts example_playbook.yml
```

This playbook will print the `example_variable` value for each host defined in the inventory.

#### Example 3: Role Variables

Create a role structure using:

```bash
ansible-galaxy init myrole
```

Inside the role directory `myrole/vars/main.yml`, define some variables:

```yaml
app_path: "/opt/myapp"
app_user: "appuser"
```

Use these variables in your tasks within the role:

```yaml
---
# tasks file for myrole
- name: Ensure application directory exists
  file:
    path: "{{ app_path }}"
    state: directory
    owner: "{{ app_user }}"
    mode: '0755'
```

#### Example 4: Prompting for Variables

Modify `example_playbook.yml` to prompt for a variable:

```yaml
---
- hosts: all
  vars_prompt:
    - name: "user_input"
      prompt: "Enter a value"
      private: no

  tasks:
    - name: Print user input
      debug:
        msg: "User entered {{ user_input }}"
```

### Conclusion

Variables in Ansible are a fundamental aspect that provides flexibility and reusability in your automation scripts. By mastering variables, you enhance your ability to create dynamic and scalable automation solutions, particularly within RHEL environments. This knowledge is crucial for the RHCSA exam and practical system administration tasks.

Remember, the key to mastering Ansible variables lies in understanding where and how to define them based on your specific requirements and ensuring they are used consistently and appropriately across your playbooks and roles.