# LC - Hard

import math
from functools import cache
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid)  # Size of the grid (N x N)

        @cache
        def maxPath(i: int, j: int, I: int, J: int) -> int:
            """
            Recursive function to compute the maximum number of cherries that can be collected
            by two "warriors" moving from (0,0) to (N-1,N-1) simultaneously.
            i, j -> coordinates of first warrior
            I, J -> coordinates of second warrior
            """

            # Base case: If either warrior goes out of bounds OR lands on a thorn (-1),
            # this path is invalid, so return negative infinity to discard it.
            if (i < 0 or N <= i or j < 0 or N <= j or grid[i][j] == -1) or \
                    (I < 0 or N <= I or J < 0 or N <= J or grid[I][J] == -1):
                return -math.inf

            # Base case: If both warriors reach the bottom-right cell (N-1, N-1),
            # return the number of cherries at that cell.
            if i == N - 1 and j == N - 1 and I == N - 1 and J == N - 1:
                return grid[i][j]

            # Calculate cherries collected at current positions.
            # If both warriors are on the same cell, count it only once.
            cherries = grid[i][j] if (i == I and j == J) else grid[i][j] + grid[I][J]

            # Recursively compute the maximum cherries by considering all possible moves:
            # 1. Both go down
            # 2. Both go right
            # 3. First goes right, second goes down
            # 4. First goes down, second goes right
            best_next = max(
                maxPath(i + 1, j, I + 1, J),  # both go down
                maxPath(i, j + 1, I, J + 1),  # both go right
                maxPath(i, j + 1, I + 1, J),  # first right, second down
                maxPath(i + 1, j, I, J + 1),  # first down, second right
            )

            return cherries + best_next  # Add current cherries to the best future path

        # The maximum cherries collected starting with both warriors at (0, 0).
        # If the result is negative (no valid path), return 0.
        return max(0, maxPath(0, 0, 0, 0))


c = Solution()
grid = [
    [0, 1, -1, 1, 0],
    [0, -1, 1, -1, 1],
    [1, 0, 1, 0, 0],
    [0, 1, -1, 1, 1],
    [1, 0, 0, -1, 0]
]
print(c.cherryPickup(grid))
