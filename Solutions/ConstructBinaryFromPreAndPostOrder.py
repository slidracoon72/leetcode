# LC-889: Construct Binary Tree from Preorder and Postorder Traversal

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None

        root = TreeNode(preorder.pop(0))  # Root node is always the first element in preorder
        if not preorder:
            return root  # If there's only one node, return it

        left_subtree_root = preorder[0]  # The second element in preorder is the root of the left subtree
        left_subtree_size = postorder.index(left_subtree_root) + 1  # Find the size of the left subtree

        # Recursively build left and right subtrees
        root.left = self.constructFromPrePost(preorder[:left_subtree_size], postorder[:left_subtree_size])
        root.right = self.constructFromPrePost(preorder[left_subtree_size:], postorder[left_subtree_size:-1])

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
