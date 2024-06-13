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


c = Solution()
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
c.setZeroes(matrix)
