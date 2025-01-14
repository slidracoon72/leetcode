from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n + 1):
            if i not in nums:
                return i

    # Using bit manipulation - XOR
    # XOR cancels out two same numbers
    # Time: O(n), Space: O(1)
    def missingNumber1(self, nums: List[int]) -> int:
        # Initialize result as 0. This will store the missing number at the end.
        res = 0

        # Step 1: XOR all the numbers in the given array
        for n in nums:
            res ^= n  # XOR each number with res

        # Step 2: XOR all numbers from 0 to len(nums) (inclusive)
        # This includes all numbers that should be in the array
        for i in range(len(nums) + 1):
            res ^= i  # XOR each index with res

        # After both loops, all numbers that appear in nums will cancel out with the corresponding
        # numbers from the range 0 to len(nums), except for the missing number.
        return res


c = Solution()
a1 = [3, 0, 1]
a2 = [0, 1]
a3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(c.missingNumber(a1))
print(c.missingNumber(a2))
print(c.missingNumber(a3))
