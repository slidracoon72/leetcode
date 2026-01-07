from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert wordDict to a set for O(1) lookup
        wordSet = set(wordDict)

        # Memoization dictionary to store results for starting index i
        memo = {}

        def dfs(i):
            # If we have reached the end of the string,
            # it means the string can be segmented successfully
            if i == len(s):
                return True

            # If this subproblem has already been solved, return the cached result
            if i in memo:
                return memo[i]

            # Try all possible substrings starting at index i
            for j in range(i + 1, len(s) + 1):
                # If substring s[i:j] is a valid word and the remaining string
                # can also be segmented, return True
                if s[i:j] in wordSet and dfs(j):
                    memo[i] = True
                    return True

            # If no valid segmentation is found starting at index i
            memo[i] = False
            return False

        # Start DFS from index 0
        return dfs(0)
