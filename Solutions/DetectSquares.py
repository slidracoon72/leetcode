from collections import defaultdict
from typing import List


# Space: O(n)
class DetectSquares:
    def __init__(self):
        # Dictionary to store the count of each point in the form (x, y)
        self.pts_count = defaultdict(int)
        # List to store all the points added
        self.points = []

    # Time:O(1)
    def add(self, point: List[int]) -> None:
        # Convert the list point to a tuple (as keys in dict cannot be lists)
        self.pts_count[tuple(point)] += 1
        # Append the point to the list of points
        self.points.append(point)

    # Time:O(n)
    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        # Iterate over all previously added points
        for x, y in self.points:
            # Check if the current point forms a diagonal with the given point and square has a positive area
            # two points form a diagonal if the absolute difference of their heights is equal to
            # the absolute difference of their widths
            if abs(px - x) != abs(py - y) or x == px or y == py:
                continue
            # Check the counts of the potential diagonal points
            res += self.pts_count[(x, py)] * self.pts_count[(px, y)]
        return res

# Example usage:
# obj = DetectSquares()
# obj.add([1, 1])
# obj.add([2, 2])
# obj.add([1, 2])
# obj.add([2, 1])
# param_2 = obj.count([2, 2])  # Should return the number of squares with (2, 2) as one of the vertices
