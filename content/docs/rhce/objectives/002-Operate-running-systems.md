# Tech Tutorial: Operate Running Systems for the Red Hat Certified System Administrator (RHCSA)

## Introduction

In preparing for the Red Hat Certified System Administrator (RHCSA) exam, it's essential to gain a thorough understanding of how to operate running systems. This component of the exam requires proficiency in managing systems day-to-day, handling services, processes, and system tuning. This tutorial will guide you through common tasks you'll need to perform under this objective using only Red Hat Enterprise Linux (RHEL) commands and configurations.

## Step-by-Step Guide

### 1. Managing Services with `systemctl`

`systemctl` is the primary tool for managing services on RHEL. It allows you to start, stop, restart, reload, enable, and disable services.

#### Starting and Stopping Services

To start a service:

```bash
sudo systemctl start [service_name]
```

To stop a service:

```bash
sudo systemctl stop [service_name]
```

For example, to start and then stop the Apache HTTP Server:

```bash
sudo systemctl start httpd
sudo systemctl stop httpd
```

#### Enabling and Disabling Services

To enable a service to start at boot:

```bash
sudo systemctl enable [service_name]
```

To disable it:

```bash
sudo systemctl disable [service_name]
```

For instance, to enable and then disable `sshd`:

```bash
sudo systemctl enable sshd
sudo systemctl disable sshd
```

### 2. Managing System Processes

Understanding how to manage system processes is crucial. You can use `ps`, `top`, `kill`, and other utilities.

#### Viewing Active Processes

To display active processes:

```bash
ps aux
```

To get a real-time display of system processes:

```bash
top
```

#### Killing Processes

To stop a process, you first need its PID, which you can find using `ps`:

```bash
ps aux | grep [process_name]
```

Then, use `kill` to terminate the process by its PID:

```bash
sudo kill [PID]
```

For a forceful termination, use:

```bash
sudo kill -9 [PID]
```

### 3. System Tuning with `tuned`

`tuned` is a dynamic adaptive system tuning daemon that tunes system settings dynamically depending on usage. To adjust system profiles for various scenarios like throughput or power consumption:

#### List Available Profiles

```bash
tuned-adm list
```

#### Activate a Profile

```bash
sudo tuned-adm profile [profile_name]
```

For example, to set the system for maximum performance:

```bash
sudo tuned-adm profile throughput-performance
```

### 4. Configuring Logging with `rsyslog`

System logging is managed in RHEL with `rsyslog`. Configuring it correctly ensures that you have access to vital system and service logs.

#### Viewing Logs

Logs are stored in `/var/log/`. For instance, to view system messages:

```bash
sudo less /var/log/messages
```

#### Configuring `rsyslog`

Edit the configuration file to define what data gets logged and where:

```bash
sudo vi /etc/rsyslog.conf
```

You can add lines such as:

```conf
*.info;mail.none;authpriv.none;cron.none                /var/log/messages
```

This example directs all info-level messages to `/var/log/messages`, excluding mail, authpriv, and cron messages.

## Conclusion

The ability to operate running systems effectively is a fundamental skill for any Red Hat Certified System Administrator. This tutorial covered essential tasks such as managing services, handling system processes, tuning systems with `tuned`, and configuring system logging with `rsyslog`. Mastery of these skills will not only help you in your RHCSA exam but also in real-world scenarios where system reliability and performance are critical. Practice these commands and configurations to deepen your understanding and proficiency.