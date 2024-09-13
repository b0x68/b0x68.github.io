# Tech Tutorial: Operate Running Systems

## Introduction

In the Red Hat Certified System Administrator (RHCSA) exam, one of the essential skills you will need to master is managing the system's state — specifically, how to boot, reboot, and shut down a Red Hat Enterprise Linux (RHEL) system properly. This tutorial will guide you through these operations, ensuring you understand the commands and contexts in which they are used. This knowledge is not only crucial for the exam but also for real-world system administration to ensure system reliability and uptime.

## Step-by-Step Guide

### 1. Understanding Systemd

RHEL uses `systemd` as its init system, which is the first process that starts at boot and the last one to terminate during shutdown. `systemd` provides a `systemctl` command, which is used to examine and control the state of the `systemd` system and service manager.

### 2. Booting the System

Booting the system is typically handled automatically by the system’s BIOS/UEFI and boot loader (GRUB2 in the case of RHEL). However, understanding the process can help you troubleshoot boot issues or modify boot parameters.

#### Detailed Code Example:

When the system starts, the GRUB2 menu is displayed. You can modify boot parameters temporarily by following these steps:

1. Start the system.
2. When the GRUB2 menu appears, press 'e' to edit the boot entries.
3. Navigate to the kernel line (starts with `linux16` or `linuxefi`) and append your parameters at the end of the line. For example, to enter single-user mode:
   ```bash
   linux16 /vmlinuz-... root=/dev/mapper/rhel-root ro single
   ```
4. Press `Ctrl + X` to start with these parameters.

### 3. Rebooting the System

Rebooting is the process of restarting the system, which is useful for applying updates, resetting system state, or recovering from errors.

#### Detailed Code Example:

To reboot the system, use the following `systemctl` command:
```bash
sudo systemctl reboot
```

Alternatively, you can use the `reboot` command, which is a symlink to `systemctl`:
```bash
sudo reboot
```

### 4. Shutting Down the System

Properly shutting down the system ensures that all processes terminate correctly and the filesystem is safely unmounted, preventing data loss or corruption.

#### Detailed Code Example:

To shut down and power off the system, use:
```bash
sudo systemctl poweroff
```

Or, use the `poweroff` command:
```bash
sudo poweroff
```

For shutting down the system without turning off the power:
```bash
sudo systemctl halt
```

Or:
```bash
sudo halt
```

### 5. System Status Checks

After booting, rebooting, or shutting down, you might want to check the system status.

#### Detailed Code Example:

To check if the system is active (i.e., fully booted):
```bash
systemctl is-system-running
```

This command will return `running` if all is well, or other statuses like `starting`, `degraded`, etc., based on current system state.

## Conclusion

Understanding how to manage the booting, rebooting, and shutdown processes in RHEL is crucial for system administrators. This guide has covered how to perform these tasks using `systemctl` and related commands. Make sure to practice these commands in a safe environment (like a virtual machine) to build your confidence and ensure you are prepared for the RHCSA exam and real-world administration tasks. Always remember to ensure that any critical data is backed up before initiating shutdown or reboot procedures to avoid data loss.