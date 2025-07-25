from typing import List


class Solution:
    # Time: O(n), Space: O(n)
    def maxSum(self, nums: List[int]) -> int:
        # Create a set of all positive unique numbers from the list.
        # Sets automatically eliminate duplicates.
        positive = set([n for n in nums if n > 0])

        # If there are any positive numbers, return the sum of the unique ones.
        # Otherwise, all numbers are non-positive — return the maximum among them (could be negative or zero).
        return sum(positive) if len(positive) > 0 else max(nums)


c = Solution()
nums = [1, 2, -1, -2, 1, 0, -1]
print(c.maxSum(nums))
