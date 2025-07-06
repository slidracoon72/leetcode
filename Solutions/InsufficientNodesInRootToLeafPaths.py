# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time Complexity: O(n), where n is the number of nodes
    # Space Complexity: O(h), where h is the height of the tree
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        # DFS to check if there exists a path with sum >= limit
        # Returns True if a sufficient path exists, False otherwise
        def dfs(node: TreeNode, path_sum: int) -> bool:
            if not node:
                return False

            # Update path sum
            path_sum += node.val

            # If it's a leaf, check the path sum
            if not node.left and not node.right:
                return path_sum >= limit

            # Recursively check left and right subtrees
            left_sufficient = dfs(node.left, path_sum)
            right_sufficient = dfs(node.right, path_sum)

            # Delete subtrees if insufficient
            if not left_sufficient:
                node.left = None
            if not right_sufficient:
                node.right = None

            # Return True if at least one sufficient path exists
            return left_sufficient or right_sufficient

        # Run DFS from the root
        return None if not dfs(root, 0) else root
