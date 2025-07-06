# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Step 1: Create a mapping from original nodes to their copies
        # Initialize with None so we can safely assign next/random as None
        oldToCopy = {None: None}

        # Step 2: First pass - create copy of each node and store in hashmap
        cur = head
        while cur:
            copy = Node(cur.val)  # Create a new node with same value
            oldToCopy[cur] = copy  # Map original node to its copy
            cur = cur.next

        # Step 3: Second pass - assign next and random pointers using the map
        cur = head
        while cur:
            copy = oldToCopy[cur]  # Get copied node
            copy.next = oldToCopy[cur.next]  # Assign next using map
            copy.random = oldToCopy[cur.random]  # Assign random using map
            cur = cur.next

        # Step 4: Return the head of the copied list
        return oldToCopy[head]
