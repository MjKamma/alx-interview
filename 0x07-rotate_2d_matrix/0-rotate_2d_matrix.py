#!/usr/bin/python3
"""
Matrix Rotation Module

This module provides a function to rotate a
given n x n 2D matrix 90 degrees clockwise in-place.
The matrix is rotated by first transposing it and then reversing each row.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.

    This function takes a 2D matrix as input and rotates it 90 degrees
    clockwise in-place. It first transposes the matrix
    by swapping elements across the diagonal,
    and then reverses each row of the transposed matrix.

    Args:
        matrix (list): The 2D matrix to rotate.

    Returns:
        None. The matrix is rotated in-place.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
