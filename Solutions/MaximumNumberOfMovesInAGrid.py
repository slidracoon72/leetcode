import collections
from typing import List


class Solution:
    # Similar to Number of Islands
    # Time: O(m*n), Space: O(m*n)
    def maxMoves(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c, 0))
            visit = set()
            visit.add((r, c))
            max_steps = 0

            while q:
                row, col, steps = q.popleft()
                max_steps = max(max_steps, steps)

                directions = [(row - 1, col + 1), (row, col + 1), (row + 1, col + 1)]
                for dr, dc in directions:
                    if (0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] > grid[row][col] and (
                            dr, dc) not in visit):
                        q.append((dr, dc, steps + 1))
                        visit.add((dr, dc))

            return max_steps

        res = 0
        for i in range(rows):
            res = max(res, bfs(i, 0))

        return res
