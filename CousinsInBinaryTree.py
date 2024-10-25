from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time complexity: O(n), where n is the number of nodes in the tree.
    # Space complexity: O(n), for storing nodes in the queue.
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        res = []  # To store depth and parent info of nodes x and y
        q = deque([(root, 0, 0)])  # Queue for BFS, holding (node, depth, parent)

        while q:
            node, d, p = q.popleft()  # Dequeue the front node with its depth and parent info
            if node:
                # If current node is either x or y, append its depth and parent to res
                if node.val == x or node.val == y:
                    res.append((d, p))
                if len(res) == 2:
                    break
                d += 1  # Move to the next depth level
                # Enqueue the left and right children with updated depth and parent info
                q.append((node.left, d, node.val))
                q.append((node.right, d, node.val))

        # Return True if x and y are at the same depth but have different parents (i.e., they are cousins)
        return (res[0][0] == res[1][0]) and (res[0][1] != res[1][1])
