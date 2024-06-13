from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        for i in range(0, n + 1):
            if i not in nums:
                l = i
        return l


c = Solution()
a1 = [3, 0, 1]
a2 = [0, 1]
a3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(c.missingNumber(a1))
print(c.missingNumber(a2))
print(c.missingNumber(a3))
