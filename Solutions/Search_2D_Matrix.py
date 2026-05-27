from typing import List


class Solution:
    # Time: O(log m + log n), Space: O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Determine the number of rows and columns
        rows, cols = len(matrix), len(matrix[0])

        if rows == 0:
            return False
        if cols == 0:
            return False

        # Early exit if the target is out of the matrix's bounds
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        # Use binary search to find the row where the target could be
        l, r = 0, rows - 1
        while l <= r:
            mid = l + (r - l) // 2
            row = matrix[mid]
            if row[0] <= target <= row[-1]:
                # Apply binary search within the row
                left, right = 0, len(row) - 1
                while left <= right:
                    mid_row = left + (right - left) // 2
                    if row[mid_row] == target:
                        return True
                    elif row[mid_row] < target:
                        left = mid_row + 1
                    else:
                        right = mid_row - 1
                return False  # Target not found in the row
            elif target < row[0]:
                r = mid - 1
            else:
                l = mid + 1

        return False  # Target not found in any row


c = Solution()
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 60
print(c.searchMatrix(matrix, target))
