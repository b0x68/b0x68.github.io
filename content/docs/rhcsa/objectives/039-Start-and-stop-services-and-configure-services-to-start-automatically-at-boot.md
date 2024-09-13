# Tech Tutorial: Deploy, Configure, and Maintain Systems - Managing Services on RHEL

## Introduction

In this tutorial, we will focus on a critical aspect of managing Red Hat Enterprise Linux (RHEL) systems, particularly starting, stopping, and configuring services to start automatically at boot. This skill is essential for system administrators as services control how the Linux system behaves at runtime and ensures necessary applications and functions are available when the system is in use.

### What are Services?

In Linux, a service (or daemon) is a background process that is designed to run independently of user sessions. These services include web servers, database servers, and system services like logging, scheduling, and printing.

### Systemd and systemctl

RHEL 7 and later versions use `systemd` as the init system, which provides a system and service manager that runs as PID 1 and starts the rest of the system. `systemd` uses a command called `systemctl` to control the state of `systemd` services.

## Step-by-Step Guide

### 1. Checking the Status of a Service

To check the status of a service on RHEL, you can use the `systemctl status` command. For instance, to check the status of the HTTPD (Apache web server), you would use:

```bash
sudo systemctl status httpd
```

This command provides detailed output including whether the service is active, loaded, enabled, and any recent log entries.

### 2. Starting and Stopping Services

To start a service immediately, use the `systemctl start` command:

```bash
sudo systemctl start httpd
```

Stopping a service is just as straightforward:

```bash
sudo systemctl stop httpd
```

### 3. Enabling and Disabling Services at Boot

To ensure a service starts automatically at boot, you must enable it:

```bash
sudo systemctl enable httpd
```

This command creates a symbolic link from the service's script in `/etc/systemd/system/` to the appropriate directory under `/etc/systemd/system/`. If you decide that you don’t want the service to start at boot anymore, you can disable it:

```bash
sudo systemctl disable httpd
```

This removes the symbolic link.

### 4. Restarting and Reloading Services

If you need to restart a service (stop and then start), you can use:

```bash
sudo systemctl restart httpd
```

If the service supports reloading configuration files without interrupting active processes, you can use:

```bash
sudo systemctl reload httpd
```

## Detailed Code Examples

Let's go through a real-world scenario where we configure a new RHEL system to run a web server that needs to start automatically at boot.

1. **Install the HTTPD Service**:

   First, we need to install the Apache HTTP Server:

   ```bash
   sudo yum install httpd
   ```

2. **Start and Enable HTTPD Service**:

   ```bash
   sudo systemctl start httpd
   sudo systemctl enable httpd
   ```

3. **Verify the Service is Running and Enabled**:

   ```bash
   sudo systemctl status httpd
   ```

   Look for `active (running)` in the output and `enabled` to confirm that it’s set to start at boot.

4. **Configure HTTPD to Serve a Custom Website**:

   Edit the configuration file and add your website details. Usually, you might edit `/etc/httpd/conf/httpd.conf` or add files under `/etc/httpd/conf.d/`.

5. **Reload the HTTPD Configuration**:

   After making configuration changes, reload the service to apply them without stopping the service:

   ```bash
   sudo systemctl reload httpd
   ```

## Conclusion

Managing services effectively on RHEL using `systemctl` is a foundational skill for any system administrator. This tutorial covered how to start, stop, enable, disable, restart, and reload services. Mastery of these commands ensures you can keep essential services running smoothly and respond effectively to changes in system configuration or requirements. Remember, careful management of services is critical to maintaining the reliability and security of your Linux environment.