# Tech Tutorial: Operate Running Systems - Manage Tuning Profiles

## Introduction

In this tutorial, we will cover the management of tuning profiles on Red Hat Enterprise Linux (RHEL), which is an essential skill for the Red Hat Certified System Administrator (RHCSA) exam. Tuning profiles help you optimize system performance by adjusting various system parameters according to the specific needs of your workload.

RHEL uses `tuned`, a dynamic adaptive system tuning daemon that tunes system settings dynamically depending on usage. It also allows for the application of predefined tuning profiles, which are sets of rules and parameters that govern how the system resources are allocated and managed.

## Prerequisites

- A Red Hat Enterprise Linux 8 or later installed.
- Sufficient privileges (root or sudo access) to make system changes.

## Step-by-Step Guide

### Step 1: Installing Tuned

First, ensure that the `tuned` service is installed and running on your system. You can install `tuned` using the following command:

```bash
sudo dnf install tuned
```

After installation, enable and start the `tuned` service:

```bash
sudo systemctl enable --now tuned
```

### Step 2: Listing Available Profiles

To see what tuning profiles are available on your system, use:

```bash
tuned-adm list
```

This command will display a list of all available profiles. Each profile is designed for specific types of workloads or hardware configurations.

### Step 3: Viewing the Current Active Profile

To check which tuning profile is currently active, execute:

```bash
tuned-adm active
```

This command will show you the currently active profile.

### Step 4: Selecting a Tuning Profile

To change the tuning profile, use the `tuned-adm` command followed by the profile you wish to apply. For example, to switch to the `network-latency` profile, which is optimized for low-latency network tuning, run:

```bash
sudo tuned-adm profile network-latency
```

Confirm the profile change by checking the active profile again:

```bash
tuned-adm active
```

### Step 5: Customizing Tuning Profiles

If the available profiles do not meet your specific needs, you can create a custom tuning profile. First, create a new profile directory in `/etc/tuned/`:

```bash
sudo mkdir /etc/tuned/my-custom-profile
```

Create a configuration file named `tuned.conf` inside your custom profile directory:

```bash
sudo nano /etc/tuned/my-custom-profile/tuned.conf
```

Here’s an example content for `tuned.conf`:

```plaintext
[main]
include=throughput-performance

[sysctl]
net.ipv4.tcp_tw_recycle = 1
net.ipv4.tcp_tw_reuse = 1

[vm]
transparent_hugepages=never
```

This configuration inherits settings from the `throughput-performance` profile and modifies some kernel parameters and virtual memory settings.

Activate your custom profile using:

```bash
sudo tuned-adm profile my-custom-profile
```

### Step 6: Checking the Effect of Tuning Profiles

To verify the changes made by tuning profiles, you can use tools like `sysctl` or `cat` to check system parameters. For example:

```bash
sysctl net.ipv4.tcp_tw_recycle
sysctl net.ipv4.tcp_tw_reuse
cat /sys/kernel/mm/transparent_hugepage/enabled
```

## Conclusion

Managing tuning profiles in RHEL using `tuned` is a powerful way to optimize system performance for specific workloads. By understanding how to list, apply, and customize tuning profiles, you can significantly improve the efficiency and responsiveness of your systems. Always test changes in a controlled environment before applying them to production systems to ensure that there are no unintended side effects.

Remember, the right tuning profile can lead to substantial performance improvements, making it a vital skill for any system administrator, especially those preparing for the RHCSA exam.