# LC - Hard
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        min_i = max_i = bad_i = -1  # Track the latest indices of minK, maxK, and invalid elements

        for i, n in enumerate(nums):
            # If the current number is out of the valid range, update bad index
            if n < minK or n > maxK:
                bad_i = i

            # Update the latest index where minK was found
            if n == minK:
                min_i = i
            # Update the latest index where maxK was found
            if n == maxK:
                max_i = i

            # Count subarrays ending at index i where both minK and maxK are present,
            # and no invalid number is in between
            res += max(0, min(min_i, max_i) - bad_i)

        return res


c = Solution()
nums = [1, 3, 5, 2, 7, 5]
minK = 1
maxK = 5
print(c.countSubarrays(nums, minK, maxK))
