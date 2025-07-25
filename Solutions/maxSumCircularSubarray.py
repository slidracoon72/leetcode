from typing import List


# Kaden's Algorithm
# Neetcode: https://www.youtube.com/watch?v=fxT9KjakYPM
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax, globMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for num in nums:
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            total += num
            globMax = max(globMax, curMax)
            globMin = min(globMin, curMin)

        return max(globMax, total - globMin) if globMax > 0 else globMax


c = Solution()
nums = [-2, 4, -5, 4, -5, 9, 4]
print(c.maxSubarraySumCircular(nums))
