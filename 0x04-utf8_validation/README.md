# UTF-8 Validation

## Description
This Python script implements a method `validUTF8(data)` to determine whether a given dataset represents a valid UTF-8 encoding. The function accepts a list of integers, where each integer represents 1 byte of data, and returns `True` if the data is a valid UTF-8 encoding, otherwise it returns `False`.

## Requirements
- Python 3.4.3 or higher
- Ubuntu 20.04 LTS
- PEP 8 style compliance

## Usage
To use the `validUTF8` function, simply import it into your Python script and pass the dataset as a list of integers.

```python
from validate_utf8 import validUTF8

data = [65]
print(validUTF8(data))  # Output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False
```

## Files
- `validate_utf8.py`: Contains the implementation of the `validUTF8` function.
- `0-main.py`: Main file for testing the `validUTF8` function.
- `README.md`: This README file.

## Testing
To run the provided test cases, execute the `0-main.py` script:

```bash
./0-main.py
```
