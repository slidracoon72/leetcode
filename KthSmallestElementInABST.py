# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Solved using Inorder-Traversal as it gives sorted output
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorderTraversal(root):
            if root is None:
                return []
            result = []
            result += inorderTraversal(root.left)
            result.append(root.val)
            result += inorderTraversal(root.right)
            return result

        return inorderTraversal(root)[k - 1]
