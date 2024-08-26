# Tech Tutorial: Operate Running Systems – Manage Tuning Profiles

## Introduction

Performance tuning is a critical aspect of system administration that involves optimizing system parameters to improve the performance based on the specific workload requirements. In this tutorial, we will explore how to manage tuning profiles on Linux systems using `tuned`, a dynamic adaptive system tuning daemon. `tuned` allows you to switch between different tuning profiles to adapt the system performance as per the workload.

## Prerequisites

- A Linux system with `tuned` installed. You can install `tuned` on most distributions using the package manager. For instance, on RHEL and CentOS, you can install it using:
  ```bash
  sudo yum install tuned
  ```
- Basic understanding of Linux command line.

## Step-by-Step Guide

### Step 1: Checking the Status of Tuned

First, ensure that the `tuned` service is running on your system. You can check the status of `tuned` by running:

```bash
sudo systemctl status tuned
```

If it's not running, you can start it with:

```bash
sudo systemctl start tuned
```

And enable it to start at boot with:

```bash
sudo systemctl enable tuned
```

### Step 2: Listing Available Tuning Profiles

To view all available tuning profiles, use the following command:

```bash
tuned-adm list
```

This will list all the profiles that `tuned` supports. Common profiles include:

- **balanced** – General non-specific tuning that improves performance while maintaining power efficiency.
- **powersave** – Maximizes power efficiency.
- **throughput-performance** – Optimizes for throughput at the expense of power consumption.
- **latency-performance** – Optimizes for low latency at the expense of power consumption.
- **network-latency** – Optimizes for low network latency.
- **network-throughput** – Optimizes for high network throughput.

### Step 3: Selecting a Tuning Profile

To select a tuning profile, use:

```bash
sudo tuned-adm profile [profile-name]
```

For example, to set the system to the `throughput-performance` profile, you would run:

```bash
sudo tuned-adm profile throughput-performance
```

### Step 4: Creating a Custom Tuning Profile

If the available profiles do not meet your specific needs, you can create a custom profile. Here’s how to do it:

1. **Create a new profile directory**:
   ```bash
   sudo mkdir /etc/tuned/my-custom-profile
   ```
   
2. **Create a `tuned.conf` file in this directory**:
   ```bash
   sudo nano /etc/tuned/my-custom-profile/tuned.conf
   ```

3. **Add configuration parameters**. For example:
   ```plaintext
   [main]
   include=throughput-performance

   [sysctl]
   net.core.rmem_max=4194304
   net.core.wmem_max=4194304
   ```

   This example creates a new profile based on the existing `throughput-performance` profile but changes the maximum read and write buffer sizes.

4. **Activate the new profile**:
   ```bash
   sudo tuned-adm profile my-custom-profile
   ```

### Step 5: Verifying the Changes

After applying a profile, you should verify that the changes are in effect. You can inspect the current active profile and system variables by using:

```bash
tuned-adm active
sysctl net.core.rmem_max
sysctl net.core.wmem_max
```

## Conclusion

In this tutorial, we explored how to manage system performance through tuning profiles using `tuned` in a Linux environment. We discussed how to list, select, and create custom tuning profiles to optimize the system performance based on specific requirements. Effective management of tuning profiles can significantly enhance system efficiency and responsiveness, which is crucial in environments where performance and power consumption are critical. By mastering these techniques, system administrators can ensure that their systems are always running optimally according to the needs of their applications and users.

Remember to continually reassess your tuning settings as your system and workload characteristics evolve. Happy tuning!