# Tech Tutorial: Manage Security - Diagnosing and Addressing Routine SELinux Policy Violations

## Introduction

Security-Enhanced Linux (SELinux) is a security architecture integrated into various Linux distributions. It enforces mandatory access control policies that confine user programs and system daemons to the minimum amount of privileges they require to perform their tasks. This tutorial will guide you through understanding, diagnosing, and addressing routine SELinux policy violations, which are common issues administrators face while managing systems with SELinux enabled.

## Step-by-Step Guide

### Step 1: Understanding SELinux Contexts and Modes

Before diving into policy violations, it's essential to understand SELinux contexts and the difference between SELinux modes.

- **SELinux Contexts:** Every file, process, and resource has an SELinux context, which includes user, role, type, and, optionally, a security level. You can view the context using the `-Z` option with commands like `ls`, `ps`, etc. For example:

```bash
ls -Z /var/www/html/index.html
```

- **SELinux Modes:** SELinux operates in three modes:
  - **Enforcing:** SELinux enforces its policies and denies access based on them.
  - **Permissive:** SELinux does not enforce policies but logs policy violations.
  - **Disabled:** SELinux is turned off.

You can check the current mode using:

```bash
getenforce
```

To change modes, use:

```bash
setenforce 0   # Set to Permissive
setenforce 1   # Set to Enforcing
```

### Step 2: Diagnosing SELinux Policy Violations

When a process attempts an unauthorized action, it's blocked by SELinux, and a corresponding event is logged. The primary tool for diagnosing these violations is `ausearch` and `sealert`.

- **Using ausearch:**
  `ausearch` queries the audit daemon logs for SELinux messages. To find recent SELinux denials, you might run:

```bash
ausearch -m avc -ts recent
```

- **Analyzing Logs with sealert:**
  `sealert` can analyze audit logs and provide human-readable reports on violations. First, ensure it's installed (`yum install setroubleshoot-server` on CentOS/RHEL), then run:

```bash
sealert -a /var/log/audit/audit.log
```

This command provides detailed descriptions and suggestions for resolving policy violations.

### Step 3: Addressing SELinux Policy Violations

Once you've identified a policy violation, you have several options:

1. **Relabel Files:**
   If an incorrect context on a file is causing access issues, use `chcon` to change the context. For example, to set the context of a web file correctly, you might use:

```bash
chcon -t httpd_sys_content_t /var/www/html/index.html
```

2. **Generate and Install Custom Policy Modules:**
   If a custom application requires exceptions, you can generate a local policy module to allow the necessary access:

```bash
ausearch -c 'httpd' --raw | audit2allow -M myhttpd
semodule -i myhttpd.pp
```

3. **Booleans:**
   SELinux has booleans that can toggle certain behaviors. Use `getsebool` to see boolean settings and `setsebool` to change them:

```bash
getsebool -a | grep httpd
setsebool httpd_can_network_connect on -P
```

### Step 4: Testing and Verifying

After making changes, ensure that:
- The system still behaves as expected.
- No new SELinux denials are being logged due to recent adjustments.

You can re-run `sealert` or use `ausearch` to ensure no new AVC denials related to your changes:

```bash
ausearch -m avc -ts recent
```

## Conclusion

Managing SELinux and understanding its policy violations is crucial for maintaining a secure Linux environment. By diagnosing and addressing routine SELinux policy violations efficiently, system administrators can ensure that their systems are both secure and functional. Remember, while disabling SELinux might eliminate these issues, it removes a robust layer of security and is generally not recommended. Instead, taking the time to understand and configure SELinux can pay off in maintaining your system's integrity and security.