from typing import List


class Solution:
    # Brute Force - Gives TLE
    # Time: O(n^2)
    def maxWidthRamp(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if i < j and nums[i] <= nums[j]:
                    res = max(res, j - i)

        return res

    # Using Decreasing Stack
    # Time: O(n)
    def maxWidthRamp1(self, nums: List[int]) -> int:
        stack = []
        # Step 1: Create a decreasing stack
        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
                # Store indices of decreasing elements in the stack
                stack.append(i)

        res = 0
        # Step 2: Traverse the array backwards to find the max width ramp
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                # Calculate the width (j - i)
                res = max(res, j - stack.pop())

        return res
