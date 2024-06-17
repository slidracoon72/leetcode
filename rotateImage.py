from typing import List


class Solution:
    def rotate(self, matrix):

        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save the topLeft
                topLeft = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft
            l += 1
            r -= 1

        return matrix

    def rotate1(self, matrix: List[List[int]]) -> None:
        """
        Rotates the given n x n 2D matrix representing an image by 90 degrees clockwise.
        The rotation is done in-place, meaning the input matrix is modified directly.
        """
        n = len(matrix)  # Get the size of the matrix (n x n)

        # Step 1: Transpose the matrix
        # Transposing involves swapping matrix[i][j] with matrix[j][i] for all i < j
        for i in range(n):
            for j in range(i + 1, n):
                # Swap elements across the diagonal
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reflect the matrix horizontally
        # Reflecting involves swapping elements in each row horizontally
        for i in range(n):
            for j in range(n // 2):
                # Swap elements across the middle vertical line
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]


c = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(c.rotate(matrix))
