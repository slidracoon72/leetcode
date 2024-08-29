from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Recursive Solution
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        result += self.postorderTraversal(root.left)
        result += self.postorderTraversal(root.right)
        result.append(root.val)
        return result

    # Iterative Solution
    # Neetcode: https://www.youtube.com/watch?v=QhszUQhGGlA
    # Time: O(n), Space: O(h) where n = no. of nodes, h = height of tree
    def postorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize a stack with the root node
        # The visit list keeps track of whether the node has been visited (used for postorder logic)
        stack = [root]
        visit = [False]
        res = []  # This will store the result of the postorder traversal

        # While there are nodes in the stack to process
        while stack:
            # Pop the current node and its visit status
            cur, v = stack.pop(), visit.pop()

            if cur:  # If the current node is not None
                if v:  # If the node has been visited before, add its value to the result
                    res.append(cur.val)
                else:  # If the node hasn't been visited yet
                    # Push the current node back onto the stack and mark it as visited next time
                    stack.append(cur)
                    visit.append(True)

                    # Push the right and left children onto the stack with their visit status as False
                    # We do this because in postorder traversal, we first visit the left and right children
                    # We add right, followed by left, so that when popped, left can be added first
                    stack.append(cur.right)  # Right child
                    visit.append(False)

                    stack.append(cur.left)  # Left child
                    visit.append(False)

        # Return the final postorder traversal result
        return res
