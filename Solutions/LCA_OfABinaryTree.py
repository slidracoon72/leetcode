# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(N)
# Space: O(1) if not counting recursive stack frames, else O(N)
# Solution: https://www.youtube.com/watch?v=WO1tfq2sbsI
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Check if the root is None (base case for recursion)
        if not root:
            return None

        # Check if the root is one of the target nodes (p or q)
        if (root == p) or (root == q):
            return root

        # Recursively search for the LCA in the left subtree
        l = self.lowestCommonAncestor(root.left, p, q)
        # Recursively search for the LCA in the right subtree
        r = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right subtrees return non-None values, it means
        # both nodes p and q are found in different subtrees of the current root
        if l and r:
            return root
        # If either left or right subtree returns a non-None value, it means
        # one of the target nodes (p or q) is found in the subtree, and the
        # other one is not found in the subtree. In this case, return the
        # non-None value from either left or right subtree.
        else:
            return l or r
