from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Memoization cache to store results of sub-problems
        # The key is a tuple (index, total), and the value is the number of ways
        # to reach the target with that (index, total)
        dp = {}

        def backtrack(i, total):
            # Base case: If we've processed all elements
            if i == len(nums):
                # If the current total equals the target, we've found a valid way
                return 1 if total == target else 0

            # Check if the result for this sub-problem is already computed
            if (i, total) in dp:
                return dp[(i, total)]

            # Recursive case: Compute the number of ways to reach the target
            # by including the current number with a '+' sign and a '-' sign
            # Try both possible choices for the current number
            include_positive = backtrack(i + 1, total + nums[i])
            include_negative = backtrack(i + 1, total - nums[i])

            # Store the computed result in the cache
            dp[(i, total)] = include_positive + include_negative

            # Return the result for this sub-problem
            return dp[(i, total)]

        # Start the backtracking process from index 0 and initial total 0
        return backtrack(0, 0)
