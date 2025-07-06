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
        """
        Do not return anything, modify matrix in-place instead.
        """
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

    # Similar as above - Using Hash-Set
    # Time: O(m * n), Space: O(m + n)
    def setZeroes2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        row_set, col_set = set(), set()

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    row_set.add(r)
                    col_set.add(c)

        for r in range(rows):
            for c in range(cols):
                if r in row_set or c in col_set:
                    matrix[r][c] = 0


c = Solution()
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
c.setZeroes(matrix)
