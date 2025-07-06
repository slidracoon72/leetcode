# LC - Hard
from collections import defaultdict
from typing import List


# Neetcode: https://www.youtube.com/watch?v=pq61VNqXGvA&ab_channel=NeetCodeIO
# Time: O(n^2), Space: O(n^2)
# Step 1: Precompute areas of existing islands
# Step 2: Map (r, c) -> island -> area
# Step 3: Connect in 4 directions by flipping 0 to 1 to get max area of island
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)  # Size of the grid (n x n matrix)

        # Function to check if a cell is out of bounds
        def out_of_bounds(r, c):
            return r < 0 or c < 0 or r == n or c == n

        # DFS function to explore and label an island, while calculating its size
        def dfs(r, c, label):
            if out_of_bounds(r, c) or grid[r][c] != 1:  # If out of bounds or not land or already visited, return 0
                return 0

            grid[r][c] = label  # Mark the current cell with the unique island label

            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]  # Possible directions (down, up, right, left)
            size = 1  # Initialize island size as 1 (current cell)
            for nr, nc in neighbors:
                size += dfs(nr, nc, label)  # Recursively explore neighbors and accumulate size

            return size  # Return total size of the island

        # 1. Precompute areas of all islands
        area = defaultdict(int)  # Dictionary to store {island label -> island size}
        label = 2  # Start labeling from 2 (since 0 = water, 1 = initial land)
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:  # If it's land, start DFS to label and calculate its area
                    area[label] = dfs(r, c, label)
                    label += 1  # Increment label for the next island

        # Function to check the maximum island size if we flip a single water cell (0 → 1)
        def connect(r, c):
            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]  # Possible directions
            visit = set()  # Set to track visited island labels
            res = 1  # Start with 1 (flipping this 0 to 1 counts as part of the island)

            for nr, nc in neighbors:
                if not out_of_bounds(nr, nc) and grid[nr][nc] not in visit:
                    res += area[grid[nr][nc]]  # Add the size of the neighboring island
                    visit.add(grid[nr][nc])  # Mark the island as visited

            return res  # Return the potential max size of the island after the flip

        # 3. Try flipping each water cell and calculate the largest island possible
        res = 0 if not area else max(area.values())  # Get max island size if no water cells exist
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:  # Only consider water cells (0s)
                    res = max(res, connect(r, c))  # Try flipping and update max island size

        return res  # Return the maximum island size possible


c = Solution()
grid = [[1, 0, 0, 0], [1, 0, 1, 1], [1, 0, 0, 1], [1, 0, 1, 1]]
print(c.largestIsland(grid))
