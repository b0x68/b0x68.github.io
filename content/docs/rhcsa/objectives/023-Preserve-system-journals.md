# Tech Tutorial: Operate Running Systems - Preserving System Journals

## Introduction

In the realm of system administration, particularly for those preparing for the Red Hat Certified System Administrator (RHCSA) exam, understanding how to manage and preserve system logs is crucial. System logs, especially the journal maintained by systemd's journaling service `systemd-journald`, provide vital insights into the workings of a system, which can help in troubleshooting and maintaining operational efficiency.

This tutorial will focus on how to effectively preserve system journals in Red Hat Enterprise Linux (RHEL). We will cover how to configure journal size, manage journal files, and ensure that logs are maintained across reboots.

## Step-by-Step Guide

### 1. Understanding the Journaling System

`systemd-journald` is a service that collects and stores logging data. It creates and maintains binary files called journal files in `/var/log/journal/`. The journal integrates directly with other `systemd` components and provides advanced querying capabilities.

### 2. Viewing the Current Journal

Before configuring anything, it's important to understand how to view the journal. The primary command used for this is `journalctl`. Here’s how to use it:

```bash
# Display all entries from the journal
sudo journalctl

# Follow new journal entries (similar to tail -f)
sudo journalctl -f
```

### 3. Configuring System Journal Persistence

By default, RHEL might not persist log entries across reboots if the `/var/log/journal/` directory does not exist. To ensure logs are preserved, you need to configure `journald` for persistent storage.

```bash
# Create /var/log/journal to store logs persistently
sudo mkdir -p /var/log/journal
sudo systemd-tmpfiles --create --prefix /var/log/journal

# Restart journald to apply changes
sudo systemctl restart systemd-journald
```

### 4. Managing Journal Size

To prevent the journal from using too much disk space, you can configure maximum size limits. Edit the configuration file `/etc/systemd/journald.conf`.

```bash
# Open the journald configuration file
sudo nano /etc/systemd/journald.conf
```

Add or modify the following lines to set the size limits:

```ini
SystemMaxUse=500M
RuntimeMaxUse=500M
```

These settings limit the journal to using 500 MB of disk space for both runtime and persistent storage. After making changes, restart the `systemd-journald` service:

```bash
sudo systemctl restart systemd-journald
```

### 5. Vacuuming Old Journals

To manually reduce the size of the journal by deleting old entries, you can use `journalctl`’s vacuum functions.

```bash
# Reduce the space used by the journal to below 300M
sudo journalctl --vacuum-size=300M

# Delete journal entries older than the past 10 days
sudo journalctl --vacuum-time=10d
```

### 6. Checking Journal Status

To check the status of the `systemd-journald` service and review its settings:

```bash
# Check the status of systemd-journald
sudo systemctl status systemd-journald

# Show runtime settings of systemd-journald
journalctl --disk-usage
```

## Detailed Code Examples

Here is a comprehensive bash script that sets up journal persistence, configures size limits, and vacuums old logs:

```bash
#!/bin/bash

# Ensure the journal directory exists for persistent logging
sudo mkdir -p /var/log/journal
sudo systemd-tmpfiles --create --prefix /var/log/journal

# Restart journald to apply directory changes
sudo systemctl restart systemd-journald

# Edit journald configuration for size limits
echo -e "[Journal]\nSystemMaxUse=500M\nRuntimeMaxUse=500M" | sudo tee /etc/systemd/journald.conf

# Restart journald to apply size limits
sudo systemctl restart systemd-journald

# Vacuum old logs
sudo journalctl --vacuum-size=300M
sudo journalctl --vacuum-time=10d

# Display final disk usage
journalctl --disk-usage
```

## Conclusion

Understanding and managing the systemd journal is a fundamental skill for any system administrator, especially those working with Red Hat Enterprise Linux. By following this guide, you can effectively manage system logs, ensuring that they are preserved across reboots, maintained within reasonable size limits, and old logs are cleaned up appropriately. This not only helps in troubleshooting issues but also in maintaining the overall health of the system.