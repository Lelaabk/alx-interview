# Minimum Operations

This Python script calculates the minimum number of operations needed to achieve a given number of characters in a text file using only "Copy All" and "Paste" operations.

## Description

In a text file, there is initially a single character 'H'. The script can execute only two operations: "Copy All" and "Paste". Given a number `n`, the script calculates the fewest number of operations needed to result in exactly `n` 'H' characters in the file.

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- The code should be documented
- The code should use the PEP 8 style (version 1.7.x)
- All files must be executable

## Function Prototype

```python
def minOperations(n):
    """
    Calculates the minimum number of operations needed to achieve n characters.

    Args:
        n (int): The target number of characters.

    Returns:
        int: The minimum number of operations.
    """
```

## Usage

```bash
./0-minoperations.py
```

## Example

```python
n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```

## Author

[Layla]