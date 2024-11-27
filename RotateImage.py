from typing import List


# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.
class Solution:
    def rotate(self, matrix: List[List[int]]) -> List[List[int]]:

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

    def rotate1(self, matrix: List[List[int]]) -> List[List[int]]:
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

        return matrix

    # Done using zip(). It is not an inplace method since zip creates new tuples
    def rotate2(self, matrix: List[List[int]]) -> List[List[int]]:
        # Step 1: Transpose using zip
        # *matrix -> unpacks the matrix (each row becomes exposed)
        # zip -> groups elements in the same index in each exposed row as a tuple
        transpose = zip(*matrix)

        # Step 2: Reverse rows to achieve clockwise rotation
        rotated = [list(row)[::-1] for row in transpose]

        return rotated

    def rotate3(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])

        res = []  # Initialize the result matrix (rotated)
        for c in range(cols):  # Iterate over columns in the original box
            col = []  # Collect elements for the new row in the rotated matrix
            for r in reversed(range(rows)):  # Iterate from bottom to top in the current column
                col.append(matrix[r][c])  # Add the element to the new row
            res.append(col)  # Append the new row to the result matrix

        return res  # Return the rotated box


c = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(c.rotate(matrix))
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(c.rotate1(matrix))
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(c.rotate2(matrix))
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(c.rotate3(matrix))


