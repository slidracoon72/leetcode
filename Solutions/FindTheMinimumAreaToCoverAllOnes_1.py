from typing import List


class Solution:
    # Time: O(m*n), Space: O(1)
    def minimumArea(self, grid: List[List[int]]) -> int:
        # Get the dimensions of the grid
        n, m = len(grid), len(grid[0])

        # Initialize boundaries:
        # top/left start at max possible (n, m) so they shrink down
        # bottom/right start at 0 so they expand upward
        top, left = n, m
        bottom, right = 0, 0

        # Traverse through every cell in the grid
        for r in range(n):
            for c in range(m):
                # If the cell contains a '1', update the rectangle boundaries
                if grid[r][c]:
                    top = min(top, r)  # update topmost row
                    left = min(left, c)  # update leftmost column
                    bottom = max(bottom, r)  # update bottommost row
                    right = max(right, c)  # update rightmost column

        # Compute the area of the rectangle enclosing all '1's
        return (bottom - top + 1) * (right - left + 1)


c = Solution()
grid = [[0, 1, 0], [1, 0, 1]]
print(c.minimumArea(grid))