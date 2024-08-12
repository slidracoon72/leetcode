from typing import List


# Similar to Number Of Islands
# We scale up the matrix 3 times to find the regions formed by slashes
# Neetcode: https://www.youtube.com/watch?v=j8KrBYIxHK8
# Time: O(n^2), Space: O(n^2)
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # Original Matrix (n * n)
        row1, col1 = len(grid), len(grid[0])

        # Initialize Up-scaled Matrix 'grid2' (n * n -> 3n * 3n)
        row2, col2 = row1 * 3, col1 * 3
        grid2 = [[0] * col2 for _ in range(row2)]

        # Generate Up-scaled Matrix 'grid2'
        # Slashes are marked as '1' and spaces are by default '0'
        # 1's are blocked(/boundaries/walls) and 0's can be traversed to find connected regions
        for r in range(row1):
            for c in range(col1):
                r2, c2 = r * 3, c * 3
                if grid[r][c] == "/":
                    grid2[r2][c2 + 2] = 1
                    grid2[r2 + 1][c2 + 1] = 1
                    grid2[r2 + 2][c2] = 1
                elif grid[r][c] == "\\":
                    grid2[r2][c2] = 1
                    grid2[r2 + 1][c2 + 1] = 1
                    grid2[r2 + 2][c2 + 2] = 1

        def dfs(r, c, visit):
            # Check boundary conditions, if already visited and if it is a wall/slash/boundary
            if r < 0 or c < 0 or r == row2 or c == col2 or (r, c) in visit or grid2[r][c] != 0:
                return
            visit.add((r, c))

            # Recursively call dfs on neighbours
            neighbours = [[r + 1, c], [r, c + 1], [r - 1, c], [r, c - 1]]
            for nr, nc in neighbours:
                dfs(nr, nc, visit)

        visit = set()
        regions = 0
        for r in range(row2):
            for c in range(col2):
                if grid2[r][c] == 0 and (r, c) not in visit:
                    dfs(r, c, visit)
                    regions += 1

        return regions


c = Solution()
grid = [" /", "/ "]
print(c.regionsBySlashes(grid))
