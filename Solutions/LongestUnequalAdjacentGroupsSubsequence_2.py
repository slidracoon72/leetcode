from typing import List
from functools import lru_cache


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        # Helper function to calculate Hamming distance between two same-length words
        def hamming(w1: str, w2: str) -> int:
            return sum(x != y for x, y in zip(w1, w2))

        n = len(words)

        # DFS with memoization to find the longest valid subsequence starting at index i
        @lru_cache(None)
        def dfs(i: int) -> List[int]:
            best = [i]  # Store the best sequence starting from index i
            for j in range(i + 1, n):
                # Conditions to continue the subsequence:
                # - Different group than previous
                # - Same length
                # - Hamming distance of 1
                if groups[i] != groups[j] and len(words[i]) == len(words[j]) and hamming(words[i], words[j]) == 1:
                    next_seq = dfs(j)
                    if len(next_seq) + 1 > len(best):
                        best = [i] + next_seq
            return best

        best_seq = []  # Store the best overall subsequence

        # Try to build the longest subsequence starting from each word
        for i in range(n):
            curr_seq = dfs(i)
            if len(curr_seq) > len(best_seq):
                best_seq = curr_seq

        # Convert indices to actual words
        return [words[i] for i in best_seq]


c = Solution()
words = ["bab", "dab", "cab"]
groups = [1, 2, 2]
print(c.getWordsInLongestSubsequence(words, groups))
