+++
title = "Start and stop services and configure services to start automatically at boot"
date = "2024-02-16T11:49:52-05:00"
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


# Tutorial: Starting and Stopping Services and Configuring Automatic Start on Boot

## Introduction

The Red Hat Certified Systems Administrator (RHCSA) exam is a performance-based certification exam that focuses on the skills required to perform essential system administration tasks on Red Hat Enterprise Linux (RHEL) systems. Objective 200 of the exam specifically covers the topic of starting and stopping services, as well as configuring services to start automatically at boot. In this tutorial, we will provide a step-by-step guide on how to complete this objective in great depth.

## Understanding Services and Daemons

Before we dive into the specific tasks of starting and stopping services and configuring them for automatic start, it is important to have a basic understanding of what services and daemons are in a Linux system. Services, also known as system services or daemons, are background processes responsible for performing various tasks on a Linux system. These services can include network services, web servers, logging services, and many others.

Daemons are similar to services in the sense that they are also background processes that perform various tasks. The main difference is that daemons are typically long-running processes that continuously operate in the background, while services are usually started and stopped on demand.

## Starting and Stopping Services

### Checking for Active Services

Before starting or stopping any services, it is important to determine which services are currently active on your system. To do this, you can use the `systemctl` command, which is the primary tool used for managing services in RHEL systems. To check the status of all running services, use the following command:

`systemctl list-units --type=service --all`

This will output a list of all services on your system, along with their current status (active, inactive, or failed).

### Starting a Service

To start a service on your system, you can use the `systemctl start` command, followed by the name of the service. For example, to start the Apache web server service, you would use the following command:

`systemctl start httpd`

This will start the service immediately and output a success message if successful. 

### Stopping a Service

Similarly, to stop a service, you can use the `systemctl stop` command, followed by the name of the service. For example, to stop the SSH service, you would use the following command:

`systemctl stop sshd`

This will stop the service immediately and output a success message if successful.

## Configuring Automatic Start on Boot

In some cases, you may want a service to start automatically every time your system boots up. This can be achieved by configuring the service to start on boot, using the `systemctl enable` command.

### Enabling Automatic Start

To enable automatic start for a service, simply use the `systemctl enable` command, followed by the name of the service. For example, to enable the MariaDB database service, you would use the following command:

`systemctl enable mariadb`

This will create a symbolic link for the service in the appropriate `/etc/systemd/system` directory, and the service will now start automatically on boot.

### Disabling Automatic Start

If you no longer want a service to start automatically on boot, you can disable it using the `systemctl disable` command. For example, to disable the Nginx web server service, you would use the following command:

`systemctl disable nginx`

This will remove the symbolic link for the service in the `/etc/systemd/system` directory, and the service will no longer start automatically on boot.

## Conclusion

In this tutorial, we have covered the basics of starting and stopping services in a Red Hat Enterprise Linux system, as well as configuring services for automatic start on boot. Remember, it is important to have a good understanding of the services and daemons on your system before attempting to manage them. By following the steps outlined in this tutorial, you should be well-prepared to complete Objective 200 of the RHCSA exam. 