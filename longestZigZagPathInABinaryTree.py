from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# DFS - Binary Tree
# Time Complexity: O(N), Space Complexity: O(N)
# Youtube: https://www.youtube.com/watch?v=hbzdyIlvBKI
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(root, isLeft, depth):
            if not root:
                # If the node is null, return the current depth
                # This acts as the base case for the recursion
                return depth

            # If the current direction is left
            if isLeft:
                # Update depth with the maximum depth found by:
                depth = max(
                    depth,
                    # Going right (zigzag) and incrementing the depth
                    dfs(root.right, False, depth + 1),
                    # Checking the possibility of a longer path from the left child without zigzagging
                    # Hence, resetting the depth to 0
                    dfs(root.left, True, 0),
                )
            # If the current direction is right
            else:
                # Update depth with the maximum depth found by:
                depth = max(
                    depth,
                    # Going left (zigzag) and incrementing the depth
                    dfs(root.left, True, depth + 1),
                    # Checking the possibility of a longer path from the right child without zigzagging
                    # Hence, resetting the depth to 0
                    dfs(root.right, False, 0),
                )
            # Return the maximum depth found
            return depth

        # Start the DFS from the root's left and right children
        # Initialize the search with the direction to the left and right with depth 0
        return max(dfs(root.left, True, 0), dfs(root.right, False, 0))
