# Meta - Question
from collections import defaultdict, deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time: O(n + k log k), Space: O(n)
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

    # Time: O(n), Space: O(n)
    # No sorting required
    def verticalOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # Dictionary to store nodes at each column index
        col_table = defaultdict(list)
        q = deque([(root, 0)])  # (node, column index)
        min_col = max_col = 0

        while q:
            node, col = q.popleft()
            col_table[col].append(node.val)

            # Track the leftmost and rightmost columns seen so far
            min_col = min(min_col, col)
            max_col = max(max_col, col)

            # Only add non-null children with their updated column index
            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))

        # Build result from leftmost column to rightmost column
        return [col_table[col] for col in range(min_col, max_col + 1)]


if __name__ == "__main__":
    # Simple test case:
    #         3
    #        / \
    #       9   20
    #          /  \
    #         15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()

    print("verticalOrder:", sol.verticalOrder(root))
    print("verticalOrder2:", sol.verticalOrder2(root))
