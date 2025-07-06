from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Solved using DFS - Recursion
    # Time: O(n), Space: O(n)
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)  # (robbed, not robbed)

            left = dfs(node.left)
            right = dfs(node.right)

            # If we rob this node, we cannot rob its children
            rob_current = node.val + left[1] + right[1]

            # If we don't rob this node, we can take the max of robbing or not robbing children
            skip_current = max(left) + max(right)

            return (rob_current, skip_current)

        return max(dfs(root))
