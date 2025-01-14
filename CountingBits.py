from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_bits(x):
            count = 0
            while x:
                count += x % 2
                x = x >> 1
            return count

        res = []
        for i in range(n + 1):
            res.append(count_bits(i))

        return res

    # Optimized - Using Dynamic Programming
    # Time: O(n), Space: O(n)
    # Neetcode: https://www.youtube.com/watch?v=RyBM56RIWrM&ab_channel=NeetCode
    def countBits1(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp


c = Solution()
n = 5
print(c.countBits(n))
print(c.countBits1(n))
