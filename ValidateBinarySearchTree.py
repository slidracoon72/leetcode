from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Neetcode: https://www.youtube.com/watch?v=s6ATEkipzow
# Time: O(n)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Helper function to validate the tree recursively
        # `node` is the current node being validated
        # `left` and `right` define the allowable range for the node's value
        def valid(node, left, right):
            # Base case: An empty node (leaf node's child) is always valid
            if not node:
                return True
            # If the current node's value does not fall within the valid range, return False
            if not (left < node.val < right):
                return False

            # Recursively validate the left subtree
            # The value of the left child must be less than the current node's value
            # The range for the left child becomes (left, node.val)
            return valid(node.left, left, node.val) and \
                valid(node.right, node.val, right)  # Similarly validate the right subtree
            # The value of the right child must be greater than the current node's value
            # The range for the right child becomes (node.val, right)

        # Start the validation from the root with the initial range (-inf, inf)
        return valid(root, float("-inf"), float("inf"))

    # My solution: Inorder traversal of BST gives a sorted array
    def isValidBST1(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            res = []
            if node.left:
                res += dfs(node.left)
            res.append(node.val)
            if node.right:
                res += dfs(node.right)
            return res

        arr = dfs(root)

        if len(arr) != len(set(arr)):
            return False

        return arr == sorted(arr)
