from typing import List


class Solution:
    # Two - Pointers
    # Time: O(n), Space: O(1)
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l


c = Solution()
a = [0, 1, 5, 5, 5, 5, 6, 7, 7, 7, 9]
print(c.removeDuplicates(a))
