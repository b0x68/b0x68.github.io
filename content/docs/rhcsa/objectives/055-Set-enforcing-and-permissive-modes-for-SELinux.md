# Tech Tutorial: Manage security with SELinux Modes

## Introduction

Security-Enhanced Linux (SELinux) is a Linux kernel security module that provides a mechanism for supporting access control security policies. It is a crucial tool for system administrators to restrict programs to the least amount of privilege they require to perform their tasks. In this tutorial, we will cover how to configure SELinux modes, specifically focusing on enforcing and permissive modes, as part of the preparation for the Red Hat Certified System Administrator (RHCSA) exam.

SELinux operates in three modes:
1. **Enforcing:** SELinux policy is enforced. SELinux denies access based on SELinux policy rules.
2. **Permissive:** SELinux policy is not enforced but denials are logged for actions that would have been denied if running in enforcing mode.
3. **Disabled:** SELinux is turned off.

Understanding how to switch between these modes is essential for troubleshooting, securing applications, and system management.

## Step-by-Step Guide

### Checking Current SELinux Status

Before changing the SELinux mode, it's important to check the current mode. This can be done using the `sestatus` command.

```bash
$ sestatus
```

This command will output the current status of SELinux, including the current mode (enforcing, permissive, or disabled), the policy version, and other configurations.

### Changing SELinux Mode Temporarily

To change the SELinux mode temporarily (i.e., until the next reboot), you can use the `setenforce` command. This is useful for testing and troubleshooting without making permanent changes to the system configuration.

- **Setting SELinux to Enforcing Mode**

```bash
$ sudo setenforce 1
```

- **Setting SELinux to Permissive Mode**

```bash
$ sudo setenforce 0
```

After running these commands, you can verify the change by running `sestatus` again.

### Changing SELinux Mode Permanently

To permanently change the SELinux mode, you need to edit the SELinux configuration file located at `/etc/selinux/config`.

1. Open the configuration file in a text editor:

```bash
$ sudo vi /etc/selinux/config
```

2. Find the line that starts with `SELINUX=` and adjust it to your desired state:

- **To set SELinux to enforcing mode:**

```plaintext
SELINUX=enforcing
```

- **To set SELinux to permissive mode:**

```plaintext
SELINUX=permissive
```

3. Save the changes and exit the editor. For the changes to take effect, you must reboot the system:

```bash
$ sudo reboot
```

After the system reboots, you can use `sestatus` to confirm that the SELinux mode has been updated as expected.

## Detailed Code Examples

Let’s take a more practical look by applying what we've learned in a real-world scenario:

**Scenario:** You have an application that is currently being developed and tested on a RHEL server. You need to troubleshoot this application without disabling SELinux completely.

**Solution:** Set SELinux temporarily to permissive mode to allow the application to run while logging any actions that would have been blocked.

```bash
$ sudo setenforce 0
$ sestatus
```

Now, run your application tests. SELinux will log any actions that would have been denied in enforcing mode. Review the logs in `/var/log/audit/audit.log` for entries referring to SELinux denials.

```bash
$ sudo grep AVC /var/log/audit/audit.log
```

After troubleshooting, set SELinux back to enforcing mode:

```bash
$ sudo setenforce 1
$ sestatus
```

## Conclusion

Understanding how to manage and configure SELinux modes is a fundamental skill for any system administrator, especially those working in environments that require high levels of security like those who are preparing for the RHCSA exam. By learning how to switch between enforcing and permissive modes, you can effectively troubleshoot applications and maintain system security without permanently weakening your system’s defenses. Remember, practice is key, so be sure to try these commands in a safe environment to build your confidence and proficiency.