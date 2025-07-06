from collections import defaultdict
from typing import List


class Solution:
    # Bubble Sort
    # Time: O(n^2), Space: O(n)
    def canSortArray(self, nums: List[int]) -> bool:
        # Early return if already sorted
        if nums == sorted(nums):
            return True

        # Calculate bit counts for each number
        bits = defaultdict(int)
        for n in nums:
            b = bin(n).count('1')
            bits[n] = b

        # Keep track of numbers in array
        n = len(nums)

        # Bubble sort with bit count constraint
        for _ in range(n - 1):  # Outer loop for multiple passes
            swapped = False
            for i in range(n - 1):
                f, s = nums[i], nums[i + 1]
                if f > s and bits[f] == bits[s]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True
            # If no swaps occurred in this pass, array is sorted as much as possible
            if not swapped:
                break

        # Check if final array is sorted
        return nums == sorted(nums)
