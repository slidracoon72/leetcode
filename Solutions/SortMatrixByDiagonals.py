from typing import List


class Solution:
    # Simulation Problem
    # Time: O(n^2 * logn), Space: O(n^2)
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        # Edge case: if the matrix has only 1 row or 1 column,
        # no sorting is needed
        if n <= 1:
            return grid

        # -------------------------------
        # Step 1: Sort diagonals in the bottom-left triangle
        # (including the main diagonal).
        # These diagonals are sorted in **descending order**.
        # -------------------------------

        r, c = 0, 0  # start from first column, moving down row by row
        for _ in range(n):
            temp = []
            i, j = r, c

            # Collect all elements along the diagonal
            while i < n and j < n:
                temp.append(grid[i][j])
                i += 1
                j += 1

            # Sort the diagonal in descending order
            temp.sort(reverse=True)

            # Put sorted values back into the matrix
            i, j = r, c
            x = 0
            while i < n and j < n:
                grid[i][j] = temp[x]
                x += 1
                i += 1
                j += 1

            # Move to the next diagonal (downward in first column)
            r += 1
            c = 0

        # -------------------------------
        # Step 2: Sort diagonals in the top-right triangle
        # (excluding the main diagonal).
        # These diagonals are sorted in **ascending order**.
        # -------------------------------

        r, c = 0, 1  # start from second column of first row
        for _ in range(n - 1):
            temp = []
            i, j = r, c

            # Collect all elements along the diagonal
            while i < n and j < n:
                temp.append(grid[i][j])
                i += 1
                j += 1

            # Sort the diagonal in ascending order
            temp.sort()

            # Put sorted values back into the matrix
            i, j = r, c
            x = 0
            while i < n and j < n:
                grid[i][j] = temp[x]
                x += 1
                i += 1
                j += 1

            # Move to the next diagonal (rightward in first row)
            r = 0
            c += 1

        # Return the modified grid with diagonals sorted
        return grid


c = Solution()
grid = [[1, 7, 3], [9, 8, 2], [4, 5, 6]]
print(c.sortMatrix(grid))
