# LC - Hard

import heapq
from collections import deque
from typing import List


# Reach from top-left to bottom-right of the grid with minimum obstacles
class Solution:
    # Solved using Dijkstra's Algorithm
    # Time: O(m*n * log(m*n))
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        minHeap = [(0, 0, 0)]  # (obstacles, row, col)
        visit = {(0, 0)}  # start from top-left

        while minHeap:
            obstacles, row, col = heapq.heappop(minHeap)

            if (row, col) == (rows - 1, cols - 1):
                return obstacles

            nei = [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]
            for nr, nc in nei:
                if nr < 0 or nr == rows or nc < 0 or nc == cols or (nr, nc) in visit:
                    continue

                heapq.heappush(minHeap, (obstacles + grid[nr][nc], nr, nc))
                visit.add((nr, nc))

    # Solved using Deque - BFS
    # We keep the deque monotonically increasing
    # Neetcode: https://www.youtube.com/watch?v=VxeH7_QL-28&ab_channel=NeetCodeIO
    # Time: O(m*n)
    def minimumObstacles1(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        q = deque([(0, 0, 0)])  # obstacles, row, col
        visit = {(0, 0)}  # row, col

        while q:
            obstacles, row, col = q.popleft()

            if (row, col) == (rows - 1, cols - 1):
                return obstacles

            nei = [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]
            for nr, nc in nei:
                if nr < 0 or nr == rows or nc < 0 or nc == cols or (nr, nc) in visit:
                    continue

                if grid[nr][nc]:
                    # add to right (end) of deque as more obstacles
                    q.append((obstacles + 1, nr, nc))
                else:
                    # add to the left (start) of deque as less obstacles
                    q.appendleft((obstacles, nr, nc))

                visit.add((nr, nc))
