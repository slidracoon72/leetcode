import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Helper function to perform BFS and find the values at the deepest level
        def bfs(root):
            if not root:
                return []

            q = collections.deque()
            q.append(root)
            last_level = []

            while q:
                cur_level = []
                qLen = len(q)
                # Process all nodes at the current level
                for _ in range(qLen):
                    node = q.popleft()
                    cur_level.append(node.val)
                    # Add child nodes for the next level
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                # Update last_level to be the current level's nodes
                if cur_level:
                    last_level = cur_level

            return last_level

        # Step 1: Get the values of the deepest level nodes
        last_level = bfs(root)
        if not last_level:  # If the tree is empty
            return None

        # Take the first and last nodes from the deepest level
        a, b = last_level[0], last_level[-1]

        # Helper function to find the Lowest Common Ancestor (LCA) of two nodes with values a and b
        # Similar to LCA_OfABinaryTree.py
        def lca(root, a, b):
            if not root:
                return None

            # If current node matches either of the values, return it
            if root.val == a or root.val == b:
                return root

            # Recur for left and right subtrees
            l = lca(root.left, a, b)
            r = lca(root.right, a, b)

            # If both left and right return non-null, this node is the LCA
            if l and r:
                return root
            else:
                # If only one side returns non-null, propagate it up
                return l or r

        # Step 2: Return the LCA of the first and last deepest nodes
        return lca(root, a, b)
