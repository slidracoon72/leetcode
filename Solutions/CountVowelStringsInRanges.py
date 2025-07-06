from typing import List


class Solution:
    # Passes 92/93 test cases
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        ind = []
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                ind.append(i)

        res = []
        for s, e in queries:
            c = 0
            for i in ind:
                if s <= i <= e:
                    c += 1
            res.append(c)
        return res

    # Solved using Prefix Sum
    # Time: O(n + q), Space: O(n)
    def vowelStrings1(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # Step 1: Create a prefix sum array for vowel strings
        n = len(words)
        prefix_sum = [0] * (n + 1)  # One extra for 0-based indexing

        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                prefix_sum[i + 1] = prefix_sum[i] + 1
            else:
                prefix_sum[i + 1] = prefix_sum[i]

        # Step 2: Answer each query using the prefix sum array
        res = []
        for s, e in queries:
            res.append(prefix_sum[e + 1] - prefix_sum[s])  # Inclusive count between indices s and e

        return res


c = Solution()
words = ["aba", "bcb", "ece", "aa", "e"]
queries = [[0, 2], [1, 4], [1, 1]]
print(c.vowelStrings1(words, queries))
