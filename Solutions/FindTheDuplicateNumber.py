from typing import List


# Neetcode: https://www.youtube.com/watch?v=wjYnzkAhcNk&ab_channel=NeetCode
class Solution:
    # Floyd's Tortoise and Hare (Cycle Detection) algorithm
    # Time: O(n), Space: O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        # Initialize slow and fast pointers
        slow, fast = 0, 0

        # Phase 1: Detect the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find the entrance to the cycle
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


c = Solution()
nums = [1, 3, 4, 2, 2]
print(c.findDuplicate(nums))
