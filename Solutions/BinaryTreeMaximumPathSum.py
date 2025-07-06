# LC - Hard
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize result with the root's value (can be negative)
        res = [root.val]

        # Helper function to perform DFS and compute maximum path sum
        def dfs(root):
            if not root:
                return 0  # Base case: null nodes contribute 0 to the path sum

            # Recursively find the max path sum of left and right subtrees
            maxLeft = dfs(root.left)
            maxRight = dfs(root.right)

            # If a subtree contributes a negative value, ignore it by using 0
            maxLeft = max(maxLeft, 0)
            maxRight = max(maxRight, 0)

            # Update the result with the max value by considering the path through current node (split path)
            res[0] = max(res[0], maxLeft + root.val + maxRight)

            # Return the maximum gain from one side (non-split path)
            return root.val + max(maxLeft, maxRight)

        dfs(root)
        return res[0]  # Final result contains the maximum path sum found
