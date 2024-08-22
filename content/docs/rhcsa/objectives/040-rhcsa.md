# Tech Tutorial: Deploy, Configure, and Maintain Systems

## Introduction

In this tutorial, we will dive deep into how to configure systems to boot into a specific target automatically. This functionality is crucial for ensuring that your systems start with the correct configurations and services running, tailored to your specific needs such as development, testing, or production environments.

System boot management is often handled by system and service managers like `systemd` on Linux. We will use `systemd` as our primary example due to its wide adoption in many Linux distributions. Understanding how to set and modify default boot targets can save time and reduce errors in system setup processes.

## Step-by-Step Guide

### Prerequisites

- A Linux system with `systemd` installed (common in distributions like Ubuntu, CentOS, and Fedora)
- Basic knowledge of Linux command line interface

### Step 1: Checking Current Target

Before making any changes, it's important to know the current default target of your system. Open your terminal and run:

```bash
systemctl get-default
```

This command will display the current default target, for example, `graphical.target` if your system boots into a graphical interface by default.

### Step 2: Listing Available Targets

To see all available targets on your system, use:

```bash
systemctl list-units --type=target
```

Look through the list to find the target that suits the purpose of your configuration.

### Step 3: Changing the Default Target

Suppose you want your system to boot in multi-user mode without a graphical interface. You would set the default target to `multi-user.target` using the following command:

```bash
sudo systemctl set-default multi-user.target
```

This command changes the symlink of `/etc/systemd/system/default.target` to point to the `multi-user.target`.

### Step 4: Rebooting and Verifying

After setting the default target, reboot your system:

```bash
sudo reboot
```

Once the system boots up, verify that it has booted into the correct target by running:

```bash
systemctl get-default
```

It should now show `multi-user.target`.

## Detailed Code Examples

Let’s consider a scenario where a server needs to be configured to automatically boot into a specific target based on the environment it is being deployed in. Below are scripts that could be part of a deployment pipeline:

### Example Script to Set Production Server to Multi-User Target

```bash
#!/bin/bash

# Check if running as root
if [ "$(id -u)" -ne 0 ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

# Set to multi-user target
systemctl set-default multi-user.target

# Reboot
echo "Rebooting system to apply changes..."
reboot
```

### Example Script to Configure a Development Machine to Boot into Graphical Target

```bash
#!/bin/bash

# Check if running as root
if [ "$(id -u)" -ne 0 ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

# Set to graphical target
systemctl set-default graphical.target

# Reboot
echo "Rebooting system to apply changes..."
reboot
```

## Conclusion

Configuring your system to boot into a specific target is an essential skill for system administrators and developers who manage multiple environments or need their systems to serve different roles. By mastering the use of `systemd` and its targets, you can ensure that your systems are always set up correctly, reducing downtime and increasing productivity.

This tutorial covered how to check, set, and verify the default system target using `systemd`. Implementing these steps into your deployment scripts can automate system setups and ensure consistency across your infrastructure.