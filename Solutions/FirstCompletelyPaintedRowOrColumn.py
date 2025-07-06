from typing import List


class Solution:
    # Time: O(n), Space: O(m*n)
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        position = {}

        # Map each value in mat to its position (row, col)
        for r in range(rows):
            for c in range(cols):
                cur = mat[r][c]
                position[cur] = (r, c)

        # Create arrays to track the painted cell counts in rows and columns
        row_count = [0] * rows
        col_count = [0] * cols

        # Iterate over the elements in arr
        for i in range(len(arr)):
            paint_row, paint_col = position[arr[i]]

            # Increment the painted cell counts
            row_count[paint_row] += 1
            col_count[paint_col] += 1

            # Check if a row or column is completely painted
            if row_count[paint_row] == cols or col_count[paint_col] == rows:
                return i

        # If no row or column is fully painted (shouldn't happen with valid input)
        return -1


c = Solution()
arr = [2, 8, 7, 4, 1, 3, 5, 6, 9]
mat = [[3, 2, 5], [1, 4, 6], [8, 7, 9]]
print(c.firstCompleteIndex(arr, mat))
