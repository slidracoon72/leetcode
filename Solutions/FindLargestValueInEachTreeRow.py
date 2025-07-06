import collections
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Solved using BFS
    # Time: O(n), Space: O(n)
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = collections.deque()
        q.append(root)
        while q:
            largest = float('-inf')
            for _ in range(len(q)):
                node = q.popleft()
                largest = max(largest, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(largest)

        return res
