from typing import List


# Intuition:
# If the count of -ve numbers is even, then all can be made +ve by flipping adjacent values.
# If the count of -ve numbers is odd, at least one will remain -ve. Thus, we subtract the smallest
# absolute number from the total sum twice
class Solution:
    # Time: O(n*n), Space: O(1)
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # Determine the dimensions of the square matrix
        rows = cols = len(matrix)  # The matrix is square, so rows == cols

        # Initialize variables:
        total = 0  # This will hold the total sum of absolute values
        smallest = float('inf')  # Tracks the smallest absolute value in the matrix
        neg_count = 0  # Counts the number of negative numbers in the matrix

        # Iterate over each element in the matrix
        for r in range(rows):
            for c in range(cols):
                # Check if the current element is negative
                if matrix[r][c] < 0:
                    neg_count += 1  # Increment the count of negatives

                # Compute the absolute value of the current element
                cur = abs(matrix[r][c])

                # Add the absolute value to the total sum
                total += cur

                # Update the smallest absolute value if necessary
                smallest = min(smallest, cur)

        # If the count of negative numbers is even, the matrix sum can include all absolute values
        if neg_count % 2 == 0:
            return total
        else:
            # If the count of negatives is odd, subtract twice the smallest absolute value
            # to ensure the sum is maximized (flip one negative to positive)
            return total - (2 * smallest)


c = Solution()
matrix = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]
print(c.maxMatrixSum(matrix))
