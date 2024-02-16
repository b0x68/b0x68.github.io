+++
title = "Configure firewall settings using firewall-cmd/firewalld"
date = "2024-02-16T10:37:21-05:00"
author = "root"
cover = ""
tags = ["system,", "network", "firewall", "--add-service=ssh", "configuration", "users", "linux.", "system"]
keywords = ["command:", "systemctl", "`firewall-cmd`", "networkmanager", "configuration,", "command", "firewall", "`systemctl`"]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++
:

# Red Hat Certified Systems Administrator Exam 200 Objective: Configure Firewall Settings using firewall-cmd/firewalld

In this tutorial, we will explain the steps to configure firewall settings using firewall-cmd/firewalld on a Red Hat Enterprise Linux system. This is one of the objectives on the Red Hat Certified Systems Administrator Exam 200, and it is important for system administrators to have a strong understanding of firewall configuration in order to ensure the security of their systems.

## Introduction to Firewall-cmd and Firewalld

Firewall-cmd is a command-line interface for the firewalld daemon, which is a firewall management tool for Linux. It allows users to configure and manage firewall rules easily, making it a convenient tool for system administrators.

Some key features of firewall-cmd/firewalld include:

- Support for both IPv4 and IPv6 traffic
- Zoned-based configuration for more granular control
- Integration with NetworkManager
- Support for dynamic firewall rules that are automatically activated when ports are opened

## Step 1: Checking the Firewall Status

Before we begin configuring the firewall, it is important to check its status to ensure that we are starting from a clean slate. To do this, we can use the `systemctl` command to check the status of the firewalld service:

```
systemctl status firewalld
```

If the service is not running, we can start it using the following command:

```
systemctl start firewalld
```

## Step 2: Understanding Firewall Zones

Firewalld uses zones to define the level of security for different network connections. A zone specifies which network interfaces are trusted and which are not, and allows for different firewall rules to be applied to each zone. By default, firewalld comes with the following predefined zones:

- `drop`: all incoming connections are dropped without notification
- `block`: all incoming connections are rejected with an ICMP host unreachable message
- `public`: for use with public networks
- `external`: for use with external networks
- `internal`: for use with internal networks
- `dmz`: for use with demilitarized zones
- `work`: for use with work networks
- `home`: for use with home networks
- `trusted`: for use with trusted networks

It is important to choose the appropriate zone based on the type of network connection you are configuring. For example, if you are setting up a firewall for a server connected to a public network, it is recommended to use the public zone.

## Step 3: View Current Zones and Active Zones

To view the current zones on your system, use the `firewall-cmd` command with the `--list-all-zones` option:

```
firewall-cmd --list-all-zones
```

This will list all the available zones on your system and their associated interfaces.

To view the active zones, use the `--get-active-zones` option:

```
firewall-cmd --get-active-zones
```

This will show which zones are currently active and the interfaces assigned to them.

## Step 4: Changing the Default Zone

The default zone is the zone assigned to all network connections that are not explicitly assigned to a specific zone. To change the default zone, use the `--set-default-zone` option followed by the name of the zone you want to set as default. For example, to set the home zone as the default zone, use the following command:

```
firewall-cmd --set-default-zone=home
```

## Step 5: Adding Services to Zones

Firewalld allows you to specify which services are allowed or blocked for each zone. Services are predefined groupings of ports and protocols that can be easily managed by firewalld. To add a service to a zone, use the `--add-service` option followed by the name of the service and the zone you want to add it to. For example, to add the SSH service to the public zone, use the following command:

```
firewall-cmd --add-service=ssh --zone=public
```

You can also remove services from zones using the `--remove-service` option.

## Step 6: Opening Ports for Specific Services

In addition to using services, you can also open specific ports for services using the `--add-port` option. This allows for more granular control over which ports are allowed or blocked for each zone. For example, to open port 80 for HTTP traffic on the public zone, use the following command:

```
firewall-cmd --add-port=80/tcp --zone=public
```

You can use the `--permanent` option to make these changes persistent, meaning they will be applied after the system is restarted.

## Step 7: Saving Changes and Reloading the Firewall

After making changes to the firewall configuration, it is important to save them so that they will be applied the next time the firewall is started. To do this, use the `--runtime-to-permanent` option to make the changes permanent:

```
firewall-cmd --runtime-to-permanent
```

It is also possible to reload the firewall configuration without restarting the firewalld service using the following command:

```
firewall-cmd --reload
```

## Conclusion

In this tutorial, we have covered the steps to configure firewall settings using firewall-cmd/firewalld on a Red Hat Enterprise Linux system. By understanding the role of zones and how to add services and open ports, you should now be able to effectively configure a firewall to secure your system. This knowledge will be valuable for the Red Hat Certified Systems Administrator Exam 200 and for effectively managing your systems in the future.