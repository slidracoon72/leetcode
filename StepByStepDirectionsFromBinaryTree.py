from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# DFS - Recursive
# Time and Space: O(n); n = no. of nodes in the tree
# Neetcode: https://www.youtube.com/watch?v=JegJNGcwtFg

# We start from root node and find the startValue first. Then we find the destValue.
# We generate paths for both the values.
# We then reverse the startPath ("L" -> "U") and append the destPath
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # Helper function to perform DFS and find the path to the target value
        def dfs(node: TreeNode, path: List[str], target: int) -> List[str]:
            if not node:
                return []
            if node.val == target:
                return path.copy()  # Return a copy of the current path when the target is found

            # Search in the left subtree
            path.append("L")
            res = dfs(node.left, path, target)
            if res:
                return res  # If found in the left subtree, return the path

            # Backtrack and search in the right subtree
            path.pop()
            path.append("R")
            res = dfs(node.right, path, target)
            if res:
                return res  # If found in the right subtree, return the path

            # If target is not found in either subtree, backtrack
            path.pop()
            return []

        # Find paths from root to startValue and destValue
        start_path = dfs(root, [], startValue)
        dest_path = dfs(root, [], destValue)

        # Determine the common prefix in both paths
        i = 0
        while i < min(len(start_path), len(dest_path)) and start_path[i] == dest_path[i]:
            i += 1

        # Create the final path: 'U' for each step to backtrack to the common ancestor
        # followed by the remaining steps in the dest_path
        res = ["U"] * len(start_path[i:]) + dest_path[i:]

        # Convert list of steps to a string
        return "".join(res)
