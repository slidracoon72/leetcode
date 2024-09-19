from functools import cmp_to_key
from typing import List


# Neetcode: https://www.youtube.com/watch?v=WDx6Y4i4xJ8
# Time Complexity: O(nlogn) - due to sorting the list.
# Space Complexity: O(n) - storing the string representation of the numbers and the sorted list.

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert each integer in the nums list to a string
        # This is necessary because we will concatenate the numbers to compare them
        for i, n in enumerate(nums):
            nums[i] = str(n)

        # Custom comparator function to define sorting order
        def compare(n1, n2) -> int:
            # Compare the two numbers based on their concatenated result in both possible orders
            # If concatenating n1 + n2 produces a larger number than n2 + n1,
            # n1 should come before n2 in the sorted order, hence return -1
            if n1 + n2 > n2 + n1:
                return -1
            # If n1 + n2 is smaller, return 1 so n2 comes before n1 in the sorted order
            else:
                return 1

        # Sort the list based on the custom compare function
        res = sorted(nums, key=cmp_to_key(compare))

        # Join the sorted numbers to form the largest number
        # str(int(...)) is used to handle edge cases like [0, 0, 0], which should return "0" instead of "000"
        return str(int("".join(res)))


c = Solution()
nums = [3, 30, 34, 5, 9]
print(c.largestNumber(nums))
