from typing import List


# Neetcode: https://www.youtube.com/watch?v=q0s6m7AiM7o
# This is a backtracking solution to generate all possible combinations of `k` numbers out of the range [1, n].
# Time Complexity: O(n^k) - Though in practice, the backtracking process makes this more efficient than a simple brute-force solution.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []  # List to store all the valid combinations

        # Helper function for backtracking
        def backtrack(start, comb):
            # Base case: If the combination has reached the required length `k`
            if len(comb) == k:
                res.append(comb.copy())  # Add the current combination to the result list
                return

            # Iterate over the possible numbers starting from `start` to `n`
            for i in range(start, n + 1):
                comb.append(i)  # Add the current number to the combination
                backtrack(i + 1, comb)  # Recurse with the next number as the starting point
                comb.pop()  # Backtrack by removing the last number added

        backtrack(1, [])  # Initial call to the backtracking function starting with 1 and an empty combination
        return res  # Return the list of all combinations

    # My solution
    # Similar to Subsets.py
    def combine1(self, n: int, k: int) -> List[List[int]]:
        res = []  # This will store all valid combinations

        def dfs(i, cur):
            # Base case: if current combination has k elements, add to result
            if len(cur) == k:
                res.append(cur.copy())  # Make a copy to avoid mutation
                return

            # Base case: if index exceeds n, stop the recursion
            if i > n:
                return

            # Recursive case 1: include current number i in the combination
            cur.append(i)
            dfs(i + 1, cur)

            # Backtrack: remove i and explore the path without including it
            cur.pop()
            dfs(i + 1, cur)

        # Start DFS from 1 with an empty combination
        dfs(1, [])
        return res  # Return the list of all combinations


c = Solution()
n = 4
k = 2
print(c.combine(n, k))  # Output should be all combinations of 2 numbers from the range [1, 4]
