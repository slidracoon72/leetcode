from collections import deque, defaultdict
from typing import Optional, List


# LC - Hard

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Getting TLE (30/40 test cases pass)
class Solution:
    def cloneTree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node:
            return None
        new_node = TreeNode(node.val)
        new_node.left = self.cloneTree(node.left)
        new_node.right = self.cloneTree(node.right)
        return new_node

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        res = []
        for query in queries:
            root_copy = self.cloneTree(root)
            q = deque([root_copy])

            while q:
                node = q.popleft()
                if node:
                    if node.left:
                        if node.left.val != query:
                            q.append(node.left)
                        else:
                            node.left = None
                    if node.right:
                        if node.right.val != query:
                            q.append(node.right)
                        else:
                            node.right = None

            res.append(self.maxDepth(root_copy) - 1)

        return res


class Solution2:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # Dictionary to store the height of each node to avoid recalculating
        memo = {}

        # Helper function to calculate the height of a node
        def height(node):
            # Base case: If the node is None, height is -1
            if not node:
                return -1
            # If the height of the node is already calculated, return it from memo
            if node.val in memo:
                return memo[node.val]
            # Calculate height as 1 + max height of left and right children
            memo[node.val] = max(height(node.left), height(node.right)) + 1
            return memo[node.val]

        # Dictionary to store max height of tree after removing each node
        results = defaultdict(int)

        # Depth-first search to calculate max height for each node removal
        def dfs(node, depth, max_height):
            # Base case: If the node is None, return
            if not node:
                return
            # Store the max height after removing the current node
            results[node.val] = max_height
            # Recursive DFS on the left child with updated max height
            dfs(node.left, depth + 1, max(max_height, depth + 1 + height(node.right)))
            # Recursive DFS on the right child with updated max height
            dfs(node.right, depth + 1, max(max_height, depth + 1 + height(node.left)))

        # Initial DFS call to populate results for each node
        dfs(root, 0, 0)
        print(results)

        # For each query, return the max height after removing the queried node
        return [results[query] for query in queries]
