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


c = Solution()
nums = [1, 2, 3, 3, 2, 2]
print(c.longestSubarray(nums))
