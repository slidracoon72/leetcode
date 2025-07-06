from typing import List


class Solution:
    # Time: O(n), Space: O(1)
    def maxAscendingSum(self, nums: List[int]) -> int:
        temp = res = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                temp += nums[i]  # extend current subarray
            else:
                temp = nums[i]  # start a new subarray
            res = max(res, temp)
        return res


c = Solution()
nums = [10, 20, 30, 5, 10, 50]
print(c.maxAscendingSum(nums))
