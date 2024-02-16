+++
title = "Restrict network access using firewall-cmd/firewall"
date = "2024-02-16T10:36:25-05:00"
author = "root"
cover = ""
tags = ["firewalld", "--add-service=ssh`.", "firewall.", "system", "services", "command:", "system.", "firewalls"]
keywords = ["firewall-cmd?", "--add-service=ssh`.", "firewall-cmd/firewall", "network", "linux", "command:", "security", "service"]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Red Hat Certified Systems Administrator Exam 200 Objective: Restrict Network Access using firewall-cmd/firewall Tutorial

In this tutorial, we will dive into the details of how to restrict network access using firewall-cmd/firewall, which is a crucial skill to master for the Red Hat Certified Systems Administrator Exam 200. Firewalls are essential security measures that control the flow of network traffic to and from a system. They act as a barrier between a trusted internal network and an untrusted external network, such as the internet.

By the end of this tutorial, you will understand:

- How to use firewall-cmd to interact with the firewall
- The structure and terminology of the firewall rules
- How to configure network zones and services
- How to restrict network access using firewall rules
- How to save and persist firewall changes

So let's get started!

## What is firewall-cmd?

firewall-cmd is a command-line interface (CLI) tool that allows you to manage the firewall on a system. It is the primary means of configuring the firewall in Red Hat Enterprise Linux (RHEL). It uses D-Bus to communicate with the firewalld service, which is responsible for managing the firewall. The firewalld service uses a set of rules to determine which network packets are allowed or blocked.

## Understanding Firewall Rules

Before we jump into configuring the firewall, it is essential to understand the structure of firewall rules. Firewall rules are made up of four main components:

1. **Rule Type:** This specifies the type of rule, such as a zone rule, service rule, or port rule.
2. **Zone:** A zone is a subset of the network with a specific level of trust attached to it. The default zones in Red Hat Enterprise Linux are public, external, internal, dmz, and work.
3. **Source and Destination:** These specify the network or IP addresses from where the traffic is coming and where it is going.
4. **Action:** This determines whether the traffic is allowed or blocked.

## Configuring Network Zones and Services

Before we can start restricting network access, we need to configure network zones and services. These are essential components of the firewall that help define the level of trust attached to a particular network or service.

To configure network zones and services using firewall-cmd, follow these steps:

Step 1: List the available network zones by running the command `sudo firewall-cmd --get-zones`.

Step 2: Choose the appropriate zone for your system. For this tutorial, we will use the `public` zone.

Step 3: To set your interface to a specific zone, run the command `sudo firewall-cmd --zone=public --change-interface=<interface_name>`. Replace the <interface_name> with the name of your interface.

Step 4: Next, we need to define the services that are allowed in this zone. To view the list of available services, run the command `sudo firewall-cmd --get-services`.

Step 5: Let's say we want to allow SSH access. We can add this service to our zone by running the command `sudo firewall-cmd --zone=public --add-service=ssh`.

Step 6: To make these changes permanent, use the `--permanent` flag with the above commands and then reload the firewall by running `sudo firewall-cmd --reload`.

## Restricting Network Access using Firewall Rules

Now that we have configured our zones and services, we can start restricting network access using firewall rules. There are two types of rules you can use: **zone rules** and **service rules**.

### Zone Rules

Zone rules apply to all traffic coming into or going out of a specific zone. To add a rule for a zone, follow these steps:

Step 1: List the current rules for the zone by running `sudo firewall-cmd --zone=<zone_name> --list-all`.

Step 2: To add a rule, use the `--add-rich-rule` option followed by the rule arguments. For example, if we want to block all incoming traffic from a specific IP address, we can use the following command:

 `sudo firewall-cmd --zone=public --add-rich-rule='rule family="ipv4" source address="x.x.x.x" drop'`

This command adds a rule to the public zone that blocks all incoming traffic from the IP address x.x.x.x.

### Service Rules

Service rules, on the other hand, apply to a specific service. To add a rule for a service, follow these steps:

Step 1: List the current rules for the service by running `sudo firewall-cmd --zone=<zone_name> --list-all`.

Step 2: To add a rule, use the `--add-service` option followed by the name of the service. For example, if we want to block all incoming HTTP traffic, we can use the following command:

`sudo firewall-cmd --zone=public --add-service=http`

This command adds a rule to the public zone that blocks all incoming HTTP traffic.

## Saving and Persisting Changes

To ensure that our firewall rules persist upon system reboot, we need to save them. To save our changes, follow these steps:

Step 1: List the current runtime rules using `sudo firewall-cmd --runtime-to-permanent`.

Step 2: To make the changes permanent, either reload the firewall or restart the system.

By default, all changes made using the `--add-*` and `--remove-*` options are applied at runtime. To make these changes permanent, use the `--permanent` option.

## Conclusion

Congratulations! You have now learned how to restrict network access using firewall-cmd/firewall. We covered essential concepts such as firewall-cmd, firewall rules, network zones, services, and how to save and persist changes. By mastering this skill, you will be well-prepared for the Red Hat Certified Systems Administrator Exam 200. Keep practicing and mastering these concepts, and you'll be on your way to becoming a certified Red Hat Systems Administrator. Good luck! 