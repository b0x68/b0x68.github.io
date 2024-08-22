# Tech Tutorial: Operate Running Systems

## Introduction

In this tutorial, we will focus on how to manually boot systems into different targets using systemd, a system and service manager for Linux operating systems. This skill is essential for system administrators and IT professionals to control the boot process, troubleshoot issues, and ensure that systems are configured to start in the desired mode.

Systemd uses the concept of "targets" to handle the boot process. Targets are similar to the runlevels used in the init system but are more flexible. Each target has a specific purpose and can be thought of as a state of the machine, defining what services are started at boot time.

## Prerequisites

- A Linux system with systemd installed (most modern Linux distributions like CentOS, Fedora, and Ubuntu use systemd by default).
- Access to a terminal or command line interface.
- Sudo or root privileges on the system.

## Step-by-Step Guide

### Step 1: Understanding Systemd Targets

Before changing boot targets, it's important to understand what each target is designed for. Here are some common systemd targets:

- **poweroff.target**: Shuts down and powers off the system.
- **rescue.target**: Boots the system in a single-user mode with minimal services started, useful for recovery.
- **multi-user.target**: Boots the system into a multi-user state without a graphical interface, similar to traditional runlevel 3.
- **graphical.target**: Boots the system into a multi-user state with a graphical interface, similar to traditional runlevel 5.
- **reboot.target**: Reboots the system.

### Step 2: Checking the Current Target

To find out the current target, use the `systemctl` command:

```bash
systemctl get-default
```

This command will display the default target to which the system boots.

### Step 3: Changing the Target

To switch to a different target manually, you can use the `systemctl isolate` command. For example, to switch to the multi-user target, you would run:

```bash
sudo systemctl isolate multi-user.target
```

This command will stop the graphical interface and bring the system to a multi-user state without restarting the system.

### Step 4: Setting the Default Boot Target

If you want the system to boot into a specific target by default, use the `set-default` command. For example, to set the system to always start in graphical mode, you would use:

```bash
sudo systemctl set-default graphical.target
```

This command changes the symlink of `/etc/systemd/system/default.target` to point to the `graphical.target`.

### Step 5: Rebooting into a Different Target

Sometimes, you may need to reboot into a different target just once. This can be done by adding the `systemd.unit` parameter to the kernel command line. Here's how to reboot into rescue mode:

```bash
sudo systemctl reboot --force --target=rescue.target
```

Alternatively, you can edit the GRUB menu during boot:
1. Restart your system.
2. When the GRUB menu appears, select the desired Linux boot entry and press 'e' to edit.
3. Find the line starting with `linux` and append `systemd.unit=rescue.target`.
4. Press `Ctrl-X` to boot with these parameters.

## Conclusion

Understanding and manipulating systemd targets is a powerful tool for managing Linux systems. Whether you are troubleshooting, performing maintenance, or ensuring that services start in the correct mode, mastering this aspect of systemd will significantly enhance your capabilities as a system administrator. This tutorial should serve as a solid foundation for effectively managing and operating running systems using different boot targets.