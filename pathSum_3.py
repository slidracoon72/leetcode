# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0

        def dfs(node, target):
            if not node:
                return 0
            # Check the current node and its children for paths
            if node.val == target:
                count = 1
            else:
                count = 0
            count += dfs(node.left, target - node.val)
            count += dfs(node.right, target - node.val)
            return count

        # Traverse the tree
        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
