from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Binary Tree Traversal using DFS
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Helper function for DFS
        def dfs(node, current_number):
            if not node:
                return 0

            # Update the current number as we traverse
            current_number = current_number * 10 + node.val

            # If it's a leaf node, return the current number
            if not node.left and not node.right:
                return current_number

            # Recursively sum for the left and right subtrees
            left_sum = dfs(node.left, current_number)
            right_sum = dfs(node.right, current_number)

            # Return the total sum from both subtrees
            return left_sum + right_sum

        # Start DFS from the root with an initial number of 0
        return dfs(root, 0)
