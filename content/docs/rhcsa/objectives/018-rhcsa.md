# Tech Tutorial: Operate Running Systems

## Introduction

In this tutorial, we will explore how to interrupt the boot process to gain access to a system. This skill is crucial for system administrators and IT professionals to understand, especially for troubleshooting and recovering from non-bootable states due to misconfigurations or other issues. We will primarily focus on Linux systems, which are widely used in server environments.

**Disclaimer:** This tutorial is meant for educational purposes only. Interrupting the boot process and accessing a system should only be done on machines you own or have explicit permission to work on.

## Step-by-Step Guide

### Prerequisites

- A Linux machine (physical or virtual)
- Basic understanding of Linux commands
- Access to the machine's console or remote management interface

### Step 1: Access the GRUB Menu

GRUB (GRand Unified Bootloader) is a common bootloader used by many Linux distributions. It is the first software that runs when a computer starts and is responsible for loading the kernel of the operating system.

1. **Restart the system**: You can either use the reboot command from an existing session or manually power cycle the machine.

    ```bash
    sudo reboot
    ```

2. **Interrupt the normal boot process**: As the system begins to boot, you will typically need to press a key to interrupt the auto-boot sequence. Common keys include `Esc`, `Shift`, or `F8`. This needs to be done right before the operating system begins to load, usually within a few seconds after powering on.

3. **Access the GRUB menu**: Once you successfully interrupt the boot process, you should see the GRUB menu. This menu lists the available kernels and recovery options.

### Step 2: Edit GRUB Boot Parameters

To gain access to the system, you may need to modify the kernel boot parameters:

1. **Select the default kernel**: Use the arrow keys to highlight the default Linux kernel entry (usually marked with `Ubuntu` or your specific Linux distribution).

2. **Edit boot parameters**: Press `e` to edit the boot parameters. You'll be taken to a screen where you can modify various boot options.

3. **Modify the kernel command line**: Look for the line starting with `linux` and find the part that reads `ro quiet splash`. This line tells GRUB how to boot the kernel.

4. **Enable administrative access**: Change `ro` to `rw` to mount the root filesystem as read-write, and add `init=/bin/bash` at the end of the line. This tells the kernel to run Bash as the initial process instead of the usual system initialization process.

    ```
    linux /boot/vmlinuz-...-generic root=UUID=... rw quiet splash init=/bin/bash
    ```

5. **Boot the modified entry**: Press `Ctrl + X` or `F10` to boot with these parameters. The system should boot to a root shell.

### Step 3: Gain Access and Make Changes

At this point, you should have a root shell without needing a password.

1. **Change the root password** if necessary:

    ```bash
    passwd root
    ```

2. **Make any necessary changes** to system files to fix issues that may be preventing normal boot.

3. **Reboot the system** normally to see if the issue is resolved. Make sure to exit from the root shell and reboot:

    ```bash
    exec /sbin/init
    ```

    Or simply reboot:

    ```bash
    reboot
    ```

## Conclusion

Interrupting the boot process and editing boot parameters is a powerful technique for gaining access to a system, especially in cases where normal access methods are unavailable. This method can be a lifesaver in various scenarios such as forgotten passwords, file system repairs, or other critical troubleshooting.

Always ensure that you perform these actions responsibly and ethically, respecting privacy and data integrity. This approach should only be used in appropriate situations, such as in recovery scenarios or with explicit authorization.

Remember, with great power comes great responsibility!