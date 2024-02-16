+++
title = "Configure firewall settings using firewall-cmd/firewalld"
date = "2024-02-16T11:52:38-05:00"
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


# Introduction
In this tutorial, we will be discussing how to configure firewall settings using `firewall-cmd` and `firewalld` on a Red Hat system. Firewall is a critical component of network security as it acts as a protective barrier between your system and the external network. As a Red Hat Certified Systems Administrator, it is important to have a thorough understanding of how to configure firewall settings to ensure the security of your system.

# Prerequisites
Before we begin, make sure you have the following prerequisites:
- A Red Hat system with `firewall-cmd` and `firewalld` installed.
- Basic knowledge of the Linux command line.
- Root access or sudo privileges to make changes to the firewall settings.
- A basic understanding of firewall concepts and protocols.

# Understanding firewall-cmd and firewalld
## Firewall-cmd
Firewall-cmd is a command line interface tool that allows you to manage firewall settings for your system. It is the preferred method for managing the firewall configuration on Red Hat systems. Firewall-cmd operates by communicating with the firewalld daemon, which manages the firewall rules and settings.

## Firewalld
Firewalld is a dynamic firewall management tool that simplifies the process of managing firewall rules. It comes pre-installed on Red Hat systems and runs as a daemon. One of the main advantages of using firewalld is that it allows for easy management of firewall rules without having to restart the entire firewall service.

# Configuring Firewall Settings
Now, let's dive into how we can configure firewall settings using `firewall-cmd` and `firewalld`.

## 1. Check Firewall Status
Before making any changes, it is important to check the current status of your firewall. To do this, run the following command:
```
sudo firewall-cmd --state
```
This will show the current status of your firewall, which can be either `running` or `not running`.

## 2. Viewing Firewall Zones
Firewalld divides the network into different zones, with each zone having its own set of rules. By default, firewalld has the following zones:
- public: Used for public networks, such as the internet.
- internal: Used for internal networks, such as corporate networks.
- dmz: Used for demilitarized zones, such as publicly accessible servers.

To view all the available zones, use the following command:
```
sudo firewall-cmd --get-zones
```

## 3. Applying Firewall Settings to Zones
Once you have identified the desired zone, you can apply firewall settings to it. This can be done in two ways:
- Permanent: Changes are saved and applied whenever the firewall service is started.
- Immediate: Changes are applied immediately but will not persist after a system reboot.

To apply firewall settings permanently, use the `--permanent` flag, followed by the desired rule and the zone you want to apply it to. For example:
```
sudo firewall-cmd --permanent --zone=public --add-service=http
```

To apply firewall settings immediately, use the `--zone` flag with the desired rule and the zone you want to apply it to. For example:
```
sudo firewall-cmd --zone=public --add-service=https
```

## 4. Enabling and Disabling Firewall Zones
To enable a firewall zone, use the `--set-default-zone` flag with the desired zone. For example:
```
sudo firewall-cmd --set-default-zone=public
```

To disable a firewall zone, use the `--permanent` flag with the `--zone` flag, followed by the desired zone and the `--remove-zone` flag. For example:
```
sudo firewall-cmd --permanent --zone=dmz --remove-zone=demilitarized
```

## 5. Viewing Active Firewalls Rules
To view the currently active firewall rules, use the `list` command. This will display all the active rules organized by zone. For example:
```
sudo firewall-cmd --list-all
```

## 6. Adding and Removing Firewall Rules
Firewall rules can be added using the `--add-rule` flag, followed by the desired rule and the zone you want to apply it to. For example:
```
sudo firewall-cmd --add-rule="rule family=ipv4 source address=10.0.0.0/24 accept" --zone=internal
```

Similarly, you can remove a rule using the `--remove-rule` flag. For example:
```
sudo firewall-cmd --remove-rule="rule family=ipv4 source address=10.0.0.0/24 accept" --zone=internal
```

## 7. Troubleshooting Firewall Settings
If you encounter any issues with your firewall settings, the `--panic-on` command can be used to temporarily disable the firewall to troubleshoot the issue. For example:
```
sudo firewall-cmd --panic-on
```

## 8. Restarting the Firewall Daemon
After making changes to your firewall settings, it is important to restart the firewall daemon for the changes to take effect. To do this, use the `reload` command. For example:
```
sudo firewall-cmd --reload
```

# Conclusion
By now, you should have a good understanding of how to configure firewall settings using `firewall-cmd` and `firewalld` on a Red Hat system. By following these steps and understanding the various commands and flags, you can effectively manage your system's firewall to ensure the security of your network. Remember to always check the status of your firewall before making any changes and to restart the firewall daemon after making changes for them to take effect. 