# Tech Tutorial: Configure Systems to Boot into a Specific Target Automatically

## Introduction

In the Linux operating system, the process of booting is managed by the `systemd` system and service manager. One of the key concepts in `systemd` is the idea of "targets" which are similar to the runlevels used in older init systems but more flexible. This tutorial will guide you through configuring a Linux system to boot into a specific target automatically. This is especially useful for setting up a system for a specific purpose, such as a graphical desktop, a network server, or a multi-user environment.

## Prerequisites

- A Linux system with `systemd` installed (most modern Linux distributions like CentOS, Fedora, Debian, and Ubuntu come with `systemd`).
- Access to a terminal or command line.
- Permissions to execute system commands (typically root access).

## Step-by-Step Guide

### Step 1: Understanding Systemd Targets

Before we configure the system to boot into a specific target, it's important to understand what targets are available. Some common systemd targets include:

- `graphical.target` — Used for systems with a graphical interface.
- `multi-user.target` — Used for systems with multiple users but no GUI.
- `network.target` — Basic network services started.
- `reboot.target` — Reboots the system.
- `poweroff.target` — Powers off the system.

You can list all available targets on your system using the following command:

```bash
systemctl list-units --type=target
```

### Step 2: Check the Current Default Target

To see which target is currently set as the default on your system, use the following command:

```bash
systemctl get-default
```

This command will output the current default target, such as `graphical.target`.

### Step 3: Changing the Default Target

To change the default boot target, use the `set-default` command. For example, if you want the system to boot into a multi-user command line environment by default, you can set `multi-user.target` as the default:

```bash
sudo systemctl set-default multi-user.target
```

Replace `multi-user.target` with your desired target. You can verify that the default target has been changed by rerunning the `get-default` command:

```bash
systemctl get-default
```

### Step 4: Rebooting to Apply Changes

After changing the default target, you need to reboot the system to apply the changes:

```bash
sudo reboot
```

Once the system boots up again, it will enter the target you specified. You can confirm that you are in the correct target by checking the status of the system:

```bash
systemctl status
```

Look in the output for the line that indicates what target the system has reached.

## Detailed Code Examples

Here is a more detailed example of how you might automate the process of setting a system to boot into `graphical.target` using a script:

```bash
#!/bin/bash

# Script to set the default systemd target to graphical.target

# Check if we have root privileges
if [ "$(id -u)" -ne 0 ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

# Set the default target to graphical.target
echo "Setting the default target to graphical.target..."
sudo systemctl set-default graphical.target

# Confirm the change
default_target=$(systemctl get-default)
echo "Default target is now set to ${default_target}"

# Option to reboot the system
read -p "Do you want to reboot the system now? (y/n) " answer
case ${answer:0:1} in
    y|Y )
    echo "Rebooting the system..."
    sudo reboot
    ;;
    * )
    echo "Reboot cancelled. Changes will apply on next reboot."
    ;;
esac
```

## Conclusion

Configuring your Linux system to boot into a specific target automatically is a powerful feature provided by systemd. It allows for flexibility in how the system is set up and used, whether it's for a desktop environment, server, or any other specialized configuration. By understanding and using systemd targets, you can ensure your system boots into the right environment every time.