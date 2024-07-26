from typing import List


class Solution:
    # Time Complexity: O(N) ; n = length of array
    def findPeakElement(self, nums: List[int]) -> int:
        l = len(nums)
        if l <= 1: return 0
        if l > 1 and nums[0] > nums[1]:
            return 0
        if l > 1 and nums[-1] > nums[-2]:
            return l - 1
        for i in range(1, l):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i

    # Time Complexity: O(log N) ; n = length of array
    # Implementing using Binary Search - Better Solution
    def findPeakElement_BinarySearch(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2  # --> avoids integer overflow
            # mid = (left+right) // 2 --> also correct

            # Always move towards the peak (greater element)
            # left neighbor greater
            if m > 0 and nums[m] < nums[m - 1]:
                r = m - 1
            # right neighbor greater
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                l = m + 1
            else:
                return m


c = Solution()
nums = [1, 2, 3, 1]
nums1 = [1, 2, 1, 3, 5, 6, 4]
print(c.findPeakElement(nums))
print(c.findPeakElement(nums1))
print(c.findPeakElement_BinarySearch(nums))
print(c.findPeakElement_BinarySearch(nums1))
