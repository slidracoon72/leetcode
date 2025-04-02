from typing import List
from functools import lru_cache


class Solution:
    # DP - Recursion with Memoization - @lru_cache(None)
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        # Memoize the recursive function using lru_cache
        @lru_cache(None)
        def dfs(i):
            # Base case: if index is out of bounds, no more points to gain
            if i >= n:
                return 0

            # Get points and brainpower for the current question
            points, brainpower = questions[i]

            # Option 1: Solve the current question
            # Gain points[i] and skip brainpower[i] questions, recurse at i + brainpower[i] + 1
            include = points + dfs(i + 1 + brainpower)

            # Option 2: Skip the current question, recurse at i + 1
            skip = dfs(i + 1)

            # Return the maximum points from the two choices
            return max(include, skip)

        # Start recursion from index 0
        return dfs(0)

    # DP - Recursion with Memoization - Hash-Map
    def mostPoints1(self, questions: List[List[int]]) -> int:
        # Get the number of questions
        n = len(questions)
        # Initialize a dictionary to store memoized results (index -> max points)
        memo = {}

        # Define recursive function to compute max points starting from index i
        def dfs(i):
            # Base case: if index is out of bounds, no more points can be gained
            if i >= n:
                return 0
            # If result for this index is already memoized, return it
            if i in memo:
                return memo[i]

            # Extract points and brainpower for the current question
            points, brainpower = questions[i]

            # Option 1: Solve the current question
            # Gain points[i] and skip brainpower[i] questions, recurse at i + brainpower[i] + 1
            include = points + dfs(i + 1 + brainpower)
            # Option 2: Skip the current question, recurse at i + 1
            skip = dfs(i + 1)
            # Store the maximum of the two options in memo
            memo[i] = max(include, skip)
            # Return the result for this index
            return memo[i]

        # Start recursion from the first question (index 0)
        return dfs(0)


c = Solution()
questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
print(c.mostPoints(questions))
print(c.mostPoints1(questions))
