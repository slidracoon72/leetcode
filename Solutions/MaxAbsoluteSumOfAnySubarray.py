from typing import List


# Solved using Kadane's Algorithm
# Time: O(n), Space: O(1)
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)  # Get the length of the input array
        max_sum = min_sum = nums[0]  # Initialize max and min subarray sums to the first element
        max_cur_sum = min_cur_sum = nums[0]  # Initialize current running sums

        for i in range(1, n):  # Iterate through the array starting from the second element
            # Update the maximum subarray sum
            max_cur_sum = max(nums[i], max_cur_sum + nums[i])  # Extend the subarray or start fresh
            max_sum = max(max_sum, max_cur_sum)  # Update max_sum if a larger sum is found

            # Update the minimum subarray sum
            min_cur_sum = min(nums[i], min_cur_sum + nums[i])  # Extend the subarray or start fresh
            min_sum = min(min_sum, min_cur_sum)  # Update min_sum if a smaller sum is found

        # Return the maximum absolute sum found between max_sum and min_sum
        return max(abs(max_sum), abs(min_sum))


c = Solution()
nums = [2, -5, 1, -4, 3, -2]
print(c.maxAbsoluteSum(nums))
