---
date: 2025-02-13
tags: Puppet
linktitle: Puppet Include vs Inherits
title: Puppet Include vs Inherits
---
![dumb looking monkey](/linux-imposter-syndrome-monkey.png)
# Differences Between `include` and `inherits` in Puppet

In Puppet, including a class (`include`) and inheriting a class (`inherits`) serve very different purposes.

## Using `include` to Apply a Class

### Purpose and Usage
- To apply a class to a node
- To ensure the class is declared only once, even if `include` is called multiple times
- To apply parameterized classes when used with `class {}` syntax

### Key Characteristics
- Executes the class immediately when it is included
- Works with parameterized classes when declared using `class {}` syntax
- Does not create a parent-child relationship

### Example: Using `include` to Apply a Class

```puppet
class webserver {
  package { 'httpd': ensure => installed }
  service { 'httpd':
    ensure => running,
    enable => true,
    require => Package['httpd'],
  }
}

include webserver  # Applies the class
```

### Example: Using `class {}` to Pass Parameters

```puppet
class webserver (
  String $package_name = 'httpd',
) {
  package { $package_name: ensure => installed }
}

class { 'webserver': package_name => 'nginx' }  # Applies the class with parameters
```

## Using `inherits` to Create a Subclass

### Purpose and Usage
- To create a child class that inherits properties from a parent class
- To extend an existing class by adding more resources or overriding variables
- Useful for defining default behaviors in a base class and extending them in child classes

### Key Characteristics
- Does not automatically apply the parent class
- Inherited class gets all resources from the parent but does not inherit parameters
- Cannot override parameters dynamically

### Example: Using `inherits` to Extend a Class

```puppet
class base_webserver {
  package { 'httpd': ensure => installed }
  service { 'httpd': ensure => running, enable => true }
}

class custom_webserver inherits base_webserver {
  file { '/etc/httpd/conf.d/custom.conf':
    ensure => file,
    content => "Custom configuration",
  }
}

include custom_webserver  # This applies the child class
```

## Comparison of `include` vs `inherits`

| Feature | `include` | `inherits` |
|---------|-----------|------------|
| Purpose | Apply a class | Extend a class |
| Execution | Runs the class immediately | Does not execute the parent unless applied separately |
| Reusability | Can be included multiple times | Can only inherit from one class |
| Parameter Support | Supports parameterized classes | Does not inherit parameters, they must be redeclared |
| Dynamic Behavior | Can be included conditionally | Static inheritance, no dynamic behavior |
| Use Case | Applying existing classes to nodes | Extending and modifying class behavior |

## Best Practices

- Favor `include` over `inherits` in most cases
- `inherits` is rarely used in modern Puppet because it has limitations with parameterized classes
- Using Hiera with `lookup()` is usually a better approach for defining default behaviors instead of using inheritance
