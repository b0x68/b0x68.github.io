+++
title = "Set enforcing and permissive modes for SELinux"
date = "2024-02-16T10:37:49-05:00"
author = "root"
cover = ""
tags = ["systems", "service", "files", "permissions.", "selinux,", "selinux.", "command", "`etc/selinux/config`,"]
keywords = ["system.", "(security-enhanced", "`selinux=`", "/etc/selinux/config", "configuration", "command", "logged", "selinux."]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Setting Enforcing and Permissive Modes for SELinux

SELinux (Security-Enhanced Linux) is a security feature in Linux systems that enforces mandatory access control policies. It provides an additional layer of protection by restricting access to certain resources based on user roles and permissions. In this tutorial, we will discuss how to set enforcing and permissive modes for SELinux, one of the objectives for the Red Hat Certified Systems Administrator Exam.

## Prerequisites

Before we begin, make sure you have the following:
- A Red Hat Enterprise Linux system
- Root access or sudo privileges
- Basic understanding of SELinux and its policies

## Understanding Enforcing and Permissive Modes

SELinux has three different modes - enforcing, permissive, and disabled. In enforcing mode, SELinux actively enforces its security policies and denies access to any unauthorized resource. In permissive mode, all the actions that would normally be denied in enforcing mode are logged but allowed to continue. This mode is mainly used for troubleshooting purposes, as it allows you to identify which actions are being denied by SELinux. In disabled mode, SELinux is completely turned off and has no effect on system security.

Now, let's dive into the steps to set enforcing and permissive modes for SELinux.

## Setting Enforcing Mode

1. Log in to your system as root or with a sudo user.
2. Open the configuration file for SELinux, `etc/selinux/config`, using a text editor. For example, you can use the `nano` editor by running the following command:
```
nano /etc/selinux/config
```
3. Locate the line that says `SELINUX=` and change its value from `disabled` to `enforcing`.
4. Save the changes and exit the text editor.
5. Reboot your system for the changes to take effect.

Upon reboot, SELinux will be in enforcing mode. All the policies will be actively enforced, and any unauthorized action will be denied.

## Setting Permissive Mode

1. Log in to your system as root or with a sudo user.
2. Open the configuration file for SELinux, `etc/selinux/config`, using a text editor. For example, you can use the `nano` editor by running the following command:
```
nano /etc/selinux/config
```
3. Locate the line that says `SELINUX=` and change its value from `disabled` to `permissive`.
4. Save the changes and exit the text editor.
5. Reboot your system for the changes to take effect.

After reboot, SELinux will be in permissive mode. All actions that would normally be denied in enforcing mode will be logged but allowed to continue. This mode is useful for troubleshooting SELinux-related issues.

## Checking the Current Mode

To verify the current mode of SELinux, you can use the `sestatus` command. It will display information about the current status, including the mode and the enforced policies. Running this command after setting enforcing or permissive mode will show the changes you made.

## Applying Modes Only for Specific Services

You can also set enforcing or permissive mode for specific services only, rather than for the entire system. This can be useful when testing SELinux policies for a particular service.

1. Log in to your system as root or with a sudo user.
2. Use the `semanage` command to view the current mode settings for all the services:
```
semanage boolean -l
```
3. Locate the service for which you want to change the mode and take note of its name.
4. Use the `semanage` command with the `-i` option to change the mode for that service. For example, to change the mode for the HTTPD service, you would use the following command:
```
semanage boolean -i -m <desired_mode> -1 httpd_can_network_connect
```
Here, `<desired_mode>` represents either `enforcing` or `permissive`. The `-m` option specifies the mode, and the `-1` option applies it to the specified service. Note that this command works for built-in SELinux policies only. For custom policies, you will have to modify the policy files manually.

## Conclusion

In this tutorial, we have discussed the process of setting enforcing and permissive modes for SELinux. We have covered the importance of these modes and how to apply them to the entire system or specific services. Understanding and effectively utilizing these modes is crucial for managing SELinux policies and maintaining system security. Be sure to practice and familiarize yourself with these concepts properly, as they are essential for passing the Red Hat Certified Systems Administrator Exam.