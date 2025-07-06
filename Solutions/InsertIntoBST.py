from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Value of the node
        self.left = left  # Left child node
        self.right = right  # Right child node


# Neetcode: https://www.youtube.com/watch?v=Cpg8f79luEA
# Average case: Time: O(logn), Space: O(logn)
# Worst case: Time: O(n), Space: O(n)
class Solution:
    # Recursive DFS solution to insert a value into a Binary Search Tree (BST)
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If the current node is None, we have found the correct position for the new value
        if not root:
            # Create a new TreeNode with the given value and return it
            return TreeNode(val)

        # If the value to insert is greater than the current node's value
        if val > root.val:
            # Recursively insert the value into the right subtree
            root.right = self.insertIntoBST(root.right, val)
        else:
            # Otherwise, insert the value into the left subtree
            root.left = self.insertIntoBST(root.left, val)

        # Return the root node (unchanged except for new insertions)
        return root

    # Iterative DFS solution to insert a value into a Binary Search Tree (BST)
    # Time: O(logn) , Space: O(1)
    def insertIntoBST1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If the root is None, create a new TreeNode with the given value and return it
        if not root:
            return TreeNode(val)

        # Initialize current node as the root of the tree
        cur = root

        # Iterate until we find the correct position to insert the new value
        while cur:
            # If the value to insert is greater than the current node's value
            if val > cur.val:
                # If there is no right child, create a new TreeNode with the value and assign it as the right child
                if not cur.right:
                    cur.right = TreeNode(val)
                    # Return the root of the modified tree
                    return root
                # Move to the right child
                cur = cur.right
            else:
                # If the value to insert is less than or equal to the current node's value
                # If there is no left child, create a new TreeNode with the value and assign it as the left child
                if not cur.left:
                    cur.left = TreeNode(val)
                    # Return the root of the modified tree
                    return root
                # Move to the left child
                cur = cur.left
