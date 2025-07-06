# LC-3392: Count Subarrays of Length Three With a Condition
from typing import List


class Solution:
    # Time: O(n), Space: O(1)
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        first, second = nums[0], nums[1]
        for r in range(2, n):
            third = nums[r]
            if first + third == second / 2:
                res += 1
            first = second
            second = third

        return res


c = Solution()
nums = [1, 2, 1, 4, 1]
print(c.countSubarrays(nums))
