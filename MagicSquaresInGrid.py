from typing import List


# Neetcode: https://www.youtube.com/watch?v=FV52wWrivNc
# Time: O(m*n), Space: O(1)
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0

        # Helper function to determine whether a 3*3 grid starting from (r,c) is a magic square or not
        def magic(r, c) -> int:
            # 1. Ensure 1 - 9
            values = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    # if value not distinct (already in set) or not from 1 to 9: not a magic square
                    if grid[i][j] in values or not (1 <= grid[i][j] <= 9):
                        return 0
                    values.add(grid[i][j])

            # 2. Rows (all rows to have same sum = 15)
            for i in range(r, r + 3):
                if sum(grid[i][c:c + 3]) != 15:
                    return 0

            # 3. Cols (all cols to have same sum = 15)
            for i in range(c, c + 3):
                if grid[r][i] + grid[r + 1][i] + grid[r + 2][i] != 15:
                    return 0

            # 4. Diagonals (all diagonals to have same sum = 15)
            if (
                    grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15 or
                    grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != 15
            ):
                return 0

            # If all conditions satisfied, it is a magic square starting from (r,c)
            return 1

        # Loop through the matrix from where a 3*3 grid is possible
        for r in range(rows - 2):
            for c in range(cols - 2):
                res += magic(r, c)

        return res


c = Solution()
grid = [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]
print(c.numMagicSquaresInside(grid))
