# LC-106: Construct Binary Tree from Inorder and Postorder Traversal
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time - O(n^2)
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        root = TreeNode(postorder.pop())
        idx = inorder.index(root.val)
        root.left = self.buildTree(inorder[:idx], postorder)
        root.right = self.buildTree(inorder[idx + 1:], postorder)
        return root

# Use below tree and orders to understand and dry run the code:
# Tree:
#              1
#             / \
#            2    3
#           / \  / \
#          4   5 6  7
#
# Orders:
# Preorder: [1,2,4,5,3,6,7]
# Inorder: [4,2,5,1,6,3,7]
# Postorder: [4,5,2,6,7,3,1]
