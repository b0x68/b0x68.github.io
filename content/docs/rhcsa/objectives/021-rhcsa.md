# Tech Tutorial: Operate Running Systems

## Introduction

In the realm of system administration, the performance of your systems is paramount. One critical aspect of managing systems, particularly on Linux-based systems, is the ability to manage tuning profiles. Tuning profiles allow administrators to optimize system performance based on the specific needs of their applications or workloads. This tutorial will delve into managing tuning profiles using the `tuned` daemon, a dynamic adaptive system tuning daemon that tunes system settings dynamically depending on usage. We will cover installation, configuration, and management of tuning profiles.

## Prerequisites

- A Linux system (CentOS/RHEL 7 or 8 are commonly used with `tuned`)
- Basic understanding of Linux command line
- Root or sudo privileges

## Step-by-Step Guide

### Step 1: Installing Tuned

First, you need to ensure that `tuned` is installed on your system. You can install `tuned` using the package manager of your Linux distribution. On RHEL/CentOS, you would use:

```bash
sudo yum install tuned
```

For Debian/Ubuntu-based systems, you might first need to enable the universe repository:

```bash
sudo add-apt-repository universe
sudo apt-get update
sudo apt-get install tuned
```

### Step 2: Starting and Enabling Tuned

Once installed, you need to start and enable `tuned` to ensure it runs at boot:

```bash
sudo systemctl start tuned
sudo systemctl enable tuned
```

### Step 3: Listing Available Profiles

`Tuned` comes with several pre-defined tuning profiles. You can list all available profiles using:

```bash
tuned-adm list
```

This command will show you profiles such as `balanced`, `powersave`, `throughput-performance`, etc.

### Step 4: Choosing a Tuning Profile

To select a tuning profile that fits your system’s role, use the `tuned-adm` command. For instance, if your server is used for database operations, you might benefit from the `throughput-performance` profile:

```bash
sudo tuned-adm profile throughput-performance
```

### Step 5: Customizing Tuning Profiles

You might find that the default profiles don't perfectly match your needs. In such cases, you can create a custom tuning profile. Here’s how you can create a simple custom profile:

1. Create a new profile directory:

    ```bash
    sudo mkdir /etc/tuned/my-custom-profile
    ```

2. Create a `tuned.conf` file in this directory:

    ```bash
    sudo nano /etc/tuned/my-custom-profile/tuned.conf
    ```

    Add the following content:

    ```
    [main]
    include=balanced

    [sysctl]
    net.ipv4.tcp_tw_reuse = 1
    ```

    This profile extends the `balanced` profile with a custom sysctl setting.

3. Activate the new profile:

    ```bash
    sudo tuned-adm profile my-custom-profile
    ```

### Step 6: Monitoring Tuned

To ensure `tuned` is applying the settings, use:

```bash
sudo tuned-adm active
```

This command shows the current active profile and confirms that it is indeed applied.

## Conclusion

Tuning profiles are a powerful tool for system administrators looking to optimize their server performance. By leveraging the `tuned` daemon, you can dynamically adapt your system's settings based on the workload, thereby improving efficiency and performance. Remember, while `tuned` provides several automated profiles, the creation of custom profiles can further refine system behavior to suit your specific needs. Always monitor the system's performance after changes and adjust as necessary.