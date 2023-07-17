#!/usr/bin/python3
"""module to calculate the minimum operations needed
to copy all and paste a given number"""


def minOperations(n):
    """function to determine the number of minimum operations"""

    # If n is less than 1, it is impossible to achieve
    if n < 1:
        return 0

    # Initialize the number of operations to 0
    operations = 0

    # Start with one H in the file
    h_count = 1

    # Initialize the clipboard with the current content of the file
    clipboard = 1

    """
    While the number of H characters
    in the file is less than the desired count
    """
    while h_count < n:
        # If the desired count is divisible by the current count
        if n % h_count == 0:
            # Copy All and Paste the clipboard
            operations += 2
            clipboard = h_count
            h_count += clipboard
        else:
            # If not divisible, simply Paste the clipboard
            operations += 1
            h_count += clipboard

    return operations
