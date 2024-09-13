# Tech Tutorial: Create Simple Shell Scripts with Input Processing in Red Hat Enterprise Linux

## Introduction

In this tutorial, we will explore how to create simple shell scripts in Red Hat Enterprise Linux (RHEL) that effectively process script inputs. Shell scripting is an essential skill for any systems administrator, particularly those preparing for the Red Hat Certified Systems Administrator (RHCSA) exam. We will focus specifically on handling positional parameters ($1, $2, etc.), which are crucial for making scripts dynamic and flexible.

## Step-by-Step Guide

### Step 1: Understanding Positional Parameters

Positional parameters are variables in a shell script that hold the values of command-line arguments passed to the script. For example, in a script invoked with `./myscript.sh arg1 arg2`, `$1` would hold `arg1` and `$2` would hold `arg2`. `$0` always holds the script's name.

### Step 2: Setting Up Your Environment

Before writing any scripts, ensure your RHEL system is ready. Open your terminal and if necessary, use `sudo` to perform tasks that require administrator privileges.

### Step 3: Writing the Script

Let's create a simple script that demonstrates the use of positional parameters.

1. Open a text editor, such as `vim` or `nano`:
   ```bash
   vim greet.sh
   ```

2. Insert the following script:
   ```bash
   #!/bin/bash
   # Script to greet users

   echo "Hello, $1!"
   echo "Welcome to the RHCSA tutorial on $2."
   ```

3. Save and exit the editor (`:wq` in `vim`).

4. Make the script executable:
   ```bash
   chmod +x greet.sh
   ```

### Step 4: Running the Script

Run the script with two arguments:
```bash
./greet.sh John "Red Hat Enterprise Linux"
```

Output should be:
```
Hello, John!
Welcome to the RHCSA tutorial on Red Hat Enterprise Linux.
```

## Detailed Code Examples

### Example 1: A Script to Sum Numbers

This script sums numbers provided as command-line arguments.

1. Create the script:
   ```bash
   vim sum.sh
   ```

2. Add the following content:
   ```bash
   #!/bin/bash
   # Sum script

   total=0

   for num in "$@"
   do
       total=$(($total + $num))
   done

   echo "Total sum: $total"
   ```

3. Make it executable and run it:
   ```bash
   chmod +x sum.sh
   ./sum.sh 5 15 10
   ```

Output:
```
Total sum: 30
```

### Example 2: A Script Using Shift

`shift` is a command used to manipulate positional parameters. It shifts all positional parameters to the left.

1. Create the script:
   ```bash
   vim shift_example.sh
   ```

2. Write the script:
   ```bash
   #!/bin/bash
   # Shift example script

   while [ "$1" != "" ]; do
       echo "Processing parameter of: $1"
       shift
   done
   ```

3. Make it executable and run it:
   ```bash
   chmod +x shift_example.sh
   ./shift_example.sh param1 param2 param3
   ```

Output:
```
Processing parameter of: param1
Processing parameter of: param2
Processing parameter of: param3
```

## Conclusion

Understanding and using positional parameters in shell scripts is fundamental for automating tasks in RHEL. By mastering this concept, you can write more dynamic and flexible scripts, enhancing your capabilities as a system administrator. This tutorial covered the basics and some intermediate uses of positional parameters, but remember, practice is key to mastering shell scripting.

Happy scripting on your path to becoming a Red Hat Certified Systems Administrator!