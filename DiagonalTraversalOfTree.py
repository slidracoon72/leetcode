from typing import List
from collections import deque


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diagonalTraverse(self, root: TreeNode) -> List[int]:
        # Step 1: Handle edge case
        if not root:
            return []

        # Step 2: Initialize queue and result
        q = deque([root])  # Queue to process diagonals
        result = []

        # Step 3: Process each diagonal
        while q:
            node = q.popleft()  # Start of a new diagonal

            # Traverse the current diagonal (follow right children)
            while node:
                result.append(node.val)  # Add node to result
                # Add left child to queue (starts a new diagonal)
                if node.left:
                    q.append(node.left)
                # Move to right child (same diagonal)
                node = node.right

        return result

# Time Complexity: O(n), where n is the number of nodes in the tree
# - Each node is processed exactly once
# Space Complexity: O(w), where w is the maximum width of the tree
# - Queue stores at most the width of the tree (max number of diagonals at any level)