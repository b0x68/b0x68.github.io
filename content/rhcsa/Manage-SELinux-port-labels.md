+++
title = "Manage SELinux port labels"
date = "2024-02-16T11:53:34-05:00"
author = "root"
cover = ""
tags = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
keywords = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Tutorial: Managing SELinux Port Labels

## Introduction
Welcome to our tutorial on managing SELinux port labels! This tutorial will provide you with a step-by-step guide on how to effectively manage SELinux port labels. The ability to manage SELinux port labels is an important skill for any Red Hat Certified Systems Administrator, as it allows you to control access to network services and protect your system from potential attacks.

## Prerequisites
Before we begin, make sure you have the following:
- A Red Hat Certified Systems Administrator Exam 200 level knowledge on SELinux
- A Red Hat Enterprise Linux system
- Root access or sudo privileges

## Understanding SELinux
SELinux (Security-Enhanced Linux) is a security mechanism implemented in the Linux Kernel that provides an access control system for enforcing mandatory access controls on processes and users. It adds an additional layer of security to your system by limiting the access of programs and processes to only the specific resources they need.

One of the ways SELinux achieves this is through the use of port labels. Port labels are attached to network ports and determine which applications are allowed to communicate through those ports. By managing SELinux port labels, you can control which programs and services have access to specific network ports.

## Step 1: Check SELinux Status
Before we start managing SELinux port labels, it's important to check the status of SELinux on your system. To do this, run the following command:

```
sestatus
```

If SELinux is enabled, you will see the following output:

```
SELinux status: enabled
```

If SELinux is disabled, you will see the following output:

```
SELinux status: disabled
```

If SELinux is disabled, you will need to enable it before you can proceed with managing port labels. This can be done by modifying the SELinux configuration file located at `/etc/selinux/config`.

## Step 2: List All Current Port Labels
To view the current port labels on your system, run the following command:

```
semanage port -l
```

This will list all the current port labels and their associated protocols, types, and contexts. It will also indicate whether the port is currently allowed or blocked by SELinux.

## Step 3: Adding a New Port Label
To add a new port label, you will need to use the `semanage` tool. This tool allows you to manage SELinux policy modules. Here's the syntax for adding a new port label:

```
semanage port -a -t <type> [-p <protocol>] <port>
```

- `-a` indicates that we want to add a new port label
- `-t` specifies the type of the port
- `-p` (optional) specifies the protocol of the port (if not specified, it will default to `tcp`)
- `<port>` the port number you want to add

For example, to add a new port label for SSH (port 22) using the TCP protocol, we would run the following command:

```
semanage port -a -t ssh_port_t -p tcp 22
```

## Step 4: Modifying an Existing Port Label
If you need to modify an existing port label, you can use the `semanage` too as well. Here's the syntax for modifying an existing port label:

```
semanage port -m -t <new_type> [-p <new_protocol>] <port>
```

- `-m` indicates that we want to modify an existing port label
- `-t` specifies the new type of the port
- `-p` (optional) specifies the new protocol of the port (if not specified, it will default to the existing protocol)
- `<port>` the port number you want to modify

For example, to change the type of the SSH port label to `http_port_t`, we would run the following command:

```
semanage port -m -t http_port_t 22
```

## Step 5: Deleting a Port Label
If you no longer need a port label, you can delete it using the `semanage` tool. Here's the syntax for deleting a port label:

```
semanage port -d -p <protocol> <port>
```

- `-d` indicates that we want to delete a port label
- `-p` specifies the protocol of the port
- `<port>` the port number of the label you want to delete

For example, to delete the port label for SSH (port 22), we would run the following command:

```
semanage port -d -p tcp 22
```

## Step 6: Checking if Port Label Changes Persist After Reboot
After making any changes to port labels, it's important to check if they persist after a system reboot. To do this, simply reboot your system and then run the `semanage port -l` command again to see if your changes are still in effect.

## Conclusion
Congratulations! You have successfully learned how to manage SELinux port labels. By using the `semanage` tool, you can easily add, modify, and delete port labels to control access to network ports and enhance the security of your system. Managing port labels is an essential skill for any Red Hat Certified Systems Administrator, and we hope this tutorial has provided you with a thorough understanding of how to do it effectively. 