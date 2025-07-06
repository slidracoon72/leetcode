from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            res[i] = nums[nums[i]]

        return res


c = Solution()
nums = [5, 0, 1, 2, 3, 4]
print(c.buildArray(nums))
