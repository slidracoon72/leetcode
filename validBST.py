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
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False

            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))

    # My solution:
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
