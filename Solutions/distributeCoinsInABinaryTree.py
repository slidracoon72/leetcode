from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Neetcode: https://www.youtube.com/watch?v=YfdfIOeV_RU
# Time: O(N) (as DFS is used), Space: O(H)
class Solution:
    # Keeping track of current tree size and extra coins
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0  # Initialize the result variable to store the number of moves required

        def dfs(cur):
            if not cur:
                # Base case: if the current node is null, return [0, 0]
                return [0, 0]  # [size of current tree, no. of coins]

            # Recursively traverse the left and right subtrees
            l_size, l_coins = dfs(cur.left)
            r_size, r_coins = dfs(cur.right)

            # Calculate the total size (number of nodes) and coins in the current subtree
            size = 1 + l_size + r_size  # Current node + left subtree nodes + right subtree nodes
            coins = cur.val + l_coins + r_coins  # Current node coins + left subtree coins + right subtree coins

            # The number of moves needed to balance the current subtree is the absolute difference
            # between the number of nodes and the number of coins in this subtree
            self.res += abs(size - coins)

            return [size, coins]  # Return the size and coin count for the current subtree

        dfs(root)  # Start the DFS traversal from the root
        return self.res  # Return the total number of moves required

    # Keeping track of only extra coins
    def distributeCoins2(self, root: Optional[TreeNode]) -> int:
        self.res = 0  # Initialize the result variable to store the total number of moves required

        def dfs(cur):
            if not cur:
                return 0  # Base case: if the current node is null, no extra coins

            # Recursively traverse the left and right subtrees
            l_extra = dfs(cur.left)  # Calculate the number of extra coins in the left subtree
            r_extra = dfs(cur.right)  # Calculate the number of extra coins in the right subtree

            # Calculate the total number of extra coins in the current subtree
            extra_coins = (cur.val - 1) + l_extra + r_extra

            # Update the total number of moves required by adding the absolute value of extra_coins
            self.res += abs(extra_coins)

            return extra_coins  # Return the total number of extra coins in the current subtree

        dfs(root)  # Start the DFS traversal from the root
        return self.res  # Return the total number of moves required to distribute coins evenly
