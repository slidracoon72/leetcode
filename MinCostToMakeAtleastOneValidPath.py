# LC - Hard
# 1368. Minimum Cost to Make at Least One Valid Path in a Grid
from collections import deque
from typing import List


# Similar to MinObstacleRemovalToReachCorner.py
# Reach from top-left to bottom-right of the grid with minimum cost
class Solution:
    # Solved using Deque - BFS
    # We keep the deque monotonically increasing
    # Neetcode: https://www.youtube.com/watch?v=3DwA6AsQvDI&ab_channel=NeetCodeIO
    # Time: O(m*n)
    def minCost(self, grid: List[List[int]]) -> int:
        directions = {
            1: [0, 1],  # right
            2: [0, -1],  # left
            3: [1, 0],  # down
            4: [-1, 0]  # up
        }

        rows, cols = len(grid), len(grid[0])
        q = deque([(0, 0, 0)])  # row, col, cost
        min_cost = {(0, 0): 0}  # row, col -> min_cost

        while q:
            row, col, cost = q.popleft()
            if (row, col) == (rows - 1, cols - 1):
                return cost

            # Explore neighbors
            for d in directions:
                dr, dc = directions[d]
                nr, nc = row + dr, col + dc
                n_cost = cost if d == grid[row][col] else cost + 1

                if nr < 0 or nc < 0 or nr == rows or nc == cols or n_cost >= min_cost.get((nr, nc), float('inf')):
                    continue

                min_cost[(nr, nc)] = n_cost
                if d == grid[row][col]:
                    q.appendleft((nr, nc, n_cost))
                else:
                    q.append((nr, nc, n_cost))


c = Solution()
grid = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]
print(c.minCost(grid))
