from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)

        # Initialize result with the absolute difference between first and last elements
        # This handles the circular adjacency (i.e., nums[n-1] and nums[0])
        res = abs(nums[0] - nums[-1])

        # Iterate through the array to find the maximum absolute difference
        # between adjacent elements
        for i in range(n - 1):
            diff = abs(nums[i] - nums[i + 1])  # Difference between nums[i] and next element
            res = max(res, diff)  # Update result if this difference is greater

        return res  # Return the maximum adjacent difference found


c = Solution()
nums = [1, 2, 4]
print(c.maxAdjacentDistance(nums))
