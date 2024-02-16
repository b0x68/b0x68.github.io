+++
title = "Adjust process scheduling"
date = "2024-02-16T10:31:38-05:00"
author = "root"
cover = ""
tags = ["linux", "command,", "user", "scheduler", "tasks:", "command.", "system's", "/etc/security/limits.conf'"]
keywords = ["commands", "process,", "tasks:", "systemd", "process", "swap:", "processes", "processes."]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Tutorial: Adjusting Process Scheduling in Red Hat Certified Systems Administrator Exam 200 Objective

In this tutorial, we will be exploring the objective of adjusting process scheduling in the Red Hat Certified Systems Administrator Exam 200. This objective falls under the "System Management" category and holds a weight of 4% on the overall exam.

Process scheduling refers to the mechanism by which a computer's operating system decides which process should be allocated CPU time. It is an essential component of the operating system and plays a crucial role in managing system resources efficiently.

In Red Hat Enterprise Linux (RHEL), there are various tools and techniques available for adjusting process scheduling. In this tutorial, we will cover the following topics:

1. Process Scheduling Overview
2. Types of Process Scheduling
3. Adjusting Process Scheduling using 'nice' and 'renice' commands
4. Monitoring and Managing Process Scheduling using 'top' command
5. Global Process Scheduling Settings

## 1. Process Scheduling Overview

As mentioned earlier, process scheduling is the mechanism by which the operating system decides which process gets to use the CPU next. It ensures that the system resources are allocated efficiently and fairly among all the active processes.

In RHEL, the Linux scheduler is responsible for managing process scheduling. It uses algorithms to determine the priority of each process and assigns CPU time accordingly.

## 2. Types of Process Scheduling

There are two types of process scheduling in RHEL:

- time-sharing: In this type, the CPU time is shared between multiple processes based on their priority.
- real-time: This type is used for applications that require a guaranteed amount of CPU time at a specific time. These processes have a higher priority over time-sharing processes.

It is important to note that the scheduler can be adjusted to favor one type of scheduling over the other, depending on the system's need.

## 3. Adjusting Process Scheduling using 'nice' and 'renice' commands

The 'nice' and 'renice' commands are used to adjust the priority of a process. They are used to change the "niceness" value, which determines the priority of a process in the time-sharing scheduling policy.

The 'nice' command is used when starting a new process, and the 'renice' command is used to alter the niceness value of an already running process.

To set a higher niceness value (lower priority) for a process, use the following command:

```
nice +[value] [command]
```

For example, to start a new process with a low priority, we can use the following command:
```
nice +10 top
```

This will start the 'top' command with a niceness value of 10, giving it a lower priority over other processes.

To change the niceness value of a running process, we use the 'renice' command. The syntax is as follows:
```
renice [value] [PID]
```

Here, the PID is the process ID of the process that we want to modify. For example, to increase the priority of a process with PID 1234, we can use the following command:
```
renice -5 1234
```

## 4. Monitoring and Managing Process Scheduling using 'top' command

The 'top' command is a useful tool for monitoring and managing process scheduling. It displays the list of currently running processes and their respective resource utilization, including CPU usage and priority.

To launch the 'top' command, open the terminal and type 'top' in the prompt. Here's an example output of the command:

```
Tasks: 117 total, 2 running, 115 sleeping, 0 stopped, 0 zombie
%Cpu(s): 0.5 us, 0.2 sy, 0.0 ni, 99.3 id, 0.0 wa, 0.0 hi, 0.0 si, 0.0 st
KiB Mem :  8005116 total,  1723880 free,  3787972 used,  2493264 buff/cache
KiB Swap:  7812092 total,  7812092 free,        0 used.  3618852 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
 2221 root      20   0  643904  37416  15028 S   0.6  0.5   0:29.89 Xorg
 5352 smith     20   0 1065660  83744  45752 S   0.6  1.0   0:09.07 gnome-online-acc
    1 root      20   0  170740   6364   3728 S   0.0  0.1   0:03.21 systemd
```

From the above output, we can see the niceness value under the "NI" column. We can also use the 'F' (capital F) command to change the fields displayed and add the "NI" column to the output.

## 5. Global Process Scheduling Settings

In RHEL, the global process scheduling settings can be modified by editing the ' /etc/security/limits.conf' file. The parameters that can be adjusted include 'nice', 'rtpriority', 'priority', and 'memlock'.

It is recommended to consult the official RHEL documentation for more information on these parameters and their acceptable values.

## Conclusion

In this tutorial, we have covered the 'Adjust Process Scheduling' objective of the Red Hat Certified Systems Administrator Exam 200 in great depth. We have discussed the basics of process scheduling, two types of scheduling, and different tools and techniques for adjusting it.

By mastering the concepts covered in this tutorial, you will be well-prepared to tackle any questions related to process scheduling on the exam. Make sure to practice and familiarize yourself with the different commands and their usage to gain confidence in this objective. 