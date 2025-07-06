from typing import List


class Solution:
    # Time: O(n), Space: O(1)
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        n = len(s)

        for i in range(0, n, k):
            res.append(s[i: i + k])

        l = len(res[-1])
        if l != k:
            res[-1] += fill * (k - l)

        return res


c = Solution()
s = "abcdefghij"
k = 3
fill = "x"
print(c.divideString(s, k, fill))
