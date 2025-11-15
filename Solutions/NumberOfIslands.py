import collections
from typing import List


# Graph question
class Solution:
    # Solved using BFS (iterative)
    # Neetcode: https://www.youtube.com/watch?v=pV2kpPD66nE
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check if grid is empty
        if not grid:
            return 0

        # Get dimensions of grid
        rows, cols = len(grid), len(grid[0])
        # Set to keep track of visited land
        visit = set()
        # Define directions to move in grid
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Define function for BFS on adjacent values
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))

            while q:
                row, col = q.popleft()
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

        islands = 0
        # Iterate over each cell in grid
        for r in range(rows):
            for c in range(cols):
                # If cell is land and not visited, start BFS from this cell
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        # Return number of islands
        return islands

    # Solved Using DFS
    def numIslands1(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visit or grid[r][c] == "0":
                return

            visit.add((r, c))
            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc
                dfs(new_row, new_col)

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    dfs(r, c)
                    islands += 1
        return islands


c = Solution()
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(c.numIslands(grid))

grid = [
    ['0', '1', '0', '0', '1', '0', '1'],
    ['1', '1', '0', '0', '0', '0', '0'],
    ['0', '0', '1', '1', '0', '1', '0'],
    ['0', '0', '0', '1', '0', '1', '0'],
    ['1', '0', '0', '0', '1', '0', '0'],
    ['1', '1', '0', '0', '0', '0', '1'],
    ['0', '0', '0', '1', '0', '0', '1']
]
print(c.numIslands(grid))