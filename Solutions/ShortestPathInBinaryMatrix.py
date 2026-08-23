from collections import deque
from typing import List


# BFS - O(n²) time and space
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Quick rejects: start or end blocked.
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        # BFS guarantees the first time we reach (n-1, n-1) it's via the
        # shortest path, since all edges have equal weight (1 step).
        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        visited = set()
        visited.add((0, 0))

        while queue:
            row, col, length = queue.popleft()

            if row == n - 1 and col == n - 1:
                return length

            for dr, dc in directions:
                r, c = row + dr, col + dc

                if 0 <= r < n and 0 <= c < n and grid[r][c] == 0 and (r, c) not in visited:
                    visited.add((r, c))
                    queue.append((r, c, length + 1))

        return -1


c = Solution()
grid = [[0, 1], [1, 0]]
print(c.shortestPathBinaryMatrix(grid))
