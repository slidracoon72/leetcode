# Meta - Question
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Using DFS - Recursive
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            nonlocal res
            if node:
                if low <= node.val <= high:
                    res += node.val
                if low < node.val:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)

        res = 0
        dfs(root)
        return res

    # Using BFS - Iterative
    def rangeSumBST1(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        q = deque([root])
        while q:
            node = q.popleft()
            if low <= node.val <= high:
                res += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res
