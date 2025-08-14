# LC-2419: Longest Subarray With Maximum Bitwise AND
from typing import List


class Solution:
    # Time: O(n), Space: O(1)
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        l = len(nums)
        res, size = 0, 0
        for i in range(l):
            if nums[i] == m:
                size += 1
                res = max(res, size)
            else:
                size = 0
        return res

    # Similar as above
    # Time: O(n), Space: O(1)
    def longestSubarray1(self, nums: List[int]) -> int:
        max_and = max(nums)

        res = 0
        l, r = 0, 0
        while r < len(nums):
            while r < len(nums) and nums[r] == max_and:
                r += 1
            res = max(res, r - l)
            r += 1
            l = r

        return res


c = Solution()
nums = [1, 2, 3, 3, 2, 2]
print(c.longestSubarray(nums))
