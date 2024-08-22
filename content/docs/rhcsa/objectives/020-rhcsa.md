# Tech Tutorial: Operate Running Systems - Adjust Process Scheduling

## Introduction

In the realm of system administration and performance optimization, process scheduling is a fundamental aspect that determines how efficiently a computer system runs multiple processes. This tutorial aims to explore how we can adjust and optimize process scheduling on a Linux system. We'll delve into practical examples using the `nice` and `renice` commands, which are crucial for prioritizing processes and thus enhancing the system's overall performance.

## Step-by-Step Guide

### Prerequisites

To follow along with this tutorial, you will need:
- A Linux-based operating system.
- Basic understanding of the command line interface.
- Optional: Access to a root or sudo user account for certain operations.

### Understanding Process Priority

In Linux, every process has an associated 'niceness' value which affects its priority on the CPU. The niceness values range from -20 (highest priority) to 19 (lowest priority). A lower niceness value means higher priority, and the kernel is more likely to allocate CPU time to it.

### 1. Viewing Process Priorities

Before adjusting any process priority, it's essential to view the current priorities. You can do this using the `top` command:

```bash
top
```

Inside the `top` output, look for the `NI` column which represents the niceness value of each process.

### 2. Changing Process Priority with `nice`

To start a new process with a specific niceness, use the `nice` command. For example, to start a script with a lower priority:

```bash
nice -n 10 ./your_script.sh
```

This sets the script's niceness to 10, making it less prioritized compared to other processes with lower niceness values.

### 3. Modifying Priority of Running Processes with `renice`

To change the priority of an already running process, use the `renice` command. First, you'll need to find out the process ID (PID), which can be done using `ps` or `pgrep`. For example, to find the PID of a running instance of `your_script.sh`:

```bash
pgrep -f your_script.sh
```

Assuming the PID is 1234, to change its niceness to 5:

```bash
renice 5 -p 1234
```

### 4. Confirming Changes

Verify that the niceness of the process has been changed by using `top` or `ps`:

```bash
ps -o pid,ni,cmd -p 1234
```

This will display the PID, niceness, and command line of the process with PID 1234.

## Detailed Code Examples

Here's a script example that demonstrates starting multiple instances of a script with different priorities and adjusting them dynamically:

```bash
#!/bin/bash

# Start a process with default priority
./long_running_process.sh &
pid1=$!

# Start a process with higher priority
nice -n -5 ./cpu_intensive_task.sh &
pid2=$!

# Display current niceness
ps -o pid,ni,cmd -p $pid1 -p $pid2

# Change niceness of the first process
renice 10 -p $pid1

# Confirm changes
ps -o pid,ni,cmd -p $pid1 -p $pid2
```

This script runs two processes and adjusts the priority of one, providing an easy way to see the impact of process priority adjustments.

## Conclusion

Adjusting process scheduling is a powerful way to manage system resources effectively. By using `nice` and `renice`, system administrators can ensure critical tasks have the necessary CPU time compared to less important processes. This becomes particularly crucial in multi-user environments or servers where resource allocation can significantly impact performance and user experience. Always consider the overall system load and the importance of each process before making adjustments to process priorities.