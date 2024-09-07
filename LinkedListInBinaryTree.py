from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # Helper function to check if the linked list starting from list_node
        # is a subpath in the binary tree starting from tree_node.
        def helper(list_node, tree_node):
            # If we've reached the end of the linked list, that means
            # we've found a matching path in the tree, so return True.
            if not list_node:
                return True
            # If the tree node is None or the values of the current linked list node
            # and tree node don't match, return False as this path won't work.
            if not tree_node or list_node.val != tree_node.val:
                return False
            # Recursively check both the left and right children of the tree node
            # to see if the remaining linked list can continue as a subpath.
            return (
                    helper(list_node.next, tree_node.left) or
                    helper(list_node.next, tree_node.right)
            )

        # Start by checking if the path starting from the root contains the linked list.
        if helper(head, root):
            return True
        # If the root is None, no subpath can exist, so return False.
        if not root:
            return False
        # Recursively check the left and right subtrees to see if the linked list
        # is a subpath starting from any other node in the tree.
        return (
                self.isSubPath(head, root.left) or
                self.isSubPath(head, root.right)
        )
