import collections
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:  # If the root is None, return an empty list
            return []

        res = []  # Initialize an empty list to store the result
        q = collections.deque()  # Initialize a deque to perform level-order traversal
        q.append(root)  # Enqueue the root node to start the traversal
        reverse_flag = False  # Flag to indicate whether to reverse the current level

        while q:  # Perform level-order traversal until the deque is empty
            level = []  # Initialize an empty list to store the current level nodes
            level_length = len(q)  # Get the number of nodes in the current level

            for _ in range(level_length):  # Process each node in the current level
                node = q.popleft()  # Dequeue the node from the left end of the deque
                if node:
                    level.append(node.val)  # Add the node's value to the current level list

                if node.left:  # If the node has a left child, enqueue it
                    q.append(node.left)
                if node.right:  # If the node has a right child, enqueue it
                    q.append(node.right)

            if reverse_flag and level:  # If reverse_flag is True, reverse the current level list
                level.reverse()
            reverse_flag = not reverse_flag  # Toggle the reverse_flag for the next level
            if level:
                res.append(level)  # Add the current level list to the result list

        return res  # Return the final result list containing zigzag level order traversal
