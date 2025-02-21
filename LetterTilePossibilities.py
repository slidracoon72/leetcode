from collections import Counter


# DFS Backtracking - Recursion
# Neetcode: https://www.youtube.com/watch?v=8FrJX-P_DnE&ab_channel=NeetCodeIO
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Create a counter to track the frequency of each tile
        count = Counter(tiles)

        # Helper function to perform backtracking
        def backtrack():
            res = 0
            # Iterate over each unique tile in the counter
            for c in count:
                # If there are still tiles left to use
                if count[c] > 0:
                    res += 1  # Count the current tile arrangement
                    count[c] -= 1  # Use one instance of the tile
                    res += backtrack()  # Recur to generate further sequences
                    count[c] += 1  # Restore the tile count for backtracking
            return res

        # Start backtracking and return the total number of possible sequences
        return backtrack()


c = Solution()
tiles = "AAB"
print(c.numTilePossibilities(tiles))
