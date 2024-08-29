from typing import List


# Neetcode: https://www.youtube.com/watch?v=uhgdXOlGYqE
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}  # This dictionary will store the maximum number of stones Alice can collect for a given subarray of piles (l, r)

        # Helper function to perform depth-first search (DFS)
        # l: left index of the current subarray
        # r: right index of the current subarray
        # Returns: the maximum number of stones Alice can collect from the subarray piles[l:r+1]
        def dfs(l, r):
            # Base case: If the subarray is empty (l > r), return 0 since no stones can be taken
            if l > r:
                return 0

            # If the result for this subarray (l, r) has already been computed and stored in dp, return it
            if (l, r) in dp:
                return dp[(l, r)]

            # Check if it's Alice's turn. It's Alice's turn when the remaining subarray length is even.
            # (r - l) gives the current subarray length. If it's even, Alice's turn; otherwise, Bob's turn.
            even = True if (r - l) % 2 == 0 else False

            # If it's Alice's turn, she can take either the leftmost or rightmost pile
            # 'left' represents the pile Alice takes from the left side
            # 'right' represents the pile Alice takes from the right side
            # If it's not Alice's turn, both 'left' and 'right' will be 0 because Bob takes the stones instead
            left = piles[l] if even else 0
            right = piles[r] if even else 0

            # Recursively calculate the maximum number of stones Alice can collect by either:
            # 1. Taking the left pile and letting the next move be from piles[l+1:r]
            # 2. Taking the right pile and letting the next move be from piles[l:r-1]
            # Store the maximum result in dp[(l, r)]
            dp[(l, r)] = max(dfs(l + 1, r) + left, dfs(l, r - 1) + right)

            # Return the maximum number of stones Alice can collect from this subarray
            return dp[(l, r)]

        # Call the dfs function for the entire array (from the first to the last pile)
        # If Alice's total stones are greater than half of the total stones, she wins, so return True
        # Otherwise, return False (Bob wins)
        return dfs(0, len(piles) - 1) > (sum(piles)) // 2
