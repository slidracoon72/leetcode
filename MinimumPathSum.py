from typing import List


# Dynamic Programming: Bottom-Up
# Time: O(m*n), Space: O(m*n)
# Neetcode: https://www.youtube.com/watch?v=pGMsrvt0fpk&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=35&pp=iAQB
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # Initialize a matrix of size: (rows + 1) * (cols + 1). The extra row and col is to handle edge cases for
        # finding the minimum of the value to the right or bottom position of the current value of given matrix.
        matrix = [[float('inf')] * (cols + 1) for _ in range(rows + 1)]
        # To handle initial min value, make the value below 0 so that we always get 0 as min value
        matrix[rows][cols - 1] = 0

        # Since we follow a Botttom-Up DP approach, travesre the matrix from the last [row+1][col+1] value and
        # build the solution to the first value [0][0] of the matrix
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                matrix[r][c] = grid[r][c] + min(matrix[r + 1][c], matrix[r][c + 1])

        return matrix[0][0]
