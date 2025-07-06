from typing import List


# Greedy Approach
# Time: O(m*n), Space: O(1)
# Neetcode: https://www.youtube.com/watch?v=Ks6fGnXkHPg
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # Number of rows and columns
        rows, cols = len(rowSum), len(colSum)

        # Initialize a matrix filled with zeros
        matrix = [[0] * cols for _ in range(rows)]

        # Distribute the row sums into the first column of the matrix
        for r in range(rows):
            matrix[r][0] = rowSum[r]

        # Adjust the matrix to satisfy the column sums
        for c in range(cols):
            # Calculate the current sum of the column 'c'
            cur_col_sum = 0
            for r in range(rows):
                cur_col_sum += matrix[r][c]

            # Adjust the values in the column if the sum exceeds colSum[c]
            r = 0
            while cur_col_sum > colSum[c]:
                # Calculate the difference that needs to be adjusted
                diff = cur_col_sum - colSum[c]

                # Determine the amount to shift to the next column
                right_shift = min(diff, matrix[r][c])

                # Adjust the current column and the next column
                matrix[r][c] -= right_shift
                if c + 1 < cols:
                    matrix[r][c + 1] += right_shift

                # Update the current column sum
                cur_col_sum -= right_shift

                # Move to the next row
                r += 1

        return matrix


c = Solution()
rowSum = [5, 7, 10]
colSum = [8, 6, 8]
print(c.restoreMatrix(rowSum, colSum))
