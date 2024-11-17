import math
from typing import List


# Neetcode: https://www.youtube.com/watch?v=U2SozAs9RzA
# Solved using Binary Search
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)  # setting range of k values [1....11]
        res = r  # initialize res to max value i.e, r
        while l <= r:  # start binary search
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res


c = Solution()
piles = [3, 6, 7, 11]
h = 8
# # piles = [30, 11, 23, 4, 20]
# # h = 5
# piles = [30, 11, 23, 4, 20]
# h = 6
print(c.minEatingSpeed(piles, h))
