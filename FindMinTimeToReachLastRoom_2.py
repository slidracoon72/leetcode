import heapq
from typing import List


class Solution:
    # Time: O(rows * cols * log(rows * cols))
    # Space: O(rows * cols)
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows, cols = len(moveTime), len(moveTime[0])
        target = (rows - 1, cols - 1)

        minHeap = [[0, 0, 0, 1]]  # time, row, col, move
        visit = {(0, 0)}

        while minHeap:
            time, row, col, move = heapq.heappop(minHeap)
            if (row, col) == target:
                return time

            neighbors = [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]
            for nr, nc in neighbors:
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visit:
                    next_time = max(time, moveTime[nr][nc]) + move
                    next_move = 2 if move == 1 else 1

                    heapq.heappush(minHeap, (next_time, nr, nc, next_move))
                    visit.add((nr, nc))

        return -1

    # Similar as above - Solved as part of LC Daily Problem (May 7, 2025)
    # Time: O(rows * cols * log(rows * cols))
    # Space: O(rows * cols)
    def minTimeToReach1(self, moveTime: List[List[int]]) -> int:
        rows, cols = len(moveTime), len(moveTime[0])
        target = (rows - 1, cols - 1)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minHeap = [(0, 0, 0, 1)]  # (time, row, col, move)
        visit = set()

        while minHeap:
            time, row, col, move = heapq.heappop(minHeap)

            if (row, col) == target:
                return time

            if (row, col) in visit:
                continue
            visit.add((row, col))

            for dr, dc in directions:
                nei_r, nei_c = row + dr, col + dc

                if 0 <= nei_r < rows and 0 <= nei_c < cols and (nei_r, nei_c) not in visit:
                    nei_time = max(moveTime[nei_r][nei_c], time) + move
                    nei_move = 2 if move == 1 else 1
                    heapq.heappush(minHeap, (nei_time, nei_r, nei_c, nei_move))
