# Tech Tutorial: Operate Running Systems

## Introduction

In this tutorial, we will delve into an essential aspect of system administration for Red Hat Enterprise Linux (RHEL)—adjusting process scheduling. This topic is significant for the Red Hat Certified System Administrator (RHCSA) exam and for anyone looking to optimize the performance of their RHEL systems.

Understanding and adjusting process scheduling allows system administrators to fine-tune the system’s responsiveness and efficiency, particularly in environments with high load or specific performance requirements.

## Step-by-Step Guide

### Understanding Process Priority and Niceness

In Linux, each process is assigned a priority level, and within RHEL, you can adjust this priority using the `nice` and `renice` commands. The "niceness" ranges from -20 (highest priority) to 19 (lowest priority).

1. **Viewing Current Process Priorities**

   To view the priorities of running processes, you can use the `top` or `ps` command. The `NI` column shows the niceness level.

   ```bash
   top
   ```

   Or:

   ```bash
   ps -el | head -1; ps -el | grep [process_name]
   ```

   Replace `[process_name]` with the actual name of the process to filter the output.

2. **Changing Process Priority**

   To change the priority of a running process, use the `renice` command.

   ```bash
   sudo renice -n 10 -p [PID]
   ```

   Replace `[PID]` with the Process ID of the process you want to re-prioritize. This command sets the niceness of the process to 10.

### Setting Real-Time Priorities with `chrt`

For processes that require real-time execution characteristics, `chrt` (change real-time attributes) is used.

1. **Viewing Real-Time Attributes**

   To see the real-time attributes of a process, use:

   ```bash
   chrt -p [PID]
   ```

   Replace `[PID]` with the Process ID of the process.

2. **Setting Real-Time Scheduling Policy**

   There are different scheduling policies available: SCHED_FIFO, SCHED_RR, and SCHED_OTHER. To set a process to real-time with the FIFO policy:

   ```bash
   sudo chrt -f -p 99 [PID]
   ```

   This sets the process with PID `[PID]` to a FIFO real-time scheduling policy with the highest priority (99).

## Detailed Code Examples

Let’s consider a scenario where we have a Java application that needs more priority over other processes.

1. **Identifying the Process ID**

   Suppose the application is named `MyJavaApp`.

   ```bash
   ps -ef | grep MyJavaApp
   ```

   Assume the output gives us a PID of 1234.

2. **Increasing Priority**

   Increase the priority by setting a lower niceness.

   ```bash
   sudo renice -n -5 -p 1234
   ```

   Check the priority change:

   ```bash
   ps -el | grep 1234
   ```

3. **Setting to Real-Time**

   If the application needs real-time execution:

   ```bash
   sudo chrt -r -p 80 1234
   ```

   Validate the change:

   ```bash
   chrt -p 1234
   ```

## Conclusion

Adjusting process scheduling in RHEL can significantly impact the performance and behavior of applications and processes. By mastering the use of `nice`, `renice`, and `chrt`, you gain finer control over how CPU time is distributed among processes, which is crucial for optimizing system performance. Remember that improper use of these tools, especially with real-time settings, can lead to system instability if not managed carefully. Always test changes in a controlled environment before applying them in a production setting.