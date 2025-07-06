from typing import List


# Sorting + Sliding Window
class Solution:
    # Time: O(n log n), Space: O(1)
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Sort the array to process elements in increasing order
        nums.sort()

        # Initialize result (max frequency) and total sum of the window
        res, total = 0, 0

        # Initialize the sliding window pointers
        l, r = 0, 0
        while r < len(nums):
            # Add the current element to the window's total sum
            total += nums[r]

            # Shrink the window while the cost to make all elements equal to nums[r]
            # exceeds the allowed operations (k)
            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]  # Remove the leftmost element from the total
                l += 1  # Shrink the window from the left

            # Update the maximum frequency (window size)
            res = max(res, r - l + 1)
            r += 1  # Expand the window to the right

        return res


c = Solution()
nums = [1, 2, 4]
k = 5
print(c.maxFrequency(nums, k))
