# Tech Tutorial: Understand and Use Essential Tools

## Introduction

In the world of Unix-like operating systems, understanding how to locate and make use of system documentation is critical for both new and experienced users. System documentation often serves as a first point of reference for learning about installed packages, commands, and utilities. This tutorial will guide you through using `man`, `info`, and exploring files in `/usr/share/doc`, which are essential tools for accessing system documentation.

## Step-by-Step Guide

### 1. Using the `man` Command

The `man` command, short for manual, is a ubiquitous tool used to display the user manual of any command that Linux has installed. The `man` pages are a comprehensive source containing information on usage, options, configuration, and more.

#### How to Use the `man` Command

- **Syntax**: The basic syntax of the `man` command is:
  ```bash
  man [option] [command]
  ```

- **Example**: To view the manual page for the `ls` command, you would use:
  ```bash
  man ls
  ```

This command will open an interface displaying detailed information about the `ls` command, its options, and how to use it.

#### Searching in `man` Pages

- You can search within a `man` page by pressing `/` followed by the search term. For example, `/directory` will search for the word "directory".
- Navigate through the search results using `n` (for next match) and `Shift+n` (for previous match).

### 2. Using the `info` Command

The `info` command displays detailed documentation about a program, which is sometimes more comprehensive than what is available via `man`. `info` pages are hyperlinked, much like web pages, allowing for easier navigation.

#### How to Use the `info` Command

- **Example**: To view the `info` page for the `bash` command, you would use:
  ```bash
  info bash
  ```

This opens the documentation for `bash` in a navigable interface.

#### Navigating `info` Pages

- **Moving Between Nodes**: Use the `n` (next node), `p` (previous node), and `u` (up one node) keys.
- **Following a Link**: Move the cursor over a highlighted link and press `Enter`.

### 3. Exploring `/usr/share/doc`

This directory contains static files such as READMEs, sample configurations, and detailed documentation specific to installed packages.

#### How to Use `/usr/share/doc`

- **Listing Contents**: To see what documents are available for `curl`, for instance:
  ```bash
  ls /usr/share/doc/curl
  ```

- **Reading Files**: Use a text viewer to read a file. For example:
  ```bash
  less /usr/share/doc/curl/README
  ```

This will display the README file for `curl`, which often includes usage examples, licensing information, and other helpful data not found in the `man` or `info` pages.

## Detailed Code Examples

Here are some common tasks you might perform using these tools:

#### Find Options for a Command

To find out what options are available for the `tar` command using `man`:
```bash
man tar
```
And then search for `-x` to find out how to extract files.

#### Learn More About a Protocol

To learn more about the HTTP protocol using `info`, you might navigate through:
```bash
info wget
```
Then follow the links to related information about HTTP within the document.

#### Check Configuration Examples

For real-world applications such as setting up a web server, consult `/usr/share/doc`:
```bash
ls /usr/share/doc/apache2/
cat /usr/share/doc/apache2/README.Debian
```

## Conclusion

Knowing how to effectively use `man`, `info`, and `/usr/share/doc` is invaluable for anyone working with Linux and Unix-like systems. These tools not only provide immediate access to a wealth of information but also empower users to solve problems and understand system functionalities independently. Remember, the more you practice, the more proficient you'll become in navigating and utilizing these essential resources.