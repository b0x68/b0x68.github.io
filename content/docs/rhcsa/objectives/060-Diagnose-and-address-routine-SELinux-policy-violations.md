# Tech Tutorial: Manage Security - Diagnosing and Addressing Routine SELinux Policy Violations

## Introduction

Security-Enhanced Linux (SELinux) is a security architecture integrated into the kernel that enforces mandatory access control policies, which define how processes and users can access resources such as files, ports, and other objects in a Linux system. Understanding and managing SELinux policy violations is crucial for maintaining the security integrity of your systems. In this tutorial, we will delve into diagnosing and addressing routine SELinux policy violations, providing you with the skills needed to ensure your Linux systems remain secure and compliant.

## Step-by-Step Guide

### Step 1: Understanding SELinux Modes

SELinux operates in one of three modes:
- **Enforcing:** SELinux policies are enforced, and violations are logged.
- **Permissive:** SELinux policies are not enforced but violations are still logged. This is useful for troubleshooting.
- **Disabled:** SELinux is completely turned off.

To check the current SELinux mode, use the following command:
```bash
getenforce
```

To temporarily switch to Permissive mode for troubleshooting, use:
```bash
sudo setenforce 0
```
Remember to switch it back to Enforcing mode (`sudo setenforce 1`) once you are done troubleshooting.

### Step 2: Diagnosing Policy Violations

The primary tool for diagnosing SELinux policy violations is the `auditd` daemon which logs all security-related events, including SELinux denials. The logs can be found in `/var/log/audit/audit.log`.

To search for SELinux related messages, you can use:
```bash
sudo ausearch -m avc -ts recent
```
This command searches for AVC (Access Vector Cache) denials that have occurred recently.

### Step 3: Interpreting AVC Messages

An AVC message typically looks like this:
```
type=AVC msg=audit(1703984203.546:123): avc:  denied  { read } for  pid=1234 comm="httpd" name="index.html" dev="sda1" ino=56789 scontext=system_u:system_r:httpd_t:s0 tcontext=system_u:object_r:default_t:s0 tclass=file
```
This message indicates that the `httpd` process was denied read access to `index.html`. The source context (`scontext`) is `httpd_t` and the target context (`tcontext`) is `default_t`.

### Step 4: Addressing Violations with `audit2allow`

`audit2allow` is a tool that generates SELinux policy allow rules from logged denials that you can use to create a custom policy module.

First, create a human-readable report from the audit log:
```bash
sudo ausearch -m avc -ts recent | audit2allow -m mymodule
```
This command filters recent AVC denials and pipes them to `audit2allow`, which generates a policy module named `mymodule`.

If the policy change seems reasonable, create a policy package:
```bash
sudo ausearch -m avc -ts recent | audit2allow -M mymodule
```
This command generates a `.pp` file (`mymodule.pp`).

### Step 5: Apply the Policy Module

To apply the generated policy module, use:
```bash
sudo semodule -i mymodule.pp
```
This command installs the policy module, which should resolve the violation.

## Detailed Code Examples

### Example: Allowing HTTPD Access to a Custom Directory

Suppose your web server (`httpd`) needs access to a custom directory `/custom`, and SELinux is blocking access. Here's how you can address it:

1. **Check for AVC denials:**
   ```bash
   sudo ausearch -m avc -ts recent | grep httpd
   ```
2. **Generate and apply a policy module:**
   ```bash
   sudo ausearch -m avc -ts recent | grep httpd | audit2allow -M httpd_custom
   sudo semodule -i httpd_custom.pp
   ```

This will allow `httpd` the necessary access while maintaining the security posture of the rest of the system.

## Conclusion

Understanding and managing SELinux policy violations are critical for maintaining the security of Linux systems. By diagnosing and addressing routine SELinux policy violations, you ensure that applications function as intended without compromising on security. Remember, while `audit2allow` provides a quick way to generate policy modules, each change should be carefully reviewed to avoid inadvertently weakening your system's security.