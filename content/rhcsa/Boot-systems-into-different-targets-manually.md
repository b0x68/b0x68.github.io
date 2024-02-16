+++
title = "Boot systems into different targets manually"
date = "2024-02-16T10:31:04-05:00"
author = "root"
cover = ""
tags = ["<target>`.", "system.", "multi-user", "target", "rd.lvm.lv=rhel/swap", "boot", "targets", ""linux""]
keywords = ["boot", "systemd.unit=rescue.target`", "rescue.target`.", "system.", "booted,", "rd.lvm.lv=rhel/swap", "booting", "<target>`."]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Boot systems into different targets manually

In this tutorial, we will explore how to manually boot a Red Hat Linux system into different targets. This is one of the objectives of the Red Hat Certified Systems Administrator Exam 200 and is an important skill for any Linux system administrator to master.

## Targets in Red Hat Linux

Targets in Red Hat Linux are similar to runlevels in other Linux distributions. They represent different states or levels of functionality for the operating system. There are several different targets in Red Hat Linux, each with a specific purpose. These include:

- Graphical user interface (GUI) target: This is the default target for most Red Hat Linux installations and provides a full graphical environment for users to interact with the system.
- Multi-user with networking target: This is a target that provides the same functionality as the GUI target, but without the graphical interface. It is commonly used for server installations.
- Rescue target: This target is used for troubleshooting and repairing a system that is not functioning properly.
- Emergency target: This is the most minimal target and is used for system recovery and maintenance tasks.

## Manually Booting Into Different Targets

To manually boot a Red Hat Linux system into different targets, follow these steps:

1. Boot the system and wait for the GRUB boot loader menu to appear.
2. Use the arrow keys to highlight the desired boot entry and press "e" to edit the boot options.
3. Navigate to the line that starts with "linux" and add the following text to the end of the line: `systemd.unit=<target>`
   
   Replace `<target>` with the target you want to boot into. For example, to boot into the rescue target, the line would look like this: `linux /vmlinuz-3.10.0-123.el7.x86_64 root=/dev/mapper/rhel-root ro crashkernel=auto rd.lvm.lv=rhel/swap vconsole.keymap=us rhgb quiet systemd.unit=rescue.target`
4. Press "Ctrl-X" or "F10" to boot the system.
5. The system will now boot into the target specified in the boot options.

## Setting a Default Target for Booting

If you want to set a default target for booting without manually editing the boot options every time, follow these steps:

1. Open the terminal and switch to the root user by running the command `su -`.
2. Use the `systemctl` command to view the current default target by running `systemctl get-default`.
3. To change the default target, run `systemctl set-default <target>`. For example, to set the rescue target as the default, run `systemctl set-default rescue.target`.
4. The next time the system is booted, it will automatically boot into the target specified as the default.

## Conclusion

Manually booting a Red Hat Linux system into different targets is a useful skill for any system administrator to have. By understanding the different targets available and how to set a default target, you can easily manage and troubleshoot your Linux systems. Practice this skill regularly to prepare for the Red Hat Certified Systems Administrator Exam 200 and to become a proficient Linux administrator.