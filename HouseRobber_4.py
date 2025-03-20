from typing import List


class Solution:
    # Similar to KokoEatingBananas.py
    # Solved using Binary Search
    # Time: O(n * log m), Space: O(1)
    def minCapability(self, nums: List[int], k: int) -> int:
        # Set binary search range: min capability is 1, max is largest house value
        l, r = 1, max(nums)
        res = r  # Initialize result to max value, will minimize it

        # Binary search for minimum capability
        while l <= r:
            mid = (l + r) // 2  # Midpoint capability to test
            count = 0  # Count of houses that can be robbed

            i = 0
            # Compute how many houses can be robbed with capability 'mid'
            while i < len(nums):
                if nums[i] <= mid:  # If house value fits within capability
                    count += 1
                    i += 2  # Skip next house (no adjacent robbing)
                else:
                    i += 1  # Move to next house

            # Check if current capability is feasible
            if count >= k:  # If we can rob at least k houses
                res = min(res, mid)  # Update result with smallest valid capability
                r = mid - 1  # Try a smaller capability
            else:  # If not enough houses robbed
                l = mid + 1  # Increase capability

        return res


c = Solution()
nums = [2, 3, 5, 9]
k = 2
print(c.minCapability(nums, k))
