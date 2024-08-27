# Tech Tutorial: Run Playbooks with Automation Content Navigator

In this tutorial, we'll dive deep into using the Automation Content Navigator to enhance your Ansible capabilities. Specifically, we'll focus on how to find and utilize new modules from available Ansible Content Collections. This is aligned with the exam objective of discovering and implementing new modules using this powerful tool.

## Introduction

Ansible is a popular automation tool used for configuration management, application deployment, and task automation. With the introduction of Ansible Content Collections, it has become easier to manage and disseminate Ansible content. The Automation Content Navigator aids in exploring these collections more efficiently, helping users find specific modules that can be used to extend the functionality of their Ansible playbooks.

## Step-by-Step Guide

### Step 1: Setting Up Your Environment

Before we begin, ensure that Ansible is installed on your machine. You can install Ansible with the following command:

```bash
pip install ansible
```

Also, install the `ansible-navigator` which is a tool to work with Ansible Content Collections:

```bash
pip install ansible-navigator
```

### Step 2: Launching Ansible Navigator

Start the ansible-navigator in the terminal:

```bash
ansible-navigator
```

This command will open a TUI (Text User Interface) that provides a navigational approach to managing your Ansible content.

### Step 3: Exploring Collections

In the ansible-navigator, use the following steps to explore available collections:

1. From the main menu, select `Collections`.
2. This will display a list of available collections. You can browse through or search for specific keywords related to the functionality you need.

For example, if you are looking for modules related to AWS, you might search for `amazon.aws`.

### Step 4: Finding Modules

Once you find a collection of interest, drill down into it:

1. Select the collection by highlighting it and pressing Enter.
2. Choose `Plugins` and then `Modules`. This will list all the modules that are part of the selected collection.

### Step 5: Using a Module in a Playbook

After identifying a module you want to use, you can incorporate it into an Ansible playbook. Here’s a simple example using the `amazon.aws.ec2_instance` module from the `amazon.aws` collection to launch an EC2 instance:

```yaml
---
- name: Launch an EC2 Instance
  hosts: localhost
  gather_facts: false
  collections:
    - amazon.aws

  tasks:
    - name: Create an EC2 instance
      ec2_instance:
        name: MyEC2
        type: t2.micro
        image_id: ami-0c55b159cbfafe1f0
        region: us-east-1
        key_name: my-key
        network:
          assign_public_ip: yes
```

### Step 6: Running the Playbook

Save the playbook as `launch_ec2.yml` and run it using the following command:

```bash
ansible-playbook launch_ec2.yml
```

## Detailed Code Examples

Let's look at another code example where we use a networking module from the `cisco.ios` collection to configure an IOS device:

```yaml
---
- name: Configure Cisco IOS Device
  hosts: routers
  gather_facts: false
  collections:
    - cisco.ios

  tasks:
    - name: Set hostname on the device
      ios_config:
        lines:
          - hostname NewRouterName
```

Here, the `ios_config` module from the `cisco.ios` collection is used to change the hostname of a router.

## Conclusion

The Automation Content Navigator is a crucial tool for Ansible users looking to expand their automation capabilities with new modules from various collections. By following this guide, you should now be able to explore, find, and implement new modules, enhancing your playbooks with a wide range of functionalities. Keep exploring different collections and modules to find the ones that best suit your needs.

Remember, the key to mastering Ansible lies in experimentation and continuous learning. Happy automating!