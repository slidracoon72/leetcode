from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        def invert(node):
            if not node:
                return

            invert(node.left)
            invert(node.right)

            node.left, node.right = node.right, node.left

            return node

        invert(root)
        return root

    def invertTree1(self, root: TreeNode) -> TreeNode:
        if not root: return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
