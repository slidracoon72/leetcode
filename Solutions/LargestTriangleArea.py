# DO AGAIN
from itertools import combinations


class Solution:
    def largestTriangleArea(self, points):
        def area(p1, p2, p3):
            # Shoelace formula for triangle area
            return abs(
                p1[0] * (p2[1] - p3[1]) +
                p2[0] * (p3[1] - p1[1]) +
                p3[0] * (p1[1] - p2[1])
            ) / 2

        max_area = 0.0
        for p1, p2, p3 in combinations(points, 3):
            max_area = max(max_area, area(p1, p2, p3))
        return max_area
