from collections import defaultdict
from typing import List


class Solution:
    # Brute Force
    # Time: O(m*n*min(m,n)^2 ~ O(n^4) for a square matrix, Space: O(1)
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = 0
        grid = min(rows, cols)

        for d in range(1, grid + 1):  # Size of the square
            for r in range(rows - d + 1):
                for c in range(cols - d + 1):
                    # Check if all cells in the d x d square are 1
                    valid_square = True
                    for i in range(d):
                        for j in range(d):
                            if matrix[r + i][c + j] == 0:
                                valid_square = False
                                break
                        if not valid_square:
                            break
                    if valid_square:
                        res += 1

        return res

    # Using Dynamic Programming - Top-Down Approach
    # Time: O(m*n), Space:O(m*n)
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        cache = {}  # Dictionary to memoize results for each cell to avoid redundant calculations

        # Recursive function to find the size of the largest square from (r, c)
        def dfs(r, c):
            # Base case: out of bounds or cell is 0, can't form a square
            if r == rows or c == cols or matrix[r][c] == 0:
                return 0
            # Return cached result if already computed for (r, c)
            if (r, c) in cache:
                return cache[(r, c)]

            # Recursively find the size of the square based on neighboring cells (right, down, and diagonal)
            cache[(r, c)] = 1 + min(
                dfs(r + 1, c),  # check below
                dfs(r, c + 1),  # check right
                dfs(r + 1, c + 1)  # check diagonal
            )

            return cache[(r, c)]  # Return computed square size

        res = 0  # Initialize result to accumulate all square counts
        # Iterate over all cells as potential bottom-right corners of squares
        for r in range(rows):
            for c in range(cols):
                res += dfs(r, c)  # Add the size of the square at each cell to the result
        return res  # Return the total number of squares

    # Using Dynamic Programming - Bottom-Up Approach
    # Time: O(m*n), Space:O(m*n)
    def countSquares2(self, matrix: List[List[int]]) -> int:
        # Determine matrix dimensions
        rows, cols = len(matrix), len(matrix[0])

        # Dictionary to store the maximum square side ending at each cell
        dp = defaultdict(int)

        res = 0  # Initialize the count of squares
        for r in range(rows):
            for c in range(cols):
                # Only proceed if the cell has a 1
                if matrix[r][c]:
                    # Calculate the size of the largest square ending at (r, c)
                    dp[(r, c)] = 1 + min(
                        dp[(r - 1, c)],  # square size above
                        dp[(r, c - 1)],  # square size to the left
                        dp[(r - 1, c - 1)]  # square size diagonally above-left
                    )
                    # Add the square count ending at (r, c) to the result
                    res += dp[(r, c)]

        return res  # Return the total count of squares in the matrix
