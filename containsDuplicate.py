from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        o = len(nums)
        f = len(set(nums))
        if o > f:
            return True
        else:
            return False


c = Solution()
a1 = [1, 2, 3, 1]
a2 = [1, 2, 3, 4]
a3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(c.containsDuplicate(a1))
print(c.containsDuplicate(a2))
print(c.containsDuplicate(a3))
