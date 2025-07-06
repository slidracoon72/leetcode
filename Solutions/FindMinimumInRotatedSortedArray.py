from typing import List


# Solved using Binary Search
# TIme Complexity: O(log n)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]


c = Solution()
nums = [3, 4, 5, 6, 1, 2]
print(c.findMin(nums))
