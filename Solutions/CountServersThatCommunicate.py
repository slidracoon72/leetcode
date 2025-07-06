from typing import List


class Solution:
    # Time: O(m * n), Space: O(m + n)
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = [0] * m
        cols = [0] * n

        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    rows[r] += 1
                    cols[c] += 1

        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] and (rows[r] > 1 or cols[c] > 1):
                    res += 1

        return res


c = Solution()
grid = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
print(c.countServers(grid))
