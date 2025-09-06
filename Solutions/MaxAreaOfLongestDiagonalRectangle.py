import math
from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diagonal, area = 0, 0

        for l, w in dimensions:
            d = math.sqrt(l * l + w * w)
            a = l * w
            if d > diagonal:
                area = a
                diagonal = d
            elif d == diagonal:
                area = max(area, a)

        return area


c = Solution()
dimensions = [[9, 3], [8, 6]]
print(c.areaOfMaxDiagonal(dimensions))
