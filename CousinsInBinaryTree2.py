from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time: O(n), Space: O(n)
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_sums = []  # To store sum of node values at each level
        q = deque([root])  # Initialize queue for level-order traversal (BFS)

        # First pass: Calculate sum of values at each level
        while q:
            cur_sum = 0  # Reset current level sum
            for i in range(len(q)):  # Loop through nodes at the current level
                node = q.popleft()  # Pop node from queue
                if node:
                    cur_sum += node.val  # Add node's value to current level sum
                # Append left and right children to the queue for the next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_sums.append(cur_sum)  # Store sum of the current level

        # Second pass: Replace each node's value with the sum of its cousins
        q = deque([(root, root.val)])  # Start with the root, track node and sum of siblings
        level = 0  # Track current level
        while q:
            for i in range(len(q)):  # Process all nodes at the current level
                node, sibling_sum = q.popleft()  # Pop node and its sibling sum
                # Replace node's value with the total level sum minus its sibling sum
                node.val = level_sums[level] - sibling_sum

                child_sum = 0  # Sum of current node's children's values
                # Calculate the sum of the left and right children's values
                if node.left:
                    child_sum += node.left.val
                if node.right:
                    child_sum += node.right.val
                # Append children to the queue for the next level
                if node.left:
                    q.append((node.left, child_sum))
                if node.right:
                    q.append((node.right, child_sum))
            level += 1  # Move to the next level

        return root  # Return the modified tree
