from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: O(n), Space: O(h)
# Neetcode: https://www.youtube.com/watch?v=rKnD7rLT0lI
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # Define a helper function for depth-first search (DFS)
        def dfs(root):
            # Base case: if the current node is None, return None
            if not root:
                return None

            # Recursively flatten the left and right subtrees
            leftTail = dfs(root.left)
            rightTail = dfs(root.right)

            # If there is a left subtree, we need to insert it between the current node and the right subtree
            if leftTail:
                # Connect the end of the left subtree to the start of the right subtree
                leftTail.right = root.right
                # Move the left subtree to the right
                root.right = root.left
                # Set the left child to None
                root.left = None

            # Return the tail of the flattened subtree
            # If there is a rightTail, it is the tail of the entire subtree
            # If there is no rightTail but there is a leftTail, it is the tail
            # If neither subtree exists, the current node is the tail
            linked_list = rightTail or leftTail or root
            return linked_list

        # Start the DFS from the root
        dfs(root)
