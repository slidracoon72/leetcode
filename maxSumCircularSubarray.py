from typing import List


# Kaden's Algorithm
# Neetcode: https://www.youtube.com/watch?v=fxT9KjakYPM
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax = curMin = total = 0
        globalMax = globalMin = nums[0]

        for n in nums:
            curMax = max(n, curMax + n)
            curMin = min(n, curMin + n)
            globalMax = max(globalMax, curMax)
            globalMin = min(globalMin, curMin)
            total += n

        if globalMax > 0:
            return max(globalMax, total - globalMin)
        else:
            return globalMax
