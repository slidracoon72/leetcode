from typing import List


class Solution:
    # Sliding Window
    # Time: O(n), Space: O(1)
    def longestSubarray(self, nums: List[int]) -> int:
        # Count of zeros in the current window
        zeros = 0
        # Store the maximum length of valid subarray found
        res = 0

        # Left pointer of the sliding window
        l = 0
        # Iterate through the array with the right pointer
        for r in range(len(nums)):
            # If we encounter a zero, increase the zero count
            if nums[r] == 0:
                zeros += 1

            # Shrink the window from the left if we have more than 1 zero
            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            # Update the result with the current valid window length
            # (subtracting 1 implicitly accounts for deleting one zero)
            res = max(res, r - l)

        # Return the maximum length of subarray after deleting one element
        return res


c = Solution()
nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
print(c.longestSubarray(nums))
