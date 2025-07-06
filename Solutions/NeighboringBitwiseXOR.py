# Neetcode: https://www.youtube.com/watch?v=d2ntGf2tSDI&ab_channel=NeetCodeIO
# Time: O(n), Space: O(1)
from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        first = 0
        last = 0

        for n in derived:
            if n:
                last = ~last

        return first == last


c = Solution()
derived = [1, 1, 0]
print(c.doesValidArrayExist(derived))
print(c.doesValidArrayExist([1, 1, 0, 1]))
