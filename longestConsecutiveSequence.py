from typing import List


# Neetcode: https://www.youtube.com/watch?v=P6RZZMu_maU
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


c = Solution()
nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
print(c.longestConsecutive(nums))
