from typing import List, Any


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        # Create a new matrix with dimensions [cols][rows]
        transposed = [[0] * rows for _ in range(cols)]

        # Fill the transposed matrix
        for r in range(rows):
            for c in range(cols):
                transposed[c][r] = matrix[r][c]

        return transposed

    def transpose1(self, matrix: List[List[int]]) -> list[tuple[Any]]:
        return list(zip(*matrix))


c = Solution()
matrix = [[1, 2, 3], [4, 5, 6]]
print(c.transpose(matrix))
print(c.transpose1(matrix))
