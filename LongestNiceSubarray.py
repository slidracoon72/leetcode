from typing import List


class Solution:
    # Solved using Sliding Window
    # Neetcode: https://www.youtube.com/watch?v=pcUmxsvTmP0&ab_channel=NeetCodeIO
    # Time: O(n), Space: O(1)
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 0
        cur = 0  # bitmask
        l = 0  # left pointer

        for r in range(len(nums)):
            while cur & nums[r]:  # if pair is non-zero
                cur = cur ^ nums[l]  # undo / remove leftmost element from bitmask by XORing
                l += 1  # Move the left pointer forward
            res = max(res, r - l + 1)  # track longest subarray
            cur |= nums[r]  # add(OR) current element to mask

        return res


c = Solution()
nums = [1, 3, 8, 48, 10]
print(c.longestNiceSubarray(nums))
