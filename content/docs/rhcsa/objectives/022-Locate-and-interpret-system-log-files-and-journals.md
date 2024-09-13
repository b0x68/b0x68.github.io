# Tech Tutorial: Operate Running Systems

## Introduction

Understanding how to locate and interpret system log files and journals is crucial for system administrators, especially when troubleshooting or monitoring the health of a system. This tutorial aims to equip you with knowledge specific to Red Hat Enterprise Linux (RHEL), helping you to efficiently manage and analyze these files. By the end of this guide, you will have a practical understanding of how to handle system logs and journal entries on a RHEL system.

## Step-by-Step Guide

### 1. Understanding System Logs and Journals

In RHEL, logs are primarily managed by two systems: traditional syslog and systemd's journal. The syslog service handles text messages for a variety of system activities, while systemd-journald captures detailed logging information about system operations, processes, and errors.

### 2. Locating System Logs

#### Traditional Log Files

System logs in RHEL are stored in `/var/log/`. Here are some of the most crucial log files:

- `/var/log/messages`: Contains global system messages, including the messages that are logged during system startup. This file includes information about the hardware and software events.
- `/var/log/secure`: Contains all security-related messages including authentication successes and failures.
- `/var/log/boot.log`: Logs details about system startup.
- `/var/log/dmesg`: Contains kernel ring buffer information, useful for troubleshooting hardware and driver issues.

To view the content of these logs, you can use commands like `cat`, `more`, `less`, etc. For instance, to view the system messages:

```bash
sudo less /var/log/messages
```

#### Systemd Journal

Systemd introduces the `journalctl` command to query and display messages from the journal, which is managed by `systemd-journald`.

To view the entire systemd journal:

```bash
sudo journalctl
```

To follow the end of the journal (similar to `tail -f`):

```bash
sudo journalctl -f
```

### 3. Detailed Code Examples

#### Filtering Logs by Time

To show journal entries from the current boot:

```bash
sudo journalctl -b
```

To display journal entries since a specific date and time:

```bash
sudo journalctl --since "2021-05-20 14:03:00"
```

#### Filtering Logs by Priority

System logs can be filtered by their priority which ranges from 0 (emergency) to 7 (debug). To display errors (priority 3) and higher:

```bash
sudo journalctl -p err..emerg
```

#### Combining Filters

You can combine multiple filters to narrow down your search. For example, to view all emergency to error logs since the last boot:

```bash
sudo journalctl -b -p err..emerg
```

#### Logs for Specific Processes or Units

To view logs for a specific unit, such as `sshd`:

```bash
sudo journalctl -u sshd
```

To see logs related to a specific process ID:

```bash
sudo journalctl _PID=1234
```

### 4. Exporting and Persisting Logs

To export log entries in JSON format:

```bash
sudo journalctl -b -o json-pretty
```

To ensure logs are persisted across reboots, make sure `/var/log/journal/` exists and systemd-journald is configured to store logs permanently:

```bash
sudo mkdir -p /var/log/journal
sudo systemd-tmpfiles --create --prefix /var/log/journal
sudo systemctl restart systemd-journald
```

## Conclusion

In this tutorial, we've covered how to locate, interpret, and manage system log files and journals in RHEL. Mastery of these skills will enhance your capability to maintain system health and troubleshoot issues effectively. Regularly checking system logs and understanding their contents is a best practice every system administrator should adopt.