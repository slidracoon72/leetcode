# LC-105: Construct Binary Tree from Preorder and Inorder Traversal

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
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
