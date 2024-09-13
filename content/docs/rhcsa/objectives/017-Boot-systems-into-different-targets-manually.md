# Tech Tutorial: Operate Running Systems

## Introduction

In this tutorial, we will cover how to boot systems into different targets manually, a key objective for the Red Hat Certified System Administrator (RHCSA) exam. The concept of "targets" in Red Hat Enterprise Linux (RHEL) pertains to systemd, which is the init system and service manager used in this distribution. Understanding how to manage systemd targets is crucial for system administration tasks such as boot management, service management, and system customization.

## Step-by-Step Guide

### Understanding Systemd and Targets

Systemd uses 'targets' to group and manage system services. These targets replace the traditional runlevels in older SysVinit system and are more flexible. Commonly used targets include:

- `graphical.target`: Used for a full graphical user interface.
- `multi-user.target`: Used for a multi-user text mode.
- `rescue.target`: Used for a rescue shell.

### Checking the Current Target

Before changing the target, it's useful to know the current target. To check the current target, use the following command:

```bash
systemctl get-default
```

This command will display the current default target, which is the target the system is set to use at boot.

### Listing Available Targets

To see what targets are available on your system, use:

```bash
systemctl list-units --type=target
```

### Changing Targets Manually

To change the current target temporarily (it will revert upon reboot), use the `systemctl isolate` command. For example, to switch to `multi-user.target`:

```bash
sudo systemctl isolate multi-user.target
```

This command will stop the services that are not needed in the `multi-user.target` and start those that are part of it.

### Setting a Default Target

To set a default target that the system will boot into, use the `systemctl set-default` command. For example, to set the graphical interface as the default:

```bash
sudo systemctl set-default graphical.target
```

After setting the default, you can confirm the change with:

```bash
systemctl get-default
```

### Detailed Code Examples

Let’s consider a scenario where we need to boot into emergency mode to perform system maintenance:

1. **Boot into Rescue Target**

   If your system is experiencing issues and requires maintenance at a root level without loading standard services, you can switch to `rescue.target`:

   ```bash
   sudo systemctl isolate rescue.target
   ```

   This command will provide a minimal environment with root privileges.

2. **Perform Maintenance Tasks**

   In the rescue environment, you can perform various maintenance tasks like checking and repairing file systems, modifying important configuration files, or recovering data.

3. **Return to a Normal State**

   After completing the maintenance tasks, if you want to go back to the normal operational state (let's assume `multi-user.target`):

   ```bash
   sudo systemctl isolate multi-user.target
   ```

   This will take the system out of the rescue state and start regular system services suitable for multi-user operations.

## Conclusion

Understanding how to manage and manipulate systemd targets is a fundamental skill for any system administrator working with RHEL. By learning how to manually change between these targets, you can control the state of a system effectively, making it possible to perform specific tasks suited to different system states. Always remember to check the impact of changing targets on running services and ensure that any changes made are consistent with system security and stability requirements.