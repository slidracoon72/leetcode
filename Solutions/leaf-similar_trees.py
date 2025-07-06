# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, leaf):
            # if root is empty
            if not root:
                return  # returns None
            # if leaf node
            if not root.left and not root.right:
                leaf.append(root.val)
                return
            # if not a leaf node
            dfs(root.left, leaf)
            dfs(root.right, leaf)

        leaf1, leaf2 = [], []
        dfs(root1, leaf1)
        dfs(root2, leaf2)
        return leaf1 == leaf2


# Test case:
# Tree 1:       1
#               \
#                2
#                 \
#                  3
# Tree 2:       1
#               \
#                3
#               /
#              2
root1_case2 = TreeNode(1)
root1_case2.right = TreeNode(2)
root1_case2.right.right = TreeNode(3)

root2_case2 = TreeNode(1)
root2_case2.right = TreeNode(3)
root2_case2.right.left = TreeNode(2)

# Testing
solution = Solution()
print(solution.leafSimilar(root1_case2, root2_case2))  # Output: false
