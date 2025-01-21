from typing import List


# Time: O(m*n), Space: O(m*n)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        rows, cols = len(grid), len(grid[0])
        # Set to keep track of visited cells
        visit = set()

        def dfs(r, c):
            # Check if the current cell is out of bounds or already visited or is water (0)
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or (r, c) in visit:
                return 0  # If so, return 0 (base case: no area to add)

            # Mark the current cell as visited
            visit.add((r, c))
            # Return the size of the island starting from this cell
            # The size is calculated by counting the current cell (1) plus the size of the island
            # found by exploring all the four directions (right, down, left, up) recursively
            return 1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)

        area = 0  # Initialize the maximum area of an island
        # Traverse each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # Update the maximum area of the island
                area = max(area, dfs(r, c))

        return area  # Return the maximum area of the island found
