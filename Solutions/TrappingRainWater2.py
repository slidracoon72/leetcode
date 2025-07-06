# LC - Hard

import heapq
from typing import List


class Solution:
    # Neetcode: https://www.youtube.com/watch?v=onA7_MaPGkM&t=521s&ab_channel=NeetCodeIO
    # Time: O(m*n * log(m*n))
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows, cols = len(heightMap), len(heightMap[0])

        # Step 1: Start from border cells.
        # Add all border cells to min-heap and mark as visited
        minHeap = []
        for r in range(rows):
            for c in range(cols):
                if r in [0, rows - 1] or c in [0, cols - 1]:
                    heapq.heappush(minHeap, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1  # mark visited

        # Step 2: Multi-source BFS
        # Prioritize smallest heights
        # Maintain max height to calculate water stored in each inner position
        res = 0
        max_h = -1

        while minHeap:
            h, r, c = heapq.heappop(minHeap)
            max_h = max(max_h, h)
            res += max_h - h

            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for nr, nc in neighbors:
                if nr < 0 or nc < 0 or nr == rows or nc == cols or heightMap[nr][nc] == -1:
                    continue

                heapq.heappush(minHeap, (heightMap[nr][nc], nr, nc))
                heightMap[nr][nc] = -1

        return res
