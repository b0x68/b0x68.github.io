+++
title = "Restrict network access using firewall-cmd/firewall"
date = "2024-02-16T11:51:48-05:00"
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
 

# Tutorial: Restricting Network Access using firewall-cmd/firewall

In this tutorial, we will be discussing the Red Hat Certified Systems Administrator Exam 200 Objective: "Restrict network access using firewall-cmd/firewall." We will go through the process of setting up and using the firewall-cmd and firewall tools to restrict network access and secure your system.

## What is firewall-cmd/firewall?

firewall-cmd and firewall are command line tools used to manage firewalls in Linux systems, specifically in Red Hat Enterprise Linux (RHEL). These tools provide administrators with a flexible and powerful way to control network traffic and secure their system by defining rules and policies.

## Prerequisites

Before beginning this tutorial, you will need:

- A system running Red Hat Enterprise Linux
- root or sudo privileges
- Basic knowledge of command line interface (CLI)

## Setting Up firewall-cmd/firewall

1. First, make sure you have the latest version of firewalld package installed on your system. You can check this by running the following command:

`firewall-cmd --version`

2. If you don't have the package installed, run the following command to install it:

`sudo yum install firewalld`

3. Once the package is installed, start the firewalld service and enable it to start on boot by running the following commands:

`sudo systemctl start firewalld`<br>
`sudo systemctl enable firewalld`

4. Verify that the service is running by using the following command:

`firewall-cmd --state`

This should return a message stating that the service is running.

## Understanding Zones and Default Policies

In firewalld, zones are predefined sets of rules that control how traffic is allowed or blocked in a specific network or interface. There are several built-in zones in firewalld, such as public, home, internal, and external. Each zone has its own set of rules and policies.

Before we start adding rules, it's important to understand the default policies for the zones. By default, firewalld has its `default_zone` set to `public`, and the default policy for this zone is `DROP` (meaning all incoming connections are blocked). To check your default zone, run the following command:

`firewall-cmd --get-default-zone`

To check the default policy for your current default zone, run:

`firewall-cmd --zone=<zone> --get-default`

## Managing Zones and Rules

Now that we have a basic understanding of zones and policies, let's dive into managing them using firewall-cmd and firewall tools.

### Adding and Removing Zones

To add a new zone, we can use the `--new-zone` option with firewall-cmd. For example, to add a zone named `secure` to our firewall, we can run the following command:

`sudo firewall-cmd --permanent --new-zone=secure`

The `--permanent` option ensures that the change is saved and will persist after a reboot. 

To remove a zone, use the `--delete-zone` option:

`sudo firewall-cmd --permanent --delete-zone=secure`

### Assigning Interfaces to Zones

Now that we have added a new zone, we need to assign an interface to it. This is done using the `--zone` and `--change-zone` options. For example, if we want to assign the `eth0` interface to our `secure` zone, we can run:

`sudo firewall-cmd --zone=secure --change-interface=eth0`

### Adding Rules to Zones

Once we have our zones set up and interfaces assigned, we can add rules to allow or deny traffic in our desired zone. This is done using the `--add-rich-rule` option and specifying the zone we want to add the rule to. For example, to allow incoming SSH connections in our `secure` zone, we can run the following command:

`sudo firewall-cmd --zone=secure --add-rich-rule='rule family="ipv4" source address="192.168.1.2" port port="22" protocol="tcp" accept'`

This command adds a rich rule that allows incoming SSH connections from the IP `192.168.1.2` on port 22 using TCP protocol.

To block a specific IP address in our `public` zone, we can use the `drop` action instead:

`sudo firewall-cmd --zone=public --add-rich-rule='rule family="ipv4" source address="125.253.112.36" drop'`

### Listing Zones and Rules

To list all the configured zones in our firewall, we can use the `--list-all-zones` option:

`firewall-cmd --list-all-zones`

To list the rules in a specific zone, we can use the `--list-rich-rules` option:

`firewall-cmd --zone=secure --list-rich-rules`

### Managing Default Policies for Zones

As mentioned earlier, each zone has its own default policy, but we can change this using the `--set-default` option. For example, if we want to set the default policy for our `public` zone to `ACCEPT`, we can run the following command:

`sudo firewall-cmd --zone=public --set-default=accept`

This will allow all incoming connections in the `public` zone by default.

## Making Changes Permanent

Firewalld allows temporary changes that are not saved after a reboot. To make a change permanent, use the `--permanent` option when adding or modifying rules. For example,

`sudo firewall-cmd --permanent --zone=secure --add-rich-rule='rule family="ipv4" source address="192.168.1.2" port port="22" protocol="tcp" accept'`

This change will be saved and applied every time the firewall service is started.

## Reload and Restart firewall-cmd

Any changes made to the firewall-cmd configuration will only take effect after the service is reloaded or restarted. To do this, use the `reload` or `restart` options respectively:

`sudo firewall-cmd --reload`<br>
`sudo firewall-cmd --restart`

## Conclusion

Congratulations, you have successfully learned how to restrict network access using firewall-cmd/firewall. By utilizing zones, rules, and policies, you can control incoming and outgoing network traffic and secure your system. Be sure to regularly review your firewall configurations and make changes as needed to keep your system protected.