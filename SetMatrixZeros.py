from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])

        pos = []

        # find all zeros
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    pos.append((i, j))

        # change it
        for i, j in pos:
            for x in range(c):
                matrix[i][x] = 0
            for y in range(r):
                matrix[y][j] = 0

        print(matrix)

    # Using Iteration
    # Time: O(m * n), Space: O(m + n)
    def setZeroes1(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rows, cols = [False] * ROWS, [False] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True

        for r in range(ROWS):
            for c in range(COLS):
                if rows[r] or cols[c]:
                    matrix[r][c] = 0


c = Solution()
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
c.setZeroes(matrix)
