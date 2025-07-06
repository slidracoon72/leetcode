# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Solving using Depth First Search (DFS) approach
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curSum):
            if not node:
                return False
            curSum += node.val
            # checking if it is leaf node
            if not node.left and not node.right:
                return curSum == targetSum
            # if not leaf node, recursive function to check other remaining nodes
            return dfs(node.left, curSum) or dfs(node.right, curSum)

        # calling(/initialising) the function with given 'root' parameter & current sum (curSum) as 0
        return dfs(root, 0)
