import heapq
import math
from typing import List


class Solution:
    # Solved using Max-Heap
    # Time: O(nlogk), Space: O(k)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []  # max_distance, coords
        for x, y in points:
            d = math.sqrt((x ** 2) + (y ** 2))
            heapq.heappush(heap, (-d, x, y))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        while heap:
            _, x, y = heapq.heappop(heap)
            res.append([x, y])
        return res


c = Solution()
points = [[3, 3], [5, -1], [-2, 4]]
k = 2
print(c.kClosest(points, k))
