from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Node's value
        self.left = left  # Reference to the left child node
        self.right = right  # Reference to the right child node


# Neetcode: https://www.youtube.com/watch?v=K81C31ytOZE
class Solution:
    # Time: O(n), Space:O(h)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize the result variable to keep track of the maximum diameter found
        # Make it a global class level variable
        self.res = 0

        # res = 0

        # Depth-First Search (DFS) function to compute the height of the tree
        def dfs(curr: Optional[TreeNode]) -> int:
            # Base case: If the current node is None, its height is 0
            if not curr:
                return 0

            # Recursively compute the height of the left subtree
            left = dfs(curr.left)
            # Recursively compute the height of the right subtree
            right = dfs(curr.right)

            # Update the result to the maximum diameter found so far
            # The diameter at the current node is the sum of the heights of the left and right subtrees
            self.res = max(self.res, left + right)

            # nonlocal res
            # res = max(res, left + right)

            # Return the height of the current node, which is 1 plus the maximum height of its subtrees
            return max(left, right) + 1

        # Start the DFS from the root to compute the diameter
        dfs(root)
        # Return the maximum diameter found
        return self.res
