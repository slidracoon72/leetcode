from collections import defaultdict
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # Step 1: Handle edge case
        if not nums or not nums[0]:
            return []

        # Step 2: Group elements by diagonal sum (r + c)
        diagonals = defaultdict(list)
        for r in range(len(nums)):
            for c in range(len(nums[r])):  # Each row has different length
                diagonals[r + c].append((r, c))

        # Step 3: Process diagonals in order of increasing sum
        result = []
        max_sum = max(diagonals.keys())  # Maximum diagonal sum
        for s in range(max_sum + 1):
            # Sort by col index (increasing c)
            # bottom-left to top-right
            for r, c in sorted(diagonals[s], key=lambda x: x[1]):
                result.append(nums[r][c])

        return result
