from typing import List


# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (anti-clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.

# In-Place Anticlockwise Rotation
class Solution:
    def rotate_anticlockwise(self, matrix: List[List[int]]):
        """
        Rotate the matrix in-place by 90 degrees anticlockwise.
        """
        # Step 1: Transpose the matrix (swap rows with columns)
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each column (in-place)
        for j in range(n):
            for i in range(n // 2):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]

        return matrix


c = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(c.rotate_anticlockwise(matrix))
