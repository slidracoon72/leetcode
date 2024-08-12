from typing import List


# LC Hard Problem
# Time: O((m*n)^2), Space: O(m*n)
# Neetcode: https://www.youtube.com/watch?v=aO-QbJ5eZwU
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, visit):
            # Check boundary conditions, if already visited and if it is not land
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visit or grid[r][c] == 0:
                return
            visit.add((r, c))

            # Recursively call dfs on neighbours
            neighbours = [[r + 1, c], [r, c + 1], [r - 1, c], [r, c - 1]]
            for nr, nc in neighbours:
                dfs(nr, nc, visit)

        def number_of_islands() -> int:
            visit = set()
            islands = 0
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1 and (r, c) not in visit:
                        dfs(r, c, visit)
                        islands += 1
            return islands

        # If there are no islands or the islands are already disconnected (more than 1 exists), then no need to remove
        # if number_of_islands() != 1: -> same
        num = number_of_islands()
        if num == 0 or num > 1:
            return 0

        # If there is one island, we need to disconnect it
        for r in range(rows):
            for c in range(cols):
                # If water, continue
                if grid[r][c] == 0:
                    continue
                # If land, change to water to disconnect
                grid[r][c] = 0
                # Now, again count the number of islands after making land to water
                # If it is 0 or greater than 1, it means that removing one land is enough to disconnect island
                if number_of_islands() != 1:
                    return 1
                # If after removal, the number of islands is still 1, then convert it back to land
                grid[r][c] = 1

        # If not returned 0 or 1, it means we need to remove 2 islands to disconnect any island of any size (m*n)
        return 2


c = Solution()
grid = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
print(c.minDays(grid))
