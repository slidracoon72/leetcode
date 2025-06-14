from typing import List


class Solution:
    # Similar to KokoEatingBananas.py
    # Solved using Binary Search
    # Time: O(nlogn + mlogm), Space: O(n)
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # Define search space: min difference is 0, max is largest possible difference
        nums.sort()  # Sort to pair adjacent elements
        l, r = 0, nums[-1] - nums[0]  # l=0 (smallest diff), r=max diff in sorted nums

        # Initialize result to the maximum possible difference
        res = r  # Start with max value; we'll minimize it

        # Binary search to find the minimum maximum difference
        while l <= r:
            # Calculate mid-point difference to test
            d = (l + r) // 2  # d is the maximum allowed difference for pairs

            # Compute number of pairs with difference <= d
            pairs = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= d:  # Can form a pair
                    pairs += 1
                    i += 2  # Skip both indices (pair formed)
                else:
                    i += 1  # Skip current index

            # Check if current difference d is feasible
            if pairs >= p:  # If enough pairs formed
                res = min(res, d)  # Update result with smallest valid difference
                r = d - 1  # Try a smaller difference to minimize d
            else:  # If not enough pairs
                l = d + 1  # Increase difference to form more pairs

        # Return the minimum maximum difference found
        return res


c = Solution()
nums = [10, 1, 2, 7, 1, 3]
p = 2
print(c.minimizeMax(nums, p))
