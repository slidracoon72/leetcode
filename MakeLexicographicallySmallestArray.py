# LC - 2948: Make Lexicographically Smallest Array by Swapping Elements
from collections import deque
from typing import List


class Solution:
    # Time complexity: O(nlogn) - due to sorting of the array.
    # Space complexity: O(n) - for storing groups and mapping numbers to their groups.
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # `groups` will store groups of numbers where each group's elements differ by at most `limit`.
        # Each group is maintained as a deque for efficient removal of elements from the front.
        groups = []

        # `num_to_group` maps each number in `nums` to its respective group index in `groups`.
        num_to_group = {}

        # Step 1: Sort the array and group elements based on the `limit` condition.
        for n in sorted(nums):
            # If `groups` is empty or the difference between the current number `n` and
            # the last number in the last group exceeds `limit`, create a new group.
            if not groups or abs(n - groups[-1][-1]) > limit:
                groups.append(deque())
            # Add the current number to the last group.
            groups[-1].append(n)
            # Record the group index for the current number.
            num_to_group[n] = len(groups) - 1

        # Step 2: Reconstruct the result array.
        res = []
        for n in nums:
            # Get the group index for the current number.
            j = num_to_group[n]
            # Append the first (also the smallest) element from the corresponding group to the result.
            res.append(groups[j].popleft())
        return res


c = Solution()
nums = [1, 7, 6, 18, 2, 1]
limit = 2
# print(nums)
# print(sorted(nums))
print(c.lexicographicallySmallestArray(nums, limit))
