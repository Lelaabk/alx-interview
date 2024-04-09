#!/usr/bin/python3
"Pascal Triangle"

def pascal_triangle(n):
    """Return the nth row of Pascals triangle as a list."""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        l = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                l[j] = triangle[i  - 1][j - 1] + triangle[i - 1][j]
        triangle.append(l)

    return triangle