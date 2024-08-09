from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize the matrix with zeros
        matrix = [[0] * n for _ in range(n)]

        # Define the boundaries of the matrix
        top, bottom = 0, n
        left, right = 0, n

        # Initial value to fill in the matrix
        num = 1

        while left < right and top < bottom:
            # Fill the top row
            for i in range(left, right):
                matrix[top][i] = num
                num += 1
            top += 1

            # Fill the right column
            for i in range(top, bottom):
                matrix[i][right - 1] = num
                num += 1
            right -= 1

            # If only one row/column exists, break
            if not (left < right and top < bottom):
                break

            # Fill the bottom row
            for i in range(right - 1, left - 1, -1):
                matrix[bottom - 1][i] = num
                num += 1
            bottom -= 1

            # Fill the left column
            for i in range(bottom - 1, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

        return matrix


n = 3
c = Solution()
print(c.generateMatrix(n))
