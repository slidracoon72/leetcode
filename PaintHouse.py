from typing import List


# Dynamic Programming: Top-Down Approach
# Time: O(n), where n is the number of houses
# Space: O(1), as we are using a fixed amount of space regardless of input size
# Neetcode: https://www.youtube.com/watch?v=-w67-4tnH5U&pp=ygULcGFpbnQgaG91c2U%3D
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        Calculate the minimum cost to paint all houses such that no two adjacent houses have the same color.

        Args:
        costs (List[List[int]]): A 2D list where costs[i][j] represents the cost of painting house i with color j.

        Returns:
        int: The minimum cost to paint all houses.
        """
        houses = len(costs)  # Number of houses to be painted

        # Initialize dp array where dp0, dp1, dp2 represent the minimum costs for the last house
        # painted with red, blue, and green respectively
        dp = [0, 0, 0]

        # Iterate over each house to compute the minimum cost
        for i in range(houses):
            # Compute cost for painting the current house with red
            dp0 = costs[i][0] + min(dp[1], dp[2])
            # Compute cost for painting the current house with blue
            dp1 = costs[i][1] + min(dp[0], dp[2])
            # Compute cost for painting the current house with green
            dp2 = costs[i][2] + min(dp[0], dp[1])
            # Update dp array with the costs for the current house
            dp = [dp0, dp1, dp2]

        # Return the minimum cost among the three colors for the last house
        return min(dp)


c = Solution()
costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
print(c.minCost(costs))
