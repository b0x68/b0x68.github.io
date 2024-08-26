# Tech Tutorial: Manage Security by Setting SELinux Modes

## Introduction

Security-Enhanced Linux (SELinux) is a mandatory access control (MAC) security mechanism implemented in the kernel. SELinux offers a means of enforcing some security policies which would otherwise not be effectively implemented by a System Administrator.

When you install a Linux distribution that supports SELinux, like CentOS or Fedora, it typically comes enabled and in enforcing mode by default. However, there are times when you might need to switch SELinux between enforcing and permissive modes for troubleshooting, testing, or working within specific security policies. This tutorial will guide you through what SELinux modes are, why they are important, and how to switch between these modes.

### What are SELinux Modes?

SELinux operates primarily in two modes:

1. **Enforcing:** In this mode, SELinux enforces the policy, denies access based on policy rules, and logs actions.
2. **Permissive:** In this mode, SELinux does not enforce the policy but still logs all denials that would have occurred in enforcing mode.

Understanding these modes is crucial for system security and administration.

## Step-by-Step Guide

This guide will provide you with the necessary commands and steps to set SELinux modes. We will cover how to check the current mode, how to switch between modes, and how to make these changes persistent across reboots.

### Prerequisites

- A Linux system with SELinux installed (Fedora, CentOS, RHEL, etc.)
- Root or sudo access on the system

### Checking the Current SELinux Mode

Before changing SELinux modes, it’s important to check the current mode. You can do this with the following command:

```bash
sestatus
```

This command will output the current SELinux status, including the mode it's in (enforcing or permissive).

### Changing SELinux Mode Temporarily

To change the SELinux mode temporarily, you can use the `setenforce` command. This change will last until the next reboot.

1. **Switch to Permissive Mode:**

    ```bash
    sudo setenforce 0
    ```

    This command sets SELinux to permissive mode.

2. **Switch to Enforcing Mode:**

    ```bash
    sudo setenforce 1
    ```

    This command sets SELinux back to enforcing mode.

### Changing SELinux Mode Permanently

To permanently change the SELinux mode, you need to edit the SELinux configuration file.

1. Open the configuration file in your preferred text editor:

    ```bash
    sudo nano /etc/selinux/config
    ```

2. Find the line that starts with `SELINUX=` and change it to either `enforcing` or `permissive`:

    ```plaintext
    SELINUX=enforcing
    ```

    or

    ```plaintext
    SELINUX=permissive
    ```

3. Save and close the file. For the change to take effect, reboot your system:

    ```bash
    sudo reboot
    ```

### Detailed Code Examples

Let's consider a scenario where you need to deploy a web server which is not working as expected due to SELinux policies. You decide to set SELinux to permissive mode temporarily to diagnose the issue.

#### Diagnosing a Web Server Issue

1. **Check Current SELinux Mode:**

    ```bash
    sestatus
    ```

2. **Set SELinux to Permissive Mode:**

    ```bash
    sudo setenforce 0
    ```

3. **Restart the web server to apply changes:**

    ```bash
    sudo systemctl restart httpd
    ```

4. **Check the web server logs for any SELinux related denials:**

    ```bash
    sudo journalctl -u httpd | grep denied
    ```

5. **Analyze the logs, adjust the SELinux policy or fix the issue, and switch back to enforcing mode:**

    ```bash
    sudo setenforce 1
    ```

## Conclusion

Managing SELinux modes is a critical skill for Linux system administrators, especially when dealing with security and troubleshooting applications. By switching between enforcing and permissive modes, administrators can effectively manage system security while diagnosing and solving issues. Remember that while permissive mode can be useful for troubleshooting, it is best practice to keep systems in enforcing mode to ensure the highest level of security.