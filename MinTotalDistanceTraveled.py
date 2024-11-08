import math
from functools import lru_cache
from typing import List


class Solution:
    # YouTube: https://www.youtube.com/watch?v=ewG0KzrRb3E
    # Time: O(f*r*k), Space: O(f*r*k)
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Using @lru_cache to store previously computed results for faster access and avoiding re-computation
        @lru_cache(None)
        def cost(f, r, k):
            # Base Case 1: If all robots have been assigned, return 0 (no additional cost)
            if r == len(robot):
                return 0
            # Base Case 2: If all factories have been considered without assigning all robots, return infinity
            # This signifies an invalid scenario since all robots need repair
            if f == len(factory):
                return math.inf

            # Option 1: Skip the current factory
            skip = cost(f + 1, r, 0)  # Move to the next factory without assigning the current robot

            # Option 2: Assign the current robot to the current factory if within its repair limit
            if k + 1 <= factory[f][1]:  # Check if this factory can take on another repair
                # Calculate the distance for this assignment
                assign = cost(f, r + 1, k + 1) + abs(factory[f][0] - robot[r])
                # Choose the minimum cost between skipping or assigning
                return min(skip, assign)

            # Return the result if assigning is not possible due to the limit
            return skip

        # Sort robots and factories by position to enable optimal assignments based on proximity
        robot.sort()
        factory.sort()
        # Initiate the recursive function starting from the first factory, first robot, and no repairs yet at the first factory
        return cost(0, 0, 0)
