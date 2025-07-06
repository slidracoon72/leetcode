from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        a1, a2 = 0, float('inf')

        for c in count:
            if count[c] % 2:
                a1 = max(a1, count[c])
            else:
                a2 = min(a2, count[c])

        return a1 - a2


c = Solution()
s = "aaaaabbc"
print(c.maxDifference(s))
