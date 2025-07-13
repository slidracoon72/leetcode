from typing import List


class Solution:
    # Backtracking
    def makesquare(self, matchsticks: List[int]) -> bool:
        # Step 1: Calculate the total length of all matchsticks
        total_length = sum(matchsticks)

        # If total length is not divisible by 4, it's impossible to form a square
        if total_length % 4 != 0:
            return False

        # Each side of the square must have this length
        length = total_length // 4

        # Initialize the 4 sides of the square to length 0
        sides = [0] * 4

        # Sort the matchsticks in descending order to optimize DFS
        matchsticks.sort(reverse=True)

        # Helper function: try to place matchstick[i] into one of the sides
        def dfs(i):
            # If all matchsticks have been placed, return True
            if i == len(matchsticks):
                return True

            # Try placing matchstick[i] into each side
            for side in range(4):
                # Only place if it doesn't exceed the target side length
                if sides[side] + matchsticks[i] <= length:
                    # Choose
                    sides[side] += matchsticks[i]

                    # Explore
                    if dfs(i + 1):
                        return True

                    # Un-choose (backtrack)
                    sides[side] -= matchsticks[i]

            # If matchstick[i] cannot be placed in any side, return False
            return False

        # Start DFS from the first matchstick
        return dfs(0)


c = Solution()
matchsticks = [1, 1, 2, 2, 2]
print(c.makesquare(matchsticks))
