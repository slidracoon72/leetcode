from typing import List


# Neetcode: https://www.youtube.com/watch?v=B90kG-ZlptE&ab_channel=NeetCodeIO
# Using Prefix Sum
# Time: O(n), Space: O(1)
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])  # Number of columns in the grid

        # Calculate prefix sums for both rows
        preSum1, preSum2 = grid[0].copy(), grid[1].copy()

        # Compute prefix sums for row 1 (grid[0]) and row 2 (grid[1])
        for i in range(1, n):
            preSum1[i] += preSum1[i - 1]  # Prefix sum for the top row
            preSum2[i] += preSum2[i - 1]  # Prefix sum for the bottom row

        # Initialize the result to infinity (minimum points robot 2 can collect)
        res = float('inf')

        # Iterate over all possible points where robot 1 can transition
        for i in range(n):
            # Calculate the points left for robot 2 in the top row
            # Robot 1 moves right, so the remaining points in the top row are from (i+1) to the end
            top = preSum1[-1] - preSum1[i]

            # Calculate the points left for robot 2 in the bottom row
            # Robot 1 moves down after column i, so robot 2 can collect points up to column i-1
            bottom = preSum2[i - 1] if i > 0 else 0

            # Robot 2 will take the maximum points it can collect from the remaining cells
            second_robot = max(top, bottom)

            # Robot 1 tries to minimize the maximum points robot 2 can collect
            res = min(res, second_robot)

        # Return the minimum points robot 2 can collect if both robots play optimally
        return res


c = Solution()
grid = [[2, 5, 4], [1, 5, 1]]
print(c.gridGame(grid))
