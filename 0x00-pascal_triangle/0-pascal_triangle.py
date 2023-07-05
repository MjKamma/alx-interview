#!/usr/bin/python3
"""Module to define pascal's triangle"""


def pascal_triangle(n):
    """return Pascal's Triangle with an array of integers"""

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[i - 1]
        curr_row = [1]
        for j in range(1, i):
            curr_row.append(prev_row[j - 1] + prev_row[j])
        curr_row.append(1)
        triangle.append(curr_row)

    return triangle
