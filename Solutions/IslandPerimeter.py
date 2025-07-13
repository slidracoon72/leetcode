from typing import List


class Solution:
    # Time: O(m*n), Space: O(1)
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    res += 4
                    if r > 0 and grid[r - 1][c]:
                        res -= 2
                    if c > 0 and grid[r][c - 1]:
                        res -= 2
        return res


c = Solution()
grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(c.islandPerimeter(grid))
