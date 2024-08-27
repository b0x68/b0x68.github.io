# Tech Tutorial: Operate Running Systems as a Red Hat Certified System Administrator

## Introduction

In the world of Linux administration, especially under the Red Hat Certified System Administrator (RHCSA) certification, one of the core competencies is the ability to operate running systems. This includes starting and stopping services, booting into different runlevels, scheduling tasks, and managing system performance. Mastery of these tasks ensures that the system administrator can maintain, troubleshoot, and control the everyday operations of a Red Hat Enterprise Linux (RHEL) system.

This tutorial aims to guide you through various essential tasks related to operating running systems, aligned with the RHCSA exam objectives. We will cover practical, real-world examples to equip you with the knowledge to perform these tasks efficiently.

## Step-by-Step Guide

### 1. Managing Services and Daemons

Services and daemons are background processes that start during boot or after logging into the system. Managing these services is crucial for system administrators.

#### Starting, Stopping, and Checking the Status of a Service

```bash
# To start a service:
sudo systemctl start httpd

# To stop a service:
sudo systemctl stop httpd

# To check the status of a service:
sudo systemctl status httpd
```

#### Enabling and Disabling Services at Boot

```bash
# To enable a service at boot:
sudo systemctl enable httpd

# To disable a service at boot:
sudo systemctl disable httpd
```

### 2. Managing System Performance

Understanding and controlling system resources is essential for maintaining the optimal performance of a system.

#### Viewing and Limiting CPU Usage

You can use the `top` command to view real-time CPU usage:

```bash
top
```

To limit CPU usage for a particular process, you can use the `cpulimit` tool. For example, to limit a process with PID 1234 to use only 50% of the CPU:

```bash
sudo cpulimit --pid 1234 --limit 50
```

#### Managing System Memory

Use the `free` command to check the available and used memory:

```bash
free -h
```

To clear the cache to free up the buffer/cache memory, you can run:

```bash
sudo sync; sudo echo 3 > /proc/sys/vm/drop_caches
```

### 3. Boot, Reboot, and Shut Down a System Safely

Knowing how to safely start and stop your system is crucial for preventing data loss and file system corruption.

```bash
# To reboot the system:
sudo systemctl reboot

# To shut down the system:
sudo systemctl poweroff
```

### 4. Scheduling Tasks Using Cron and At

Automating tasks to run at specific times can save a lot of time and effort.

#### Creating a Cron Job

Edit the crontab file for the current user:

```bash
crontab -e
```

Add a line to run a script every day at midnight:

```
0 0 * * * /path/to/script.sh
```

#### Using `at` to Schedule a One-Time Task

To run a script at 10:00 AM on July 31:

```bash
echo "/path/to/script.sh" | at 10:00 July 31
```

## Conclusion

In this tutorial, we've covered crucial aspects of operating running systems on RHEL, aligned with the RHCSA exam objectives. By mastering these tasks, you can ensure the smooth operation of Linux systems, manage resources effectively, and automate necessary tasks to optimize performance and efficiency.

Practice these commands and scenarios to build your confidence and deepen your understanding as you prepare for the RHCSA exam or manage real-world Linux environments.