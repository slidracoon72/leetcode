from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Neetcode: https://www.youtube.com/watch?v=FqAoYAwbwV8
class Solution:
    # Using Postorder - DFS Recursion
    # Time and Space: O(n)
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None

        # Postorder: left, right, root
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        # Check for leaf node and if it's the target value
        if not root.left and not root.right and root.val == target:
            # Delete it by returning None
            return None
        return root

    # Using Postorder - DFS Iterative
    # Time and Space Complexity: O(n)
    def removeLeafNodes1(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        stack = [root]  # Initialize the stack with the root node for DFS
        visit = set()  # A set to keep track of visited nodes
        parents = {root: None}  # A dictionary to keep track of each node's parent

        while stack:
            node = stack.pop()  # Pop a node from the stack

            # Check if the node is a leaf node and its value equals the target
            if not node.left and not node.right:
                if node.val == target:
                    p = parents[node]  # Get the parent of the current node

                    if not p:  # If the node is the root (it has no parent)
                        return None  # If the root node itself is to be deleted, return None

                    # If the current node is the left child of its parent, remove it
                    if p.left == node:
                        p.left = None
                    # If the current node is the right child of its parent, remove it
                    if p.right == node:
                        p.right = None

            elif node not in visit:  # If the node has not been visited
                visit.add(node)  # Mark the node as visited

                # Since the stack follows LIFO order, we need to add nodes in reverse order
                # Add the current node back to the stack to process its children first
                stack.append(node)

                # Add the left child to the stack and record its parent
                if node.left:
                    stack.append(node.left)
                    parents[node.left] = node

                # Add the right child to the stack and record its parent
                if node.right:
                    stack.append(node.right)
                    parents[node.right] = node

        return root  # Return the modified tree root
