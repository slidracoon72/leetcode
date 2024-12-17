# 2779. Maximum Beauty of an Array After Applying Operation

from typing import List


class Solution:
    # Using Sliding Window
    # Neetcode: https://www.youtube.com/watch?v=x29QnzSBFVI&ab_channel=NeetCodeIO
    # Time Complexity: O(nlogn) - for sorting the input array
    # Space Complexity: O(n) - for sorting and any additional space used by the sort function
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # Sort the array to allow for a sliding window approach
        nums.sort()
        res = 0  # Variable to store the maximum beauty (length of the valid subarray)
        l = 0  # Left pointer of the sliding window

        # Iterate through the array with the right pointer
        for r in range(len(nums)):
            # Shrink the window if the difference between the current right element
            # and the leftmost element exceeds 2 * k
            while nums[r] - nums[l] > 2 * k:
                l += 1  # Move the left pointer to the right to shrink the window

            # Update the result with the maximum size of the valid subarray
            res = max(res, r - l + 1)

        # Return the maximum beauty (size of the largest valid subarray)
        return res
