# LC - 2962: Count Subarrays Where Max Element Appears at Least K Times
from typing import List


class Solution:
    # Sliding Window
    # Time: O(n), Space: O(1)
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Find the maximum element in nums
        max_val = max(nums)

        # Initialize variables
        res = 0  # Number of valid subarrays
        count = 0  # Count of max_val in current window
        l, r = 0, 0  # Left and right pointers

        # Slide the window
        while r < n:
            # Add current element to window
            if nums[r] == max_val:
                count += 1

            # Shrink window while max_count >= k
            while l <= r and count >= k:
                res += n - r  # Count all subarrays ending at r or beyond
                if nums[l] == max_val:
                    count -= 1
                l += 1

            r += 1

        return res


c = Solution()
nums = [1, 3, 2, 3, 3]
k = 2
print(c.countSubarrays(nums, k))
