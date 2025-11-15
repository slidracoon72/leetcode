from collections import Counter


class Solution:
    # Time: O(n), Space: O(26) = O(1)
    def maxFreqSum(self, s: str) -> int:
        vowels = "aeiou"
        count = Counter(s)

        v, c = 0, 0
        for key, freq in count.items():
            if key in vowels:
                v = max(v, freq)
            else:
                c = max(c, freq)

        return v + c


c = Solution()
print(c.maxFreqSum("successes"))
print(c.maxFreqSum("aeiaeia"))
