from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# Neetcode: https://www.youtube.com/watch?v=GMUI91_pDmM
# Time: O(n), Space: O(h) where n = no. of nodes, h = height of tree
class Solution:
    # Recursive Solution
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def helper(node):
            if not node:
                return
            for child in node.children:
                helper(child)
            res.append(node.val)

        helper(root)
        return res

    # Iterative Solution
    def postorder1(self, root: 'Node') -> List[int]:
        res = []  # This list will store the result of the postorder traversal

        if not root:  # If the root is None, return an empty list (base case)
            return []

        # Initialize the stack with a tuple of the root node and a visited flag set to False
        # The visited flag helps us know when to add the node's value to the result
        stack = [(root, False)]

        # Process nodes in the stack iteratively
        while stack:
            node, visited = stack.pop()  # Pop the top node and its visited status

            if visited:
                # If the node has been visited, add its value to the result list
                res.append(node.val)
            else:
                # If the node hasn't been visited yet, mark it as visited
                stack.append((node, True))

                # Add all children of the node to the stack in reverse order
                # Reversing ensures we process the leftmost child first, respecting postorder traversal
                for child in node.children[::-1]:
                    stack.append((child, False))

        return res  # Return the final postorder traversal result
