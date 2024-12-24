import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Solved using BFS (level order traversal)
    # Time: O(n), Space: O(n)
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = collections.deque()
        q.append(root)

        level = 0
        while q:
            if level % 2:  # if level is odd
                l, r = 0, len(q) - 1
                while l < r:
                    # swap values
                    q[l].val, q[r].val = q[r].val, q[l].val
                    l += 1
                    r -= 1

            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return root
