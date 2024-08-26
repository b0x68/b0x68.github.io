# Tech Tutorial: Create Simple Shell Scripts

## Introduction

Shell scripting is a powerful tool for automating tasks on UNIX and Linux systems. In this tutorial, we will focus on how to process script inputs using positional parameters (`$1`, `$2`, etc.). Understanding how to handle script inputs is crucial for creating flexible and reusable scripts.

## Step-by-Step Guide

### 1. Understanding Positional Parameters

In shell scripting, positional parameters are variables that hold the arguments passed to the script from the command line. They are named as `$1`, `$2`, `$3`, etc., where `$1` represents the first argument, `$2` the second argument, and so on.

For example, if a script is run with the command `./myscript.sh apple banana`, then `apple` and `banana` are positional parameters where `apple` is `$1` and `banana` is `$2`.

### 2. Accessing Positional Parameters

To use these parameters in your script, you simply refer to them using their respective dollar-sign notation. Here’s a basic script that echoes the first two positional parameters:

```bash
#!/bin/bash

echo "First argument: $1"
echo "Second argument: $2"
```

### 3. Handling Multiple Inputs

You can process more than just one or two inputs by looping through all the positional parameters using a loop. Here’s an example:

```bash
#!/bin/bash

for arg in "$@"
do
    echo "Argument: $arg"
done
```

This script will echo each argument passed to the script.

### 4. Shifting Parameters

Sometimes, you may want to "shift" parameters so that `$2` becomes `$1`, `$3` becomes `$2`, and so on. This can be achieved using the `shift` command. Here's an example:

```bash
#!/bin/bash

while [ "$1" != "" ]; do
    echo "Processing $1"
    shift
done
```

This script will process each argument until there are no more arguments left.

### 5. Using Parameters with Options

Often, you'll need to handle options (like `-h` for help or `-v` for verbose) along with other arguments. Here's a more complex script that handles options and general arguments:

```bash
#!/bin/bash

while getopts ":hv" option; do
    case $option in
        h)
            echo "Usage: $0 [-h] [-v] [file...]"
            exit;;
        v)
            verbose=1
            shift
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            exit 1
            ;;
    esac
done

if [ "$verbose" = "1" ]; then
    echo "Verbose mode is on."
else
    echo "Verbose mode is off."
fi

echo "Processing files: ${@}"
for file in "$@"; do
    echo "File: $file"
done
```

## Detailed Code Examples

Let’s create a script named `file_processor.sh` that demonstrates handling multiple file names and options for displaying file contents.

```bash
#!/bin/bash

display_content=false

# Parse options
while getopts ":f:v" opt; do
  case $opt in
    f)
      display_content=true
      ;;
    v)
      echo "Version 1.0"
      exit
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

# Remove the options from the positional parameters
shift $((OPTIND-1))

# Iterate over remaining arguments
for filename in "$@"; do
    echo "Processing file: $filename"
    if $display_content; then
        echo "Contents of $filename:"
        cat "$filename"
    fi
done
```

## Conclusion

In this tutorial, you have learned how to handle script inputs using positional parameters in shell scripts. We covered how to access, shift, and loop through parameters, and how to manage options with `getopts`. These techniques will help you write more flexible and powerful shell scripts, enhancing your automation capabilities on UNIX and Linux systems. Remember, practice is key to mastering shell scripting, so keep experimenting with different scripts and scenarios.