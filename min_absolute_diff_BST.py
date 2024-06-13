from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder_traversal(node):
            if not node:
                return 0

            res = []
            if node.left:
                res += inorder_traversal(node.left)

            res.append(node.val)

            if node.right:
                res += inorder_traversal(node.right)

            return res

        sorted_array = inorder_traversal(root)

        m = float('inf')
        for i in range(len(sorted_array) - 1):
            m = min(m, sorted_array[i + 1] - sorted_array[i])

        return m
