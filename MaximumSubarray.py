from typing import List


class Solution:
    # Kadane's Algorithm
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = nums[0]  # Initialize with the first element

        current_sum = nums[0]

        for i in range(1, n):
            # Choose the current element or extend the current subarray
            current_sum = max(nums[i], current_sum + nums[i])

            # Update the global maximum
            max_sum = max(max_sum, current_sum)

        return max_sum


c = Solution()
a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(c.maxSubArray(a))
