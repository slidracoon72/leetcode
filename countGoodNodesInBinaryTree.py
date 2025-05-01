# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: O(N), Space: O(N)
class Solution:
    # DFS
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            # Count current node as a good node if its value is greater than or equal to the maximum value in the path
            count = 1 if node.val >= max_val else 0
            # Update the maximum value in the path
            max_val = max(max_val, node.val)
            # Recursively count good nodes in the left and right subtrees
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)
            return count

        return dfs(root, float('-inf'))

    # BFS
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque()
        q.append((root, -float('inf')))

        while q:
            node, maxval = q.popleft()
            if node.val >= maxval:
                res += 1

            maxVal = max(maxval, node.val)

            if node.left:
                q.append((node.left, maxVal))

            if node.right:
                q.append((node.right, maxVal))

        return res
