from typing import List


# Neetcode Solution: https://www.youtube.com/watch?v=73r3KWiEvyk
# Using Dynamic Programming
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


nums = [2, 7, 9, 3, 1]
c = Solution()
print(c.rob(nums))
