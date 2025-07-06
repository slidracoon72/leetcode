# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Neetcode: https://www.youtube.com/watch?v=f_epkBeS1LQ
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # Initialize the number of good leaf node pairs to 0
        self.pairs = 0

        # Depth-First Search (DFS) function
        def dfs(node):
            # If the node is None (base case for recursion), return an empty list
            if not node:
                return []

            # If the node is a leaf (no children), return a list with a single element 1
            if not node.left and not node.right:
                return [1]

            # Recursively get the distances from left and right subtrees
            left_dist = dfs(node.left)
            right_dist = dfs(node.right)

            # Check pairs of distances from left and right subtrees
            for d1 in left_dist:
                for d2 in right_dist:
                    # If the sum of distances is less than or equal to the given distance, it's a good pair
                    if d1 + d2 <= distance:
                        self.pairs += 1

            # Collect all distances from both left and right subtrees, incremented by 1
            # This is because we're moving one level up in the tree
            all_dist = left_dist + right_dist
            return [d + 1 for d in all_dist]

        # Call the DFS function starting from the root
        dfs(root)

        # Return the total number of good pairs found
        return self.pairs
