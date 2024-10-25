from collections import defaultdict, deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time: O(n), Space: O(n)
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # Dictionary to store nodes at each column index
        col_table = defaultdict(list)
        q = deque([(root, 0)])  # (node, column index)

        while q:
            node, col = q.popleft()
            if node:
                col_table[col].append(node.val)
                q.append((node.left, col - 1))  # Left child goes to col - 1
                q.append((node.right, col + 1))  # Right child goes to col + 1

        # Sorting columns and returning result
        return [col_table[x] for x in sorted(col_table.keys())]
