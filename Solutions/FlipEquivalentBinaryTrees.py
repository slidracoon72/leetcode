from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Using Recursion
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Base case: if both are None, they are equivalent
        if not root1 and not root2:
            return True

        # If one is None and the other isn't, they are not equivalent
        if not root1 or not root2 or root1.val != root2.val:
            return False

        # Recursively check both configurations:
        # 1. Children are the same, no flip required
        # 2. Children are flipped (left child matches right, right matches left)
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or \
            (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
