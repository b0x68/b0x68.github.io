+++
title = "Manage tuning profiles"
date = "2024-02-16T10:31:48-05:00"
author = "root"
cover = ""
tags = ["command:", "profile.", "kernel,", "linux", "group.", "system.", "system,", "kernel"]
keywords = ["command:", "--include=<kernel_parameter>`.", "profile", "system,", "profiles,", "system", "`--basedon=<profile_name>`", "package"]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


## Managing Tuning Profiles

Tuning profiles in Red Hat Certified Systems Administrator Exam 200 objective refer to the process of optimally configuring system settings to meet specific performance requirements. This tutorial will provide an in-depth explanation of how to effectively manage tuning profiles on a Red Hat Enterprise Linux system.

### Understanding Tuning Profiles
A tuning profile is a pre-configured set of system settings that can be applied to optimize the performance of a Red Hat Enterprise Linux system. Each tuning profile is designed to meet a specific performance goal, such as increasing throughput or reducing response time. These settings can be applied across various system components, including the kernel, network, storage, and application layers.

### Creating Tuning Profiles
To create a tuning profile, you must have root privileges or be a member of the `wheel` group. The `tuned` package must also be installed.

1. Install the `tuned` package if it is not already installed using the `yum install tuned` command.
2. Once the package is installed, you can create a new tuning profile using the `tuned-adm` command with the `create` option. For example, to create a profile named "webserver," use the following command: `tuned-adm create webserver`.
3. By default, the new profile will be based on the "default" profile. You can specify a different base profile by using the `--basedon=<profile_name>` option.

### Modifying Tuning Profiles
You can modify the settings of a tuning profile using the `tuned-adm` command.

1. To view the current settings of a profile, use the `tuned-adm` command with the `profile` option, followed by the profile name. For example, to view the settings of the "webserver" profile created in the previous step, use the following command: `tuned-adm profile webserver`.
2. To modify the settings, use the `tuned-adm` command with the `profile` and `modifiy` options. For example, to add a kernel parameter to the "webserver" profile, use the following command: `tuned-adm profile modify webserver --include=<kernel_parameter>`.

### Applying Tuning Profiles
Once you have created and modified your tuning profiles, you can apply them to your system. This can be done using the `tuned-adm` command.

1. To apply a specific profile, use the `tuned-adm` command with the `profile` option and the profile name. For example, to apply the "webserver" profile, use the following command: `tuned-adm profile webserver`.
2. To make a profile apply automatically at boot, use the `tuned-adm` command with the `profile` and `off` options. For example, to make the "webserver" profile auto-apply, use the following command: `tuned-adm profile off webserver`.

### Managing Active and Available Tuning Profiles
You can view a list of currently active and available tuning profiles using the `tuned-adm` command with the `list` option. This will also display the current active profile.

1. To view all available profiles, use the `--available` option. For example, `tuned-adm list --available`.
2. To view all active profiles, use the `--active` option. For example, `tuned-adm list --active`.

### Switching Between Tuning Profiles
You can switch between active tuning profiles using the `tuned-adm` command with the `switch` option. For example, to switch to the "webserver" profile, use the following command: `tuned-adm switch webserver`.

### Disabling Tuning Profiles
If you want to temporarily disable tuning profiles on your system, you can use the `tuned-adm` command with the `off` option. This will stop any currently active profiles from applying but will not remove them from the system.

To disable a specific profile, use the `off` option followed by the profile name (e.g. `tuned-adm off webserver`). To disable all profiles, use the `off` option followed by the `all` keyword (e.g. `tuned-adm off all`).

## Conclusion
In this tutorial, we have covered the process of managing tuning profiles on a Red Hat Enterprise Linux system. By creating, modifying, and applying these profiles, you can effectively optimize the performance of your system to meet specific goals. Remember to regularly review and modify your tuning profiles as your system's performance requirements may change over time.