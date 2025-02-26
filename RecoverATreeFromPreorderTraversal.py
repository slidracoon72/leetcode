# LC - Hard
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solved using Stack
# Time: O(N), Space: O(N)
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        dash = 0  # Tracks the depth of the current node based on the number of dashes
        stack = []  # Stack to maintain the hierarchy of tree nodes
        i = 0  # Pointer for iterating through the traversal string

        while i < len(traversal):
            # Count the number of consecutive dashes to determine the depth
            if traversal[i] == "-":
                dash += 1
                i += 1
            else:
                # Find the numeric value of the node
                j = i
                while j < len(traversal) and traversal[j] != "-":
                    j += 1
                val = int(traversal[i:j])  # Convert the extracted substring to an integer
                node = TreeNode(val)  # Create a new tree node

                # Ensure stack only contains nodes at the correct depth
                while len(stack) > dash:
                    stack.pop()

                # Attach the new node to its correct parent
                if stack:
                    if not stack[-1].left:
                        stack[-1].left = node  # Assign as left child if available
                    else:
                        stack[-1].right = node  # Otherwise, assign as right child

                # Push the new node onto the stack
                stack.append(node)

                # Reset depth counter and move the pointer
                dash = 0
                i = j

        return stack[0]  # Return the root node, which is the first element in the stack
