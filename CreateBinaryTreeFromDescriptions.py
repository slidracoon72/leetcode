from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time & Space Complexity: O(n)
# Neetcode: https://www.youtube.com/watch?v=yWkrFfqO7NA
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # Dictionary to hold the TreeNode objects for each value
        nodes = {}
        # Set to keep track of all child nodes
        children = set()

        # Iterate through each description to build the tree nodes and their relationships
        for par, child, is_left in descriptions:
            # Add the child node to the set of children
            children.add(child)
            # If the parent node is not already in the nodes dictionary, create it
            if par not in nodes:
                nodes[par] = TreeNode(par)
            # If the child node is not already in the nodes dictionary, create it
            if child not in nodes:
                nodes[child] = TreeNode(child)

            # Establish the left or right child relationship based on is_left value
            if is_left == 1:
                nodes[par].left = nodes[child]
            else:
                nodes[par].right = nodes[child]

        # Identify the root node by finding a node that is not anyone's child
        for par, child, is_left in descriptions:
            if par not in children:
                # Return the root node
                return nodes[par]

# c = Solution()
# descriptions = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]
# print(c.createBinaryTree(descriptions))
