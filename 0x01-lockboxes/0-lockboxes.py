#!/usr/bin/python3
"""Lockboxes module"""

from collections import deque


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes.
            Each inner list contains the keys
            found inside the corresponding box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.

    Example:
        boxes = [
            [1],       # Box 0 has key 1
            [2],       # Box 1 has key 2
            [3, 4],    # Box 2 has keys 3 and 4
            [5],       # Box 3 has key 5
            []         # Box 4 has no keys
        ]

        print(canUnlockAll(boxes))  # Output: True
    """

    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True  # Start with the first box unlocked
    queue = deque([0])  # Add the first box to the queue

    while queue:
        current_box = queue.popleft()
        keys = boxes[current_box]

        for key in keys:
            if key < num_boxes and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
