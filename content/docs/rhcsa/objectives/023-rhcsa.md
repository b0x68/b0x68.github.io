# Tech Tutorial: Preserving System Journals

## Introduction

In Linux-based systems, the journal maintained by systemd-journald is a fundamental component used for logging and keeping track of system events and messages. This tutorial delves into how to preserve system journals effectively, ensuring that you can maintain a robust log for troubleshooting and auditing purposes. We will be using `systemd-journald`, which is part of the systemd suite, common to many Linux distributions such as Fedora, Ubuntu, and CentOS.

## Prerequisites

To follow this tutorial, you should have:
- A Linux system with `systemd` installed.
- Basic familiarity with terminal and command-line operations.
- Sudo or root access on the system to modify service configurations.

## Step-by-Step Guide

### Step 1: Understanding Systemd Journal

Systemd-journald collects and stores logging data in a binary format. These logs can be viewed using the `journalctl` command. By default, systemd-journald may not retain log files after a reboot, depending on your system’s configuration.

### Step 2: Viewing Current Journal Settings

1. Open your terminal.
2. To see the current status and configuration of the journal service, run:
   ```bash
   systemctl status systemd-journald
   ```

3. To check the current configuration file settings, use:
   ```bash
   cat /etc/systemd/journald.conf
   ```
   Look for settings like `Storage=`, `SystemMaxUse=`, `SystemKeepFree=`, `SystemMaxFileSize=`, and `SystemMaxFiles=`. If they are commented out (preceded by `#`), they are not set and default values are used.

### Step 3: Configuring Journal Persistence

To make sure logs are preserved across reboots, you need to edit the `journald.conf` file.

1. Open the configuration file in a text editor with root privileges. For instance:
   ```bash
   sudo nano /etc/systemd/journald.conf
   ```

2. Find the `Storage=` line and change it to:
   ```plaintext
   Storage=persistent
   ```
   This setting ensures that logs are stored in `/var/log/journal/`, which is persistent across reboots.

3. Optionally, adjust the space that logs are allowed to use on disk by setting:
   ```plaintext
   SystemMaxUse=1G
   ```
   This limits the journal logs to use a maximum of 1GB of disk space.

4. After making changes, save the file and exit the editor.

### Step 4: Restarting Journal Service

Apply the changes by restarting the systemd-journald service:
```bash
sudo systemctl restart systemd-journald
```

### Step 5: Verifying Configuration

Check if the settings are applied correctly:
```bash
journalctl --disk-usage
```
This command shows the amount of disk space the journal logs are currently using.

## Detailed Code Examples

Let’s simulate a scenario where you need to troubleshoot a service failure after a reboot:

1. **Create a sample service**:
   - Create a new service file:
     ```bash
     sudo nano /etc/systemd/system/sample.service
     ```
   - Add the following contents:
     ```plaintext
     [Unit]
     Description=Sample Service

     [Service]
     Type=simple
     ExecStart=/bin/false

     [Install]
     WantedBy=multi-user.target
     ```
   - Enable and start the service:
     ```bash
     sudo systemctl enable --now sample.service
     ```

2. **Reboot the system** and then check the status of the service:
   ```bash
   systemctl status sample.service
   ```

3. **Check the journal** for logs related to the `sample.service`:
   ```bash
   journalctl -u sample.service
   ```
   This command fetches logs specifically for `sample.service` even after the reboot, thanks to the persistent storage configuration.

## Conclusion

By following this tutorial, you have learned how to configure and verify the preservation of system journals on a Linux system running systemd. This configuration is crucial for system administrators and developers who need reliable access to historical data for troubleshooting and auditing system behavior over time. Always remember to tailor the journal settings according to the specific needs and resources of your system.