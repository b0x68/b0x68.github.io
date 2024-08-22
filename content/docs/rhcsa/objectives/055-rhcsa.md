# Tech Tutorial: Manage Security by Setting Enforcing and Permissive Modes for SELinux

## Introduction

Security-Enhanced Linux (SELinux) is a security architecture integrated into the Linux kernel, using a flexible Mandatory Access Control (MAC) system built into the kernel. Understanding how to manage SELinux modes is crucial for ensuring that system security policies do not interfere unduly with system operations while still maintaining the integrity and security of the system. This tutorial will focus on how to set SELinux to either enforcing or permissive modes, which is a critical skill for system administrators.

## What is SELinux?

SELinux provides a mechanism for supporting access control security policies. This prevents unauthorized access and enables administrators to define what users and applications can do on a system. SELinux has three modes of operation:

- **Enforcing:** SELinux policy is enforced. SELinux denies access based on SELinux policy rules, and logs actions.
- **Permissive:** SELinux does not enforce the policy but rather logs all denials. This mode is useful for troubleshooting and policy development.
- **Disabled:** SELinux is turned off.

## Step-by-Step Guide

### Checking Current SELinux Status

Before changing SELinux modes, it's important to check the current status. This can be done using the `sestatus` command.

```bash
sestatus
```

The output should look something like this:

```
SELinux status:                 enabled
SELinuxfs mount:                /sys/fs/selinux
SELinux root directory:         /etc/selinux
Loaded policy name:             targeted
Current mode:                   enforcing
Mode from config file:          enforcing
Policy MLS status:              enabled
Policy deny_unknown status:     allowed
Max kernel policy version:      31
```

### Changing SELinux Mode Temporarily

To change the SELinux mode temporarily, use the `setenforce` command. This change will last until the system is rebooted.

1. **Set SELinux to Permissive**

   ```bash
   sudo setenforce 0
   ```

   Verify the change:

   ```bash
   getenforce
   ```
   Output:
   ```
   Permissive
   ```

2. **Set SELinux to Enforcing**

   ```bash
   sudo setenforce 1
   ```

   Verify the change:

   ```bash
   getenforce
   ```
   Output:
   ```
   Enforcing
   ```

### Changing SELinux Mode Permanently

To permanently change the SELinux mode, you need to edit the SELinux configuration file.

1. Open the SELinux configuration file in a text editor:

   ```bash
   sudo nano /etc/selinux/config
   ```

2. Find the line that starts with `SELINUX=` and modify it as needed:

   - To set SELinux to permissive mode:
     ```
     SELINUX=permissive
     ```
   - To set SELinux to enforcing mode:
     ```
     SELINUX=enforcing
     ```

3. Save and close the file. For the changes to take effect, reboot the system:

   ```bash
   sudo reboot
   ```

### Checking Changes After Reboot

After your system reboots, verify that the SELinux mode has been successfully changed:

```bash
sestatus
```

Look for the "Current mode" line in the output.

## Conclusion

Understanding and controlling SELinux modes is essential for managing the security policy of Linux systems. Changing between enforcing and permissive can help you troubleshoot issues, develop new policies, or enhance system security as required. Remember that keeping SELinux in enforcing mode is recommended for production environments to ensure that policies are properly enforced.