from typing import List


class Solution:
    # Time: O(n), Space: O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        o = len(nums)
        f = len(set(nums))
        if o > f:
            return True
        else:
            return False

    def hasDuplicate1(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)


c = Solution()
a1 = [1, 2, 3, 1]
a2 = [1, 2, 3, 4]
a3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(c.containsDuplicate(a1))
print(c.containsDuplicate(a2))
print(c.containsDuplicate(a3))
