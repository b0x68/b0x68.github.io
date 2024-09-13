# Tech Tutorial: Understanding Core Components of Ansible - Roles

Ansible is a powerful automation tool that simplifies complex configuration tasks and consistent IT application environments management. One of the fundamental building blocks in Ansible is the concept of "Roles". Roles allow for the organization of tasks, variables, files, and templates into a coherent structure that can be reused and shared.

## Introduction to Ansible Roles

Roles in Ansible are essentially sets of variables, tasks, files, and handlers that are organized in a predefined file structure. Using roles, you can break down your playbooks into reusable components that can be used across different projects or within different parts of the same project. This not only enhances the readability and maintainability of your Ansible code but also promotes the reuse of code.

### Benefits of Using Roles:

1. **Modularity**: Encapsulate logic and abstract complexity.
2. **Reusability**: Use the same role in multiple playbooks.
3. **Simplicity**: Manage tasks in smaller chunks that are easier to understand.
4. **Shareability**: Share roles across teams or through Ansible Galaxy, the Ansible roles repository.

## Step-by-Step Guide to Creating and Using an Ansible Role

### Step 1: Setting Up Your Environment

Ensure you have Ansible installed on your Red Hat Enterprise Linux system. You can install Ansible using YUM:

```bash
sudo yum install ansible
```

### Step 2: Creating a Role

Ansible roles have a standard directory structure. To create a role named `httpd`, you can use the `ansible-galaxy` command, which is the simplest way to get started:

```bash
ansible-galaxy init httpd
```

This command creates the following structure in the `httpd` directory:

```
httpd/
├── defaults
│   └── main.yml
├── files
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── README.md
├── tasks
│   └── main.yml
├── templates
└── vars
    └── main.yml
```

### Step 3: Populating the Role

Edit the files within the role directory to define tasks, variables, handlers, etc.

#### **tasks/main.yml**

```yaml
---
# tasks file for httpd
- name: Install httpd
  yum:
    name: httpd
    state: present

- name: Ensure httpd is running
  service:
    name: httpd
    state: started
    enabled: yes
```

#### **handlers/main.yml**

```yaml
---
# handlers file for httpd
- name: restart httpd
  service:
    name: httpd
    state: restarted
```

### Step 4: Using the Role in a Playbook

Create a playbook `site.yml` that uses the `httpd` role:

```yaml
---
- hosts: all
  become: yes
  roles:
    - httpd
```

### Step 5: Running Your Playbook

Run your playbook using the ansible-playbook command:

```bash
ansible-playbook site.yml
```

## Detailed Code Examples

To provide a more complex example, suppose you want to deploy a web application where you need to install `httpd`, copy a web app's files, and ensure the service is running.

**Adding tasks to `tasks/main.yml` in the `httpd` role:**

```yaml
---
- name: Install httpd
  yum:
    name: httpd
    state: present

- name: Copy web application files
  copy:
    src: "{{ playbook_dir }}/files/my_web_app"
    dest: /var/www/html

- name: Ensure httpd is running
  service:
    name: httpd
    state: started
    enabled: yes
```

**Using the role in `site.yml`:**

```yaml
---
- hosts: web_servers
  become: yes
  roles:
    - httpd
```

## Conclusion

Ansible roles are a vital part of Ansible's playbooks that help in managing complex IT infrastructures with ease. By breaking down tasks into smaller, reusable components, roles enable sysadmins and DevOps professionals to write cleaner and more maintainable Ansible scripts. Remember, roles can be shared and reused across different teams and projects, increasing efficiency and standardization.

In your journey to becoming proficient with Ansible and preparing for the Red Hat Certified Engineer exam, mastering roles will provide a strong foundation for developing robust automation environments.