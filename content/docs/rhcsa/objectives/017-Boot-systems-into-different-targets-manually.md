# Tech Tutorial: Operate Running Systems

## Introduction

In Linux systems, the concept of boot targets (also known as runlevels in older systems) is central to system administration. These targets are configurations that allow the system to boot into different states, each tailored for specific use cases. For instance, a system can boot into a graphical user state, a multi-user state without graphical support, or a recovery state. 

This tutorial aims to provide a deep understanding of how to manually boot systems into different targets using `systemd`, which is the init system and service manager in modern Linux distributions. By the end of this tutorial, you should be capable of changing boot targets, understanding their implications, and managing them efficiently.

## Prerequisites

- A Linux system with `systemd` installed (most modern distributions like Ubuntu, CentOS, Fedora, etc., use `systemd`).
- Access to a terminal or command line interface.
- Basic familiarity with system administration commands.

## Step-by-Step Guide

### 1. Checking the Current Target

Before changing the system's boot target, it's crucial to know the current target. This can be achieved with the following command:

```bash
systemctl get-default
```

This command will return the current default target, such as `graphical.target`, which is the default for systems with a GUI.

### 2. Listing Available Targets

To view all available targets on your system, use the following command:

```bash
systemctl list-units --type=target
```

This will list all the targets, along with their current status.

### 3. Changing the Current Target

To change the current target dynamically (without rebooting), you can use the `systemctl isolate` command. For example, if you want to switch to a multi-user target without GUI, you can use:

```bash
sudo systemctl isolate multi-user.target
```

This command will change the current state of the system to a multi-user environment.

### 4. Setting a Default Target

If you want the system to boot into a specific target every time it starts, you need to set the default target. For example, to set the system to always start in a graphical environment, use:

```bash
sudo systemctl set-default graphical.target
```

This change will be persistent across reboots.

### 5. Understanding Targets

Here's a brief overview of some common targets and their uses:

- **graphical.target**: Used for systems with a graphical interface.
- **multi-user.target**: Used for systems that should not start a graphical interface but need network and multiple users.
- **rescue.target**: Provides a minimal environment to perform system rescue operations.

### 6. Rebooting into a Specific Target Temporarily

If you need to boot into a specific target once (for troubleshooting or other reasons) without changing the default, you can modify the boot parameters in the bootloader (GRUB, for example). Here’s how you can do it:

- On the GRUB menu during boot, select the desired Linux boot entry and press `e` to edit.
- Find the line starting with `linux` and append your target. For example, append `systemd.unit=rescue.target` at the end of the line.
- Press `Ctrl + x` to boot with these parameters.

## Detailed Code Examples

Here’s a more complex scenario where you might want to script the checking and changing of targets based on specific conditions:

```bash
#!/bin/bash

# Check the current target
current_target=$(systemctl get-default)

# Define desired target
desired_target="graphical.target"

# Compare current target to desired target
if [ "$current_target" != "$desired_target" ]; then
  echo "Switching to $desired_target"
  sudo systemctl set-default $desired_target
  sudo systemctl isolate $desired_target
else
  echo "Already on $desired_target"
fi
```

This script checks the current target and switches to the `graphical.target` if it is not already set.

## Conclusion

Understanding and manipulating systemd targets is a powerful skill for any system administrator. It allows for precise control over the system's state and behavior, especially during boot, making it essential for both routine operations and troubleshooting. By following this tutorial, you should now be able to handle different targets confidently and tailor the system's boot process to your needs. Whether it's for a server environment or a desktop setup, mastering these commands provides a foundation for robust system management.