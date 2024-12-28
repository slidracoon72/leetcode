import collections
from typing import List


# Graph question
# Solving using BFS (iterative)
# Neetcode: https://www.youtube.com/watch?v=pV2kpPD66nE
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check if grid is empty
        if not grid:
            return 0

        # Get dimensions of grid
        rows, cols = len(grid), len(grid[0])
        # Set to keep track of visited land
        visit = set()
        islands = 0

        # Define function for BFS on adjacent values
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))

            while q:
                row, col = q.popleft()
                # Define directions to move in grid
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    # Calculate new coordinates
                    new_r, new_c = row + dr, col + dc
                    # Check if new coordinates are within grid bounds and if it's land
                    if (new_r in range(rows) and
                            new_c in range(cols) and
                            grid[new_r][new_c] == '1' and
                            (new_r, new_c) not in visit):
                        # Add new coordinates to queue and mark as visited
                        q.append((new_r, new_c))
                        visit.add((new_r, new_c))

        # # Define function for DFS on adjacent values
        # def dfs(r, c, visit):
        #     # Check boundary conditions, if already visited and if it is not land
        #     if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visit or grid[r][c] == 0:
        #         return
        #     visit.add((r, c))
        #     # Recursively call dfs on neighbours
        #     neighbours = [[r + 1, c], [r, c + 1], [r - 1, c], [r, c - 1]]
        #     for nr, nc in neighbours:
        #         dfs(nr, nc, visit)

        # Iterate over each cell in grid
        for r in range(rows):
            for c in range(cols):
                # If cell is land and not visited, start BFS from this cell
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        # Return number of islands
        return islands


c = Solution()
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(c.numIslands(grid))
