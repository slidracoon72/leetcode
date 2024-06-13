# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            # Count current node as a good node if its value is greater than or equal to the maximum value in the path
            count = 1 if node.val >= max_val else 0
            # Update the maximum value in the path
            max_val = max(max_val, node.val)
            # Recursively count good nodes in the left and right subtrees
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)
            return count

        return dfs(root, float('-inf'))
