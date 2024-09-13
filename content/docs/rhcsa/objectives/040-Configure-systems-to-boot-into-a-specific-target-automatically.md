# Tech Tutorial: Deploy, Configure, and Maintain Systems 

## Introduction

In the realm of system administration, particularly when managing Red Hat Enterprise Linux (RHEL) systems, understanding how to configure system boot targets is crucial. This capability is essential for ensuring that your systems start with the appropriate configurations and services required for their roles. In this tutorial, we will delve into how to configure a RHEL system to boot into a specific target automatically, a key objective for the Red Hat Certified System Administrator (RHCSA) exam.

## Step-by-Step Guide

### Understanding systemd and System Targets

RHEL uses `systemd` as its init system, which introduces the concept of `targets` that replace the traditional SysV init runlevels. Targets are used to group units and to set up and start the system with various configurations. Common targets include:

- `graphical.target`: Equivalent to runlevel 5, and starts the system in graphical mode.
- `multi-user.target`: Equivalent to runlevel 3, and starts the system in multi-user text mode.
- `rescue.target`: Provides a minimal environment to perform system recovery.

### Checking the Current Target

Before configuring the system to boot into a specific target, it's helpful to know the current default target. This can be done with the following command:

```bash
systemctl get-default
```

### Step 1: Changing the Default Target

To configure your system to boot into a specific target by default, you need to use the `systemctl` command. For instance, to set the system to boot by default into the graphical interface, you would use:

```bash
sudo systemctl set-default graphical.target
```

If you wish to set the system to start in multi-user text mode, you can use:

```bash
sudo systemctl set-default multi-user.target
```

### Detailed Code Examples

**Example 1: Setting Graphical Mode as the Default**

If your server needs to start with a GUI, perhaps for a workstation or a display kiosk, you would configure it as follows:

```bash
# Set the default target to graphical mode
sudo systemctl set-default graphical.target

# Check the new default target
systemctl get-default
```

This command will output `graphical.target`, confirming the change.

**Example 2: Setting Multi-User Text Mode as the Default**

For servers that do not require a GUI, which is common in server environments, you can set the system to boot into multi-user mode:

```bash
# Set the default target to multi-user mode
sudo systemctl set-default multi-user.target

# Check the new default target
systemctl get-default
```

This will output `multi-user.target`.

### Verifying and Testing

After configuring your system's default target, it's a good practice to reboot the system to ensure that it boots into the correct target:

```bash
sudo reboot
```

After rebooting, you can use the `systemctl get-default` command again to verify that the system has booted into the correct target.

## Conclusion

Configuring your RHEL system to boot into a specific target is a fundamental skill for any system administrator. By mastering the use of `systemctl` to manage system targets, you can ensure that your systems are set up correctly for their intended roles, whether they are desktop machines needing a graphical interface or headless servers operating in multi-user mode. This knowledge not only helps in daily administration tasks but is also crucial for achieving the RHCSA certification. Remember, practical experience is the best preparation for the exam, so continue to practice these commands and explore further configurations in your test environments.