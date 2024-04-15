```markdown
# Lockboxes

## Introduction
This Python script determines whether all the boxes in a set of locked boxes can be opened. Each box may contain keys to other boxes, and a key with the same number as a box opens that box. The script utilizes breadth-first search (BFS) to traverse through the boxes and determine if they can all be opened.

## Files
- **0-lockboxes.py**: Python script containing the `canUnlockAll` function, which determines if all boxes can be opened.
- **main_0.py**: Example usage of the `canUnlockAll` function with test cases.

## Usage
To run the script with the provided test cases, execute the `main_0.py` file:
```bash
./main_0.py
```

## Function Prototype
```python
def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists representing the locked boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
```

## Example
```python
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
```

## Requirements
- Allowed editors: vi, vim, emacs
- Interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Code should be documented
- Code should use the PEP 8 style (version 1.7.x)
- All files must be executable

## Author
This script was written by [Your Name].

## Acknowledgments
- This project is part of the ALX Software Engineering program.
- Inspiration for this project came from a coding interview question.
```