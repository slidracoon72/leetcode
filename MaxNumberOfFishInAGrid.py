from collections import deque
from typing import List

# Time: O(rows * cols), Space: O(rows * cols)
class Solution:
    # Solved using BFS
    # Similar to NumberOfIslands.py
    def findMaxFish(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()

        def bfs(row, col):
            q = deque([(row, col)])
            visit.add((row, col))

            fish = 0
            while q:
                r, c = q.popleft()
                fish += grid[r][c]

                neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
                for nr, nc in neighbors:
                    if nr < 0 or nr == rows or nc < 0 or nc == cols or grid[nr][nc] == 0 or (nr, nc) in visit:
                        continue

                    q.append((nr, nc))
                    visit.add((nr, nc))

            return fish

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0 and (r, c) not in visit:
                    res = max(res, bfs(r, c))

        return res

    # Solved using DFS
    # Similar to MaxAreaOfIsland.py
    def findMaxFish1(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or (r, c) in visit:
                return 0

            visit.add((r, c))

            return grid[r][c] + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0 and (r, c) not in visit:
                    res = max(res, dfs(r, c))

        return res


c = Solution()
grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
print(c.findMaxFish(grid))
