from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = float('inf')

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1

        if res == float('inf'):
            return 0
        else:
            return res


c = Solution()
target = 7
nums = [2, 3, 1, 2, 4, 3]
print(c.minSubArrayLen(target, nums))
