from typing import List


class Solution:
    # https://www.youtube.com/watch?v=_WIFehFkkig
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0

        points.sort()
        prev = points[0]
        total = 1

        for s, e in points[1:]:
            # if not overlapping
            if s > prev[1]:
                total += 1
                prev = [s, e]
            # if overlapping
            else:
                prev[1] = min(prev[1], e)

        return total


c = Solution()
points = [[10, 16], [2, 8], [1, 6], [7, 12]]
print(c.findMinArrowShots(points))
