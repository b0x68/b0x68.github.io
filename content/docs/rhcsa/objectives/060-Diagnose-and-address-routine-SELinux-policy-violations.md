# Tech Tutorial: Manage Security with SELinux

## Introduction

Security-Enhanced Linux (SELinux) is an essential part of managing security policies on Red Hat Enterprise Linux (RHEL) systems. SELinux adds an additional layer of security by enforcing access control policies that define how processes and users interact with system resources such as files, devices, and network ports. In this tutorial, we'll delve into diagnosing and addressing routine SELinux policy violations, a critical skill for anyone preparing for the Red Hat Certified System Administrator (RHCSA) exam.

## Step-by-Step Guide

### Understanding SELinux Modes and Contexts

Before diving into policy violations, it's important to understand the different modes in which SELinux can operate:

- **Enforcing:** SELinux enforces its policies and denies access based on these policies, logging actions.
- **Permissive:** SELinux does not enforce policies but logs what would have been denied if it were in Enforcing mode.
- **Disabled:** SELinux is completely turned off.

To check the current SELinux status, use the `sestatus` command:

```bash
$ sestatus
```

SELinux contexts are labels attached to every process and file, defining their security properties. To view the context of a file, use the `ls -Z` command:

```bash
$ ls -Z /path/to/file
```

### Diagnosing SELinux Policy Violations

When SELinux denies an operation, it logs a corresponding event, which can be examined using the `ausearch` and `audit2why` tools. These tools help in understanding why an action was denied.

1. **Finding SELinux Denial Messages**

   To find recent SELinux denials, you can use:

   ```bash
   $ ausearch -m avc -ts recent
   ```

   This command searches for type `avc` (Access Vector Cache) messages logged recently.

2. **Interpreting Denials with audit2why**

   To understand the reason behind a denial, pipe the output of `ausearch` to `audit2why`:

   ```bash
   $ ausearch -m avc -ts recent | audit2why
   ```

   This will provide a human-readable explanation of the denial, suggesting possible actions to resolve it.

### Addressing SELinux Policy Violations

After diagnosing a violation, the next step is to resolve it. Common approaches include adjusting file contexts, modifying SELinux booleans, or creating custom policy modules.

1. **Restoring File Contexts**

   If a file's context has been incorrectly modified, restore it using `restorecon`:

   ```bash
   $ restorecon -v /path/to/file
   ```

   This command will reset the file's SELinux context to its default value as defined by the policy.

2. **Toggling SELinux Booleans**

   SELinux booleans control various aspects of policy enforcement. To list booleans and their current values:

   ```bash
   $ getsebool -a
   ```

   To change a boolean value:

   ```bash
   $ setsebool -P httpd_can_network_connect on
   ```

   The `-P` flag makes the change persistent across reboots.

3. **Creating Custom Policy Modules**

   If standard adjustments are insufficient, you may need to create a custom SELinux policy module. Start by generating a module from denial messages:

   ```bash
   $ ausearch -c 'httpd' --raw | audit2allow -M myHttpd
   ```

   Here, `httpd` is the context or process being denied access, and `myHttpd` is the name of the new module. Install the module:

   ```bash
   $ semodule -i myHttpd.pp
   ```

## Conclusion

Managing SELinux policy violations effectively is crucial for maintaining the security integrity of RHEL systems. By diagnosing and addressing these violations, system administrators ensure that SELinux enhances system security without hindering legitimate system functionality. Remember, while SELinux can appear complex, mastering its fundamentals is rewarding and enhances your system administration skill set, especially as you prepare for the RHCSA exam.