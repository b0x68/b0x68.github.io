# Tech Tutorial: Operate Running Systems

## Introduction

In the course of managing or troubleshooting computing systems, especially under a Linux-based environment, it becomes vital to understand how to monitor and manage system resources effectively. A common task in this realm is identifying and managing processes, particularly those that consume excessive amounts of CPU or memory. This tutorial aims to equip you with the necessary skills to identify CPU/memory intensive processes and efficiently terminate them if needed, using command-line tools available in most Linux distributions.

## Step-by-Step Guide

### 1. Understanding Process Management

Before diving into process termination, it's essential to understand what processes are and how they work in Linux. A process is an instance of a running program and is the fundamental unit of execution in the operating system. Linux provides various tools to manage and monitor these processes.

### 2. Identifying CPU/Memory Intensive Processes

#### Using `top`

The `top` command is one of the most versatile and widely used tools for real-time process monitoring. It provides a dynamic, real-time view of a running system.

```bash
top
```

Once you run `top`, it will show a list of all running processes along with useful information such as CPU usage, memory usage, PID (Process ID), and process owner. CPU and memory intensive processes typically appear at the top of this list, sorted by their CPU usage by default.

#### Using `htop`

An enhanced version of `top`, `htop` provides a more user-friendly and colorful interface for monitoring processes. It also allows you to scroll vertically and horizontally, so you can easily view all the processes running on the system.

```bash
# First, install htop using package manager, if it's not installed:
sudo apt install htop  # For Debian/Ubuntu
sudo yum install htop  # For CentOS/Fedora

# Then, run htop
htop
```

#### Using `ps` and `awk`

For more specific tasks, such as fetching the top 5 memory-consuming processes, you can use a combination of `ps` and `awk`.

```bash
ps aux --sort=-%mem | head -n 6
```

This command lists all processes along with their details, sorts them by memory usage in descending order, and then uses `head` to fetch the top entries.

### 3. Killing Processes

Once you have identified a problematic process, you may decide to terminate it. The `kill` command is used to send signals to a process, with various signals available for different purposes. The most common signal for terminating a process is SIGTERM (signal number 15).

#### Using `kill`

To kill a process with a specific PID:

```bash
kill 12345
```

Replace `12345` with the actual PID of the process. If the process does not stop, you can use SIGKILL (signal number 9), which forcefully stops the process but should be used as a last resort:

```bash
kill -9 12345
```

#### Using `pkill`

If you want to kill processes by name, `pkill` is very useful:

```bash
pkill -f firefox
```

This command will terminate all processes with 'firefox' in the name.

## Conclusion

Understanding how to monitor and manage processes in a Linux environment is crucial for system administration and troubleshooting. By using tools like `top`, `htop`, `ps`, and `kill`, you can effectively manage system resources and ensure that your systems run smoothly and efficiently. Always consider the implications of killing a process and use SIGKILL sparingly, as it does not allow the process to clean up after itself.

This tutorial should give you a solid foundation in handling CPU/memory intensive processes, contributing to your overall ability to manage and maintain running systems effectively.