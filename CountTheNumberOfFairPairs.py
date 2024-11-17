from typing import List


class Solution:
    # Neetcode: https://www.youtube.com/watch?v=TjthKf7Mc_8&ab_channel=NeetCodeIO
    # Time: O(n log n), Space: O(1)
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # Helper function to perform binary search
        # Returns the largest index i where nums[i] < target
        def binary_search(l, r, target):
            while l <= r:
                mid = l + (r - l) // 2  # Find the midpoint between l and r
                if nums[mid] >= target:  # If the midpoint value is too high,
                    r = mid - 1  # move the right boundary leftward.
                else:  # Otherwise, move the left boundary rightward.
                    l = mid + 1
            return r  # Return the index where nums[i] is < target

        # Sort nums to allow binary searching for ranges
        nums.sort()
        res = 0  # Initialize result counter

        # Loop through each element in nums to consider it as part of a fair pair
        for i in range(len(nums)):
            low = lower - nums[i]  # Calculate lower bound for the pair
            up = upper - nums[i]  # Calculate upper bound for the pair

            # Find the highest index of elements <= 'up' by binary search
            upper_valid = binary_search(i + 1, len(nums) - 1, up + 1)

            # Find the highest index of elements < 'low' by binary search
            lower_invalid = binary_search(i + 1, len(nums) - 1, low)

            # The difference between upper_valid and lower_invalid gives
            # the count of valid pairs that fall within the range [lower, upper]
            res += upper_valid - lower_invalid

        return res  # Return the total count of fair pairs

    # Brute Force - Gives TLE
    # Time: O(n^2)
    def countFairPairs1(self, nums: List[int], lower: int, upper: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if lower <= nums[i] + nums[j] <= upper:
                    res += 1
        return res


c = Solution()
nums = [0, 1, 7, 4, 4, 5]
lower = 3
upper = 6
print(c.countFairPairs(nums, lower, upper))
