from collections import defaultdict
from typing import List


# LC-2958. Length of Longest Subarray With at Most K Frequency
# Sliding Window Problem
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # Dictionary to count the frequency of each element in the current window
        count = defaultdict(int)
        max_length = 0
        l = 0

        # Iterate over each element with the right pointer
        for r in range(len(nums)):
            count[nums[r]] += 1

            # Ensure the window is valid by shrinking from the left if needed
            while count[nums[r]] > k:
                # Shift left window
                count[nums[l]] -= 1
                l += 1

            # Update the maximum length of the valid window
            max_length = max(max_length, r - l + 1)

        return max_length


c = Solution()
nums = [1, 2, 3, 1, 2, 3, 1, 2]
k = 2
print(c.maxSubarrayLength(nums, k))
