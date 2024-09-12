# Tech Tutorial: Operate Running Systems for RHCSA

## Introduction

This tutorial is specifically designed to help prospective Red Hat Certified System Administrators (RHCSA) master the essential skills required to operate running systems, one of the key objectives of the RHCSA exam. This guide focuses on using Red Hat Enterprise Linux (RHEL) commands to manage running systems effectively.

In this tutorial, we will cover how to manage system services, configure SSH, monitor system logs, and manage processes. Each section will include step-by-step guidance and detailed examples to ensure you can apply these skills in real-world scenarios.

## Step-by-Step Guide

### 1. Managing System Services with `systemctl`

System services in RHEL are managed primarily through the `systemctl` command, part of the systemd suite, which is the init system and service manager in RHEL 7 and later versions.

#### Starting, Stopping, and Checking the Status of Services

To manage services, you need to know how to start, stop, restart, and check their status. Here’s how you do it:

- **Start a service:**
  ```bash
  sudo systemctl start httpd.service
  ```

- **Stop a service:**
  ```bash
  sudo systemctl stop httpd.service
  ```

- **Restart a service:**
  ```bash
  sudo systemctl restart httpd.service
  ```

- **Check the status of a service:**
  ```bash
  sudo systemctl status httpd.service
  ```
  This command provides detailed output, including whether the service is active, loaded, and enabled on boot, along with recent log entries.

- **Enable a service to start at boot:**
  ```bash
  sudo systemctl enable httpd.service
  ```

- **Disable a service from starting at boot:**
  ```bash
  sudo systemctl disable httpd.service
  ```

### 2. Configuring SSH for Secure Remote Access

Secure Shell (SSH) is a protocol used to securely connect to remote systems. RHEL uses `sshd`, the SSH daemon, to listen for incoming connections.

- **Install the SSH package:**
  ```bash
  sudo yum install openssh-server
  ```

- **Start and enable the SSH service:**
  ```bash
  sudo systemctl start sshd.service
  sudo systemctl enable sshd.service
  ```

- **Configuring SSH:**
  Edit the SSH configuration file `/etc/ssh/sshd_config` using a text editor like `vi`:
  ```bash
  sudo vi /etc/ssh/sshd_config
  ```
  Make necessary changes such as changing the default port, disabling root login (`PermitRootLogin no`), and then save the file.

- **Restart the SSH service to apply changes:**
  ```bash
  sudo systemctl restart sshd.service
  ```

### 3. Monitoring System Logs with `journalctl`

System logs are crucial for diagnosing problems and monitoring system activity.

- **View system logs:**
  ```bash
  sudo journalctl
  ```

- **Filter logs by service:**
  ```bash
  sudo journalctl -u httpd.service
  ```

- **Show logs since the last boot:**
  ```bash
  sudo journalctl -b
  ```

### 4. Managing Processes

Understanding how to manage system processes is crucial for system administration.

- **List all running processes:**
  ```bash
  ps aux
  ```

- **Kill a process with `kill`:**
  To kill a process, you first need its PID. Use `ps` to find it, then:
  ```bash
  sudo kill [PID]
  ```

- **Using `top` to monitor active processes:**
  ```bash
  top
  ```
  `top` provides a dynamic real-time view of running processes. Use `Shift + P` to sort by CPU usage and `Shift + M` to sort by memory usage.

## Conclusion

In this tutorial, we covered essential tasks that every Red Hat Certified System Administrator should be able to perform to manage and operate running systems. Mastering these tasks will not only help you pass the RHCSA exam but also provide a strong foundation for real-world system administration on RHEL systems.

By understanding and practicing these commands and procedures, you'll be better equipped to handle the responsibilities of a Red Hat Certified System Administrator. Remember, consistent practice and exploration are key to mastering Linux system administration.