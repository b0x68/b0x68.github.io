# Tech Tutorial: Modify the System Bootloader on Red Hat Enterprise Linux (RHEL)

## Introduction

In the Red Hat Certified System Administrator (RHCSA) exam, one of the core competencies is the ability to modify the system bootloader. The bootloader on RHEL systems is typically GRUB2 (GRand Unified Bootloader version 2), which is responsible for loading the kernel of the operating system and initial RAM disk at system start-up. Understanding how to configure and modify GRUB2 is essential for troubleshooting boot issues, customizing boot parameters, and securing the boot process.

This tutorial will guide you through the process of modifying the system bootloader on a RHEL system. We will cover how to edit bootloader configurations, change default kernel boot parameters, set a boot password, and more.

## Prerequisites

- A RHEL 7 or RHEL 8 installation.
- Root or sudo privileges on the system.

## Step-by-Step Guide

### Step 1: Accessing the GRUB2 Configuration

The GRUB2 configuration file on RHEL is located at `/etc/default/grub`. This file contains user-editable settings that affect the global GRUB2 behavior.

1. **Open the GRUB configuration file:**
   ```bash
   sudo vi /etc/default/grub
   ```

### Step 2: Modify Kernel Boot Parameters

To add or modify kernel boot parameters:

1. **Locate the line starting with `GRUB_CMDLINE_LINUX`:**
   - This line contains kernel parameters that are applied globally.

2. **Add or modify parameters:**
   - For example, to enable verbose booting, you can add the `debug` parameter.
   ```bash
   GRUB_CMDLINE_LINUX="crashkernel=auto rhgb quiet debug"
   ```

3. **Save and exit the editor.**

### Step 3: Regenerate the GRUB2 Configuration

After modifying `/etc/default/grub`, you must regenerate the main GRUB2 configuration file (`grub.cfg`) for changes to take effect.

- **Regenerate the GRUB2 configuration on BIOS-based systems:**
  ```bash
  sudo grub2-mkconfig -o /boot/grub2/grub.cfg
  ```

- **Regenerate the GRUB2 configuration on UEFI-based systems:**
  ```bash
  sudo grub2-mkconfig -o /boot/efi/EFI/redhat/grub.cfg
  ```

### Step 4: Setting a GRUB2 Boot Password

To enhance system security, you can set a password that must be entered to edit boot entries.

1. **Generate a password hash:**
   ```bash
   grub2-mkpasswd-pbkdf2
   ```
   - Follow the prompts to enter and confirm the password. Note the password hash output.

2. **Edit the GRUB2 configuration file:**
   ```bash
   sudo vi /etc/grub.d/40_custom
   ```

3. **Add the password settings:**
   - At the end of the file, add:
   ```bash
   set superusers="admin"
   password_pbkdf2 admin [paste-your-password-hash-here]
   ```
   - Replace `[paste-your-password-hash-here]` with the password hash from step 1.

4. **Regenerate the GRUB2 configuration as per Step 3.**

## Detailed Code Examples

Here's a detailed example of modifying the GRUB configuration to include a new kernel parameter and setting up a boot password.

```bash
# Open the GRUB configuration file
sudo vi /etc/default/grub

# Modify the GRUB_CMDLINE_LINUX line to add a 'debug' parameter
GRUB_CMDLINE_LINUX="crashkernel=auto rhgb quiet debug"

# Save and exit the editor

# Regenerate the GRUB configuration for a UEFI-based system
sudo grub2-mkconfig -o /boot/efi/EFI/redhat/grub.cfg

# Generate a password hash for the boot password
grub2-mkpasswd-pbkdf2

# Edit the custom GRUB file
sudo vi /etc/grub.d/40_custom

# Add password protection
set superusers="admin"
password_pbkdf2 admin [paste-your-password-hash-here]

# Regenerate the GRUB configuration
sudo grub2-mkconfig -o /boot/efi/EFI/redhat/grub.cfg
```

## Conclusion

Modifying the system bootloader on RHEL involves understanding and editing the GRUB2 configuration files. By following the steps outlined in this tutorial, system administrators can customize boot parameters, enhance system security with a boot password, and troubleshoot various boot issues. Mastery of these skills is vital for effective system management and is a valuable part of preparing for the RHCSA exam.