from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Solved using DFS
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # If the tree is empty, return 0
        if not root:
            return 0

        # DFS function with depth tracking
        def dfs(node, depth):
            # If node is None, return a large number so it doesn't affect min calculation
            if not node:
                return float('inf')

            # If it's a leaf node, return current depth
            if not node.left and not node.right:
                return depth

            # Recurse on left and right children, increasing depth
            return min(dfs(node.left, depth + 1), dfs(node.right, depth + 1))

        # Start from root at depth 1
        return dfs(root, 1)

    # Solved using BFS - More optimal for this problem
    def minDepth1(self, root: Optional[TreeNode]) -> int:
        # If the tree is empty
        if not root:
            return 0

        # Queue for BFS: stores (node, current_depth)
        q = deque([(root, 1)])

        while q:
            node, depth = q.popleft()

            # If it's a leaf node, return its depth
            if not node.left and not node.right:
                return depth

            # Add children to queue with incremented depth
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
