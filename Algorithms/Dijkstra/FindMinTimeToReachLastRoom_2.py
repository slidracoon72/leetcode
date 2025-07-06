import heapq
from typing import List


class Solution:
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
