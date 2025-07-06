from typing import List


class Solution:
    # Time: O(n^2 * L)
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1: str, str2: str) -> bool:
            return str1 == str2[:len(str1)] and str1 == str2[-len(str1):]
            # return str2.startswith(str1) and str2.endswith(str1)

        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    res += 1

        return res


c = Solution()
words = ["a", "aba", "ababa", "aa"]
print(c.countPrefixSuffixPairs(words))
