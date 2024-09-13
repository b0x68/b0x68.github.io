# Tech Tutorial: Operate Running Systems

## Introduction

Interrupting the boot process to gain access to a system is a critical skill for system administrators, especially when dealing with issues like lost root passwords or system recovery. This tutorial is tailored for Red Hat Certified System Administrator (RHCSA) exam takers and focuses on Red Hat Enterprise Linux (RHEL). We will cover how to interrupt the boot process effectively to gain root access to a system, specifically detailing steps suitable for RHEL 7 and RHEL 8.

## Step-by-Step Guide

### Step 1: Accessing the GRUB Menu

When you start a RHEL system, the first thing you see is the GRUB (Grand Unified Bootloader) menu. This is where you can select which kernel to boot and modify boot parameters.

1. **Start the System**: Power on your machine.
2. **Interrupt the Boot Sequence**: As soon as the BIOS completes its startup, and before the GRUB menu disappears, press the `Esc` key to stop the automatic boot. For some systems, you might need to press a specific key like `Shift` or `Space` to bring up the GRUB menu.

### Step 2: Editing GRUB Parameters

Once you have the GRUB menu on screen:

1. **Navigate to Your Kernel**: Use the arrow keys to highlight the kernel you want to boot.
2. **Edit Boot Options**: Press `e` to edit the boot options for the selected kernel.

### Step 3: Modifying Kernel Boot Parameters

You're now looking at a list of parameters that GRUB will use to boot your system. We need to modify these to gain root access.

1. **Find the Line Starting with `linux`**: This line contains the kernel parameters.
2. **Modify Boot Parameters**:
   - Append `rd.break` at the end of the line to interrupt the boot process and bring you into an emergency shell.
   - Alternatively, you can use `init=/bin/sh` to directly boot into a shell.

   Example:
   ```
   linux /vmlinuz-3.10.0-327.el7.x86_64 root=/dev/mapper/rhel-root ro crashkernel=auto rd.lvm.lv=rhel/root rd.lvm.lv=rhel/swap rhgb quiet rd.break
   ```

3. **Boot the System**: Press `Ctrl + X` or `F10` to boot with these parameters.

### Step 4: Gaining Root Access

After booting with the modified parameters, the system will stop early in the boot process, either at an emergency shell or at another point you specified:

1. **Access the Root File System**:
   ```
   switch_root:/# mount -o remount,rw /sysroot
   switch_root:/# chroot /sysroot
   ```

2. **Change the Root Password** (if necessary):
   ```
   sh-4.2# passwd root
   Enter new UNIX password:
   Retype new UNIX password:
   passwd: password updated successfully
   ```

3. **Ensure SELinux Contexts are Relabeled on Reboot**:
   ```
   sh-4.2# touch /.autorelabel
   ```

4. **Exit and Reboot**:
   ```
   sh-4.2# exit
   switch_root:/# reboot
   ```

## Detailed Code Examples

In this section, we'll delve deeper into the `rd.break` method, which is commonly used for recovering systems.

- **Using `rd.break`**: This parameter interrupts the boot process before the root file system is mounted read-only. Here is what you should append to the kernel line:
  ```
  rd.break
  ```

- **Remounting the File System**:
  ```
  mount -o remount,rw /sysroot
  chroot /sysroot
  ```

## Conclusion

Interrupting the boot process to gain access to a system is an invaluable tool in a system administrator's arsenal, particularly for troubleshooting and recovering from critical errors. By following the steps outlined in this tutorial, you should be able to effectively gain access to your RHEL system during boot time, allowing for direct system recovery and password resets. Always ensure you have legitimate reasons and the necessary permissions to perform these operations, as they can impact system security and integrity.

Remember, practice is key to mastering these techniques, and setting up a virtual environment to practice these steps is highly recommended. Good luck with your RHCSA exam preparation!