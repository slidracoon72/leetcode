# LC - Hard
# LC - 1639 Number of Ways to Form a Target String Given a Dictionary

from typing import List
from collections import defaultdict


# Dynamic Programming - (DFS Recursive)
# Neetcode: https://www.youtube.com/watch?v=_GF-0T-YjW8&ab_channel=NeetCodeIO
# Time: O(n*m*k), Space: O(n*m)
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = (10 ** 9) + 7  # Modular arithmetic to handle large numbers

        # Count occurrences of each character at each position across all words
        cnt = defaultdict(int)  # (index, char) -> count of char at index across all words
        for word in words:
            for i, c in enumerate(word):
                cnt[(i, c)] += 1

        dp = {}  # Memoization dictionary to store results of subproblems

        # Key: (i, k) where `i` is the index in target and `k` is the index in words[0]
        # Value: Number of ways to form `target[i:]` using `words[][k:]`

        def dfs(i, k):
            """
            Recursive function to compute the number of ways to form `target[i:]`
            using characters from the `k-th` column onwards in the `words` matrix.
            """
            # Base case: Successfully formed the entire target
            if i == len(target):
                return 1
            # Base case: Exhausted all columns in the words matrix without forming the target
            if k == len(words[0]):
                return 0
            # If the result is already computed, return it
            if (i, k) in dp:
                return dp[(i, k)]

            c = target[i]  # Current character in the target we are trying to form

            # Option 1: Skip the current column `k` in the words matrix
            dp[(i, k)] = dfs(i, k + 1)

            # Option 2: Use the current column `k` in the words matrix
            # Multiply the count of `c` at position `k` by the number of ways to form `target[i+1:]`
            dp[(i, k)] += cnt[(k, c)] * dfs(i + 1, k + 1)

            # Return the result modulo `mod` to prevent overflow
            return dp[(i, k)] % mod

        # Start the recursive computation from the beginning of the target and the words matrix
        return dfs(0, 0)


c = Solution()
words = ["acca", "bbbb", "caca"]
target = "aba"
print(c.numWays(words, target))
