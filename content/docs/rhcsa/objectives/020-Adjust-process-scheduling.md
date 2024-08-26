# Tech Tutorial: Operate Running Systems

## Introduction

In this tutorial, we will delve into the concept of process scheduling in operating systems. Process scheduling is a fundamental aspect that determines how processes share the CPU. This is crucial in a multi-tasking environment where efficiency and performance are key. We will explore how to adjust process scheduling to optimize the performance of different types of applications, such as those requiring more real-time responses or those that can afford some delays.

We will use Linux as the platform for demonstration because of its widespread use and robustness in handling multiple processes. By the end of this tutorial, you should be able to adjust process priorities using nice and renice commands, understand real-time priorities with `chrt`, and manipulate CPU affinities using `taskset`.

## Step-by-Step Guide

### 1. Understanding Process Priority

In Linux, every process is assigned a priority. The kernel uses these priorities to decide which process gets to use the CPU next. The `nice` value of a process determines its priority. The range of nice values is from -20 (highest priority) to 19 (lowest priority).

#### Checking Process Priority

To check the nice value of a running process, you can use the `top` command:

```bash
top
```

In the `NI` column, you'll see the nice value of each process.

### 2. Using `nice` and `renice`

#### Starting a Process with a Specific Nice Value

To start a new process with a specific nice value, use the `nice` command:

```bash
nice -n 10 command
```

This starts `command` with a nice value of 10.

#### Changing the Nice Value of an Existing Process

To change the nice value of a running process, use the `renice` command:

```bash
renice 5 -p 1234
```

This sets the nice value of the process with PID 1234 to 5.

### 3. Real-Time Scheduling with `chrt`

Linux supports real-time scheduling policies which are crucial for tasks where time constraints are strict. The `chrt` command can be used to manipulate real-time attributes.

#### Checking and Setting Real-Time Priorities

To see the real-time attributes of a process, use:

```bash
chrt -p PID
```

To set a process to a real-time scheduling policy with a specific priority:

```bash
chrt -f -p 99 PID
```

This sets the process with PID to FIFO real-time policy with the highest priority (99).

### 4. Setting CPU Affinity with `taskset`

CPU affinity is a scheduling property that binds a process to a given set of CPUs on the system, which can be useful for performance reasons.

#### Checking CPU Affinity

To check the CPU affinity of a process, use:

```bash
taskset -p PID
```

#### Setting CPU Affinity

To set a process to run only on the first CPU (CPU 0):

```bash
taskset -p 0x1 PID
```

### 5. Practical Example

Let's consider a scenario where you are running a web server (PID 2500) and a database server (PID 2600). The database server is more critical and should have a higher priority. 

Adjust the database server's priority and set its CPU affinity:

```bash
renice -5 -p 2600
taskset -p 0x1 2600
```

For the web server, ensure it does not interfere much with the database server:

```bash
renice 5 -p 2500
taskset -p 0x2 2500
```

## Conclusion

Adjusting process scheduling is a powerful tool in system administration that can help optimize application performance and responsiveness. By understanding and utilizing commands like `nice`, `renice`, `chrt`, and `taskset`, system administrators can fine-tune their systems based on the specific needs of their applications. This tutorial provided foundational knowledge and practical examples to get started with adjusting process scheduling. Experimenting on a test system can further enhance your understanding and skills in this area.