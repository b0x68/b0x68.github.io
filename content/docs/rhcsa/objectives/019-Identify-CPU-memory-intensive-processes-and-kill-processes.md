# Tech Tutorial: Operate Running Systems

## Introduction

Managing system resources efficiently is crucial for maintaining the performance and stability of Red Hat Enterprise Linux (RHEL) servers. This tutorial will guide you through identifying and managing CPU and memory-intensive processes, which is essential for any systems administrator preparing for the Red Hat Certified System Administrator (RHCSA) exam.

Understanding how to monitor system resources and address processes that are using an excessive amount of these resources will help you maintain the health of your RHEL systems and ensure they are performing optimally.

## Step-by-Step Guide

### 1. Identifying CPU/Memory Intensive Processes

#### Using `top`

`top` is a powerful utility in RHEL that provides a dynamic, real-time view of a running system. It shows a list of processes and their CPU and memory usage.

To start `top`, simply type the following in your terminal:

```bash
top
```

Once `top` is running, you can see a list of all the processes, with the most resource-intensive processes shown at the top. By default, processes are sorted by their CPU usage, but you can change this to sort by memory by pressing `Shift + M`.

#### Using `ps`

While `top` provides a dynamic view, `ps` is used for capturing a snapshot of current processes. To view processes with their CPU and memory usage, you can use:

```bash
ps aux --sort=-%cpu,-%mem
```

This command lists all running processes, sorted by CPU and memory usage in descending order.

### 2. Killing Processes

Once you've identified a process that is consuming too many resources, you may decide to kill it to free up system resources. This should be done with caution, as killing essential system processes can lead to system instability.

#### Using `kill`

To kill a process, you need its PID (Process ID). Suppose the PID is 1234; you can kill it with:

```bash
kill 1234
```

This sends SIGTERM, asking the process to terminate cleanly. If the process does not terminate, you might need to use:

```bash
kill -9 1234
```

This sends SIGKILL, which forcefully terminates the process. Use SIGKILL as a last resort.

#### Using `pkill`

`pkill` allows you to kill processes by name, which is useful if you do not know the PID. For example, to kill all processes named `myapp`, use:

```bash
pkill myapp
```

Like `kill`, `pkill` sends SIGTERM by default. To forcefully kill processes, use:

```bash
pkill -9 myapp
```

### 3. Detailed Code Examples

#### Monitoring and Killing a Specific Process

Suppose a process named `myapp` is known to occasionally consume excessive CPU resources. You want to monitor its resource usage and kill it if necessary. Here’s how you might script this:

```bash
#!/bin/bash

# Monitor the myapp process
top -b -n 1 | grep myapp

# If CPU usage of myapp exceeds 80%, kill it
cpu_usage=$(ps aux | grep myapp | awk '{print $3}' | head -n 1)

if (( $(echo "$cpu_usage > 80" | bc -l) )); then
    echo "CPU usage is above 80%; killing myapp"
    pkill -9 myapp
else
    echo "CPU usage is under control"
fi
```

This script first checks the CPU usage of `myapp`, and if it exceeds 80%, it forcefully kills the process.

## Conclusion

In this tutorial, we've covered how to identify and kill CPU/memory-intensive processes in RHEL. These skills are fundamental for systems administration, especially when managing servers that are prone to high loads. By efficiently monitoring and managing system resources, you can ensure that your RHEL servers remain stable and perform well under various conditions.

Remember, always verify the importance of a process before deciding to kill it, as terminating critical system processes can lead to unintended consequences.