# Tech Tutorial: Operate Running Systems

## Introduction

In this tutorial, we will explore how to interrupt the boot process to gain access to a system. This capability is crucial for system recovery, troubleshooting, and performing system maintenance in scenarios where usual access methods are not available. It's important to note, however, that these techniques should only be used on systems you are authorized to access, as using them without permission can be illegal and unethical.

## Prerequisites

Before proceeding, ensure you have the following:
- A computer running Linux. Most of the steps here are demonstrated on a Linux system using GRUB (GRand Unified Bootloader).
- Basic understanding of Linux commands and permissions.
- Physical access to the computer, as you will need to interact with the boot process.

## Step-by-Step Guide

### Step 1: Accessing the GRUB Menu

1. **Restart your computer.**
   - As the system starts, watch for a message indicating how to enter the boot menu or setup. This often involves pressing a key such as `F2`, `F12`, `Del`, or `Esc`.

2. **Interrupt the normal boot process to open the GRUB menu.**
   - For most Linux systems, you should press and hold the `Shift` key right after the BIOS/UEFI loads to access the GRUB menu. On some systems, you might need to repeatedly tap the `Esc` key instead.

### Step 2: Editing the GRUB Entry

1. **Select the default boot entry.**
   - Use the arrow keys to navigate to the default Linux boot option. Do not press Enter yet.

2. **Edit the boot parameters.**
   - Press `e` to edit the selected boot entry. You will be presented with a list of boot parameters.

3. **Modify the boot parameters to access a root shell.**
   - Find the line that starts with `linux` and look for `ro` (read-only). Change `ro` to `rw` (read-write).
   - At the end of this line, add `init=/bin/bash`. This tells the system to run Bash as the initial process, giving you root access without requiring a password.

   ```plaintext
   linux /vmlinuz-... root=/dev/sda1 rw init=/bin/bash
   ```

4. **Boot with the modified parameters.**
   - Press `Ctrl + x` or `F10` to boot with these parameters.

### Step 3: Gaining Root Access

1. **You should now see a root shell prompt.**
   - At this point, you have root access with a read-write file system.

2. **Change the root password (optional).**
   - If your goal is to recover access to the system, you can change the root password by typing:
     ```bash
     passwd root
     ```
   - Enter a new password when prompted.

### Step 4: Reboot and Clean Up

1. **Reboot the system properly.**
   - Type `exec /sbin/init` or `reboot -f` to restart the system normally.

2. **Remove any evidence of the boot modification if necessary.**
   - If you edited any files or changed settings, ensure they are returned to their original state.

## Conclusion

Interrupting the boot process to gain system access is a powerful method of system recovery and troubleshooting. It should be used responsibly and ethically, keeping in mind the security implications and legal boundaries. By understanding and using these techniques, you can recover from situations where the usual access methods are unavailable, potentially saving significant time and resources in critical moments.

## Further Resources

- [GNU GRUB Manual](https://www.gnu.org/software/grub/manual/grub/)
- [Linux Kernel Documentation](https://www.kernel.org/doc/html/latest/)

Remember, with great power comes great responsibility. Use these techniques judiciously and ethically.