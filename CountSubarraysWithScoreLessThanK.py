# LC - Hard
from typing import List


class Solution:
    # Sliding Window
    # Time: O(n), Space: O(1)
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Initialize variables
        res = 0
        total = 0  # Sum of the current window
        l, r = 0, 0

        # Slide the window
        while r < len(nums):
            total += nums[r]  # Add the current element to the window sum

            # Shrink the window while the score is >= k
            while l <= r and total * (r - l + 1) >= k:
                total -= nums[l]  # Remove the leftmost element
                l += 1

            # Count all subarrays ending at r: [l, r], [l+1, r], ..., [r, r]
            res += r - l + 1
            r += 1

        return res


c = Solution()
nums = [2, 1, 4, 3, 5]
k = 10
print(c.countSubarrays(nums, k))
