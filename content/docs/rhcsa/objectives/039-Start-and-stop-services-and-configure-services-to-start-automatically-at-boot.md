# Tech Tutorial: Deploy, Configure, and Maintain Systems

## Exam Objective: Start and Stop Services and Configure Services to Start Automatically at Boot

In this tutorial, we'll explore how to manage services on a Linux system, which is a crucial skill for system administrators and IT professionals. We'll focus on starting, stopping services, and configuring them to start automatically at boot. This guide will use `systemd`, the most common init system and service manager in modern Linux distributions like CentOS, Debian, and Ubuntu.

### Introduction

In Linux, a 'service' is an application (or a set of applications) that runs in the background waiting to be used or performing essential tasks. Proper management of these services is vital for system stability and performance.

### Prerequisites

- A Linux system with `systemd` installed.
- Sudo or root access on the system.

### Step-by-Step Guide

#### 1. Understanding Systemd

`systemd` is an init system that initializes the components that must be started after the Linux kernel is booted. It also manages services and daemons at any point while the system is running. 

#### 2. Checking the Status of Services

Before starting or stopping services, it's essential to understand how to check their status.

```bash
# Check the status of a specific service, e.g., Apache HTTP Server
sudo systemctl status apache2
```

This command provides detailed output, including whether the service is active, loaded, and enabled to start on boot, plus recent log entries.

#### 3. Starting and Stopping Services

To start or stop a service, use `systemctl` followed by the command `start` or `stop`.

```bash
# Start a service
sudo systemctl start apache2

# Stop a service
sudo systemctl stop apache2
```

#### 4. Enabling and Disabling Services

If you want a service to start automatically at boot, you need to 'enable' it. Conversely, if you don't want the service to start on boot, you should 'disable' it.

```bash
# Enable a service to start on boot
sudo systemctl enable apache2

# Disable a service from starting on boot
sudo systemctl disable apache2
```

#### 5. Restarting and Reloading Services

Sometimes, you may need to restart a service after making configuration changes. Alternatively, if the service supports it, you can reload it to apply changes without interrupting the running service.

```bash
# Restart a service
sudo systemctl restart apache2

# Reload a service, if supported
sudo systemctl reload apache2
```

### Detailed Code Examples

Let's consider a real-world scenario where we configure a new service, such as a custom Node.js application, to start automatically and manage it using `systemd`.

#### Creating a systemd Service File for Your Node.js App

1. **Create a service file** `/etc/systemd/system/myapp.service`:

```ini
[Unit]
Description=My Node.js App
After=network.target

[Service]
Type=simple
User=nodeuser
ExecStart=/usr/bin/node /path/to/myapp/app.js
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

2. **Reload systemd to recognize new service**:
    ```bash
    sudo systemctl daemon-reload
    ```

3. **Enable and start your service**:
    ```bash
    sudo systemctl enable myapp
    sudo systemctl start myapp
    ```

4. **Check the status of your service**:
    ```bash
    sudo systemctl status myapp
    ```

### Conclusion

Understanding how to manage services with `systemd` is a fundamental skill for anyone administering Linux systems. By mastering the commands and steps outlined in this tutorial, you can ensure that your services are running as expected and configured correctly for your environment's needs.

Feel free to adapt the examples to fit the specific services and applications in your own Linux environment. Remember, practice and experimentation are key to mastering Linux service management.