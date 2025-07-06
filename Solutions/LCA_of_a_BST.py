# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# LCA = Lowest Common Ancestor
# Neetcode: https://www.youtube.com/watch?v=gs2LMfuOR9k
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Check if the root is None (base case for recursion)
        if not root:
            return None
        # Initialize current node to root
        cur = root
        # Traverse the BST until the LCA is found
        while root:
            # If both p and q are greater than the current node's value, move to the right subtree
            if (p.val > cur.val) and (q.val > cur.val):
                cur = cur.right
            # If both p and q are smaller than the current node's value, move to the left subtree
            elif (p.val < cur.val) and (q.val < cur.val):
                cur = cur.left
            # If one value is smaller and the other is greater than the current node's value,
            # then the current node is the LCA
            else:
                return cur
