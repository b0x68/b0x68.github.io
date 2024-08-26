# Tech Tutorial: Operate Running Systems

## Exam Objective: Preserve System Journals

### Introduction

In the realm of system administration, especially on systems that utilize `systemd`, preserving system journals is crucial for diagnosing issues, auditing, and ensuring that historical data is accessible for analysis. The system journal collected by `systemd-journald` is a fundamental component for logging system events and messages. This tutorial will focus on how to effectively preserve these journals on Linux systems that use `systemd`.

### Prerequisites

Before diving into the tutorial, ensure that you have:
- A Linux system running `systemd`
- Sudo or root access to the system
- Basic familiarity with command-line operations

### Step-by-Step Guide

#### Step 1: Understanding Systemd Journald

`systemd-journald` is a service that collects and manages journal entries from different sources. By default, these logs are stored in `/run/log/journal/` and are volatile (i.e., they are lost on reboot). To preserve these logs across reboots, they must be stored in `/var/log/journal/`.

1. **Check if Persistent Storage is Enabled**

   Run the following command to check if persistent storage of logs is enabled:
   ```bash
   cat /etc/systemd/journald.conf | grep Storage
   ```
   If the output is `#Storage=auto` or `Storage=volatile`, you need to change this setting to `Storage=persistent`.

#### Step 2: Enabling Persistent Storage

1. **Edit the journald Configuration**

   Open the `journald.conf` file in a text editor:
   ```bash
   sudo nano /etc/systemd/journald.conf
   ```
   Find the line that contains `Storage=` and change it to:
   ```
   Storage=persistent
   ```
   Save and close the file.

2. **Restart systemd-journald**

   Apply the changes by restarting the service:
   ```bash
   sudo systemctl restart systemd-journald
   ```

#### Step 3: Verifying the Configuration

1. **Check Journal Directory**

   After restarting, ensure that the `/var/log/journal/` directory is created:
   ```bash
   ls /var/log/journal/
   ```
   You should see a directory with a machine-id as the name.

2. **Inspect Logs**

   Use the `journalctl` command to inspect the logs:
   ```bash
   journalctl -D /var/log/journal/
   ```

#### Step 4: Managing Journal Size

To prevent the journal from using too much disk space, configure size limits:

1. **Edit the journald Configuration Again**

   Open the configuration file:
   ```bash
   sudo nano /etc/systemd/journald.conf
   ```
   Set the disk usage limits, for example:
   ```
   SystemMaxUse=500M
   SystemKeepFree=1G
   SystemMaxFileSize=50M
   ```
   Save and close the file.

2. **Restart the Service**

   ```bash
   sudo systemctl restart systemd-journald
   ```

### Detailed Code Examples

Here are detailed examples of commands you might use to manage the system journal:

- **Checking Disk Usage of the Journal**
  ```bash
  journalctl --disk-usage
  ```

- **Vacuuming Old Logs**
  ```bash
  sudo journalctl --vacuum-size=500M
  sudo journalctl --vacuum-time=1years
  ```

### Conclusion

Preserving system journals is essential for maintaining a robust and recoverable system. By enabling persistent storage, managing space, and understanding how to interact with `systemd-journald`, you can ensure that your system's logs are preserved efficiently and sustainably. This practice not only aids in troubleshooting but also complies with many auditing requirements. Stay proactive in your log management to keep your systems secure and well-documented.

### Further Reading

- [systemd-journald man page](https://www.freedesktop.org/software/systemd/man/journald.conf.html)
- [Arch Wiki on Systemd/Journal](https://wiki.archlinux.org/index.php/Systemd/Journal)