+++
title = "Boot systems into different targets manually"
date = "2024-02-16T11:46:13-05:00"
author = "root"
cover = ""
tags = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
keywords = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Booting Systems into Different Targets Manually

Boot targets are specific modes or levels in which a system can be booted into. Each boot target is designed for a specific purpose, such as booting a system into a graphical user interface (GUI) or a command-line interface. The ability to manually boot a system into different targets is an important skill for a Red Hat Certified Systems Administrator and is included as an objective in the Red Hat Certified Systems Administrator Exam 200.

In this tutorial, we will go in-depth on how to manually boot systems into different targets, covering the following topics:

1. Understanding Boot Targets
2. Accessing Boot Manager
3. Selecting a Boot Target
4. Verifying Boot Target Change
5. Troubleshooting Boot Target Issues

Let's get started!

## Understanding Boot Targets

As mentioned earlier, boot targets are specific modes or levels in which a system can be booted into. The available boot targets may vary depending on the operating system and system configuration. For Red Hat Enterprise Linux, the common boot targets are:

- Graphical (GUI) - This target allows for booting into a desktop environment with a graphical user interface.
- Multi-user (Text mode) - This target boots the system into a command-line interface, also known as text mode.
- Rescue - This target is used for troubleshooting and repairing a system that is having issues with its primary boot targets.
- Network - This target is used to boot a system over the network, instead of using the local storage devices.

Now that we understand the different boot targets, let's see how we can manually boot into them.

## Accessing Boot Manager

The first step to manually booting a system into a different target is to access the boot manager. The steps to access the boot manager may vary depending on the system's hardware, but the most common method is to press a specific key (e.g. F12 or Esc) during the system's startup process.

Once in the boot manager, select the device from which you want to boot the system. This can be a local storage device, such as a hard drive or a USB drive, or a network device.

## Selecting a Boot Target

After selecting the boot device, the system will attempt to boot into the default boot target. To manually choose a different boot target, we need to interrupt the boot process by pressing a key (e.g. Tab or Esc). This will bring up the boot menu, which lists all available boot targets.

Use the arrow keys to navigate the boot menu and highlight the desired boot target. Then, press Enter to confirm the selection. The system will then boot into the chosen target.

## Verifying Boot Target Change

Once the system has successfully booted into the selected target, it is important to verify the change. This can be done by checking the output of the "runlevel" command, which displays the current run level of the system. Each boot target corresponds to a specific run level, as shown below:

- Graphical (GUI) - Run level 5
- Multi-user (Text mode) - Run level 3
- Rescue - Run level 1 or S (single user mode)
- Network - Run level 2

To verify the current boot target, type "runlevel" in the command line and press Enter. The output will display the current run level, which should correspond to the boot target we manually selected.

## Troubleshooting Boot Target Issues

In some cases, you may encounter issues while trying to boot a system into a specific target manually. This can be due to various reasons, such as incorrect boot loader settings or missing files. To troubleshoot these issues, you can use the rescue target to boot into a minimal system and perform troubleshooting steps.

One of the common issues with boot target changes is incorrect boot loader settings. If this is the case, you can use the rescue target to access the system's configuration files and make necessary changes to the boot loader.

If the issue persists, you can also refer to Red Hat documentation or seek help from the Red Hat community for further troubleshooting steps.

## Conclusion

Being able to manually boot systems into different targets is a crucial skill for a Red Hat Certified Systems Administrator. In this tutorial, we covered the basics of boot targets, accessing the boot manager, selecting a boot target, verifying the change, and troubleshooting boot target issues.

Remember to thoroughly understand the different boot targets for your operating system and constantly practice manually booting into them. This will not only prepare you for the Red Hat Certified Systems Administrator Exam 200 but also help in real-world scenarios where you may need to switch boot targets. 