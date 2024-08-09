from typing import List


class Solution:
    # From start, we move right once, down once; then left twice, up twice;
    # then right thrice, down thrice and so on.
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # Directions array to define movement in the matrix
        # Directions are ordered as: right, down, left, up
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        # Initialize the starting position
        r, c = rStart, cStart

        # List to store the result, i.e., the spiral order of coordinates
        res = []

        # Initial number of steps to move in a direction
        steps = 1

        # Index to track the current direction from 'directions'
        i = 0

        # Continue until we have covered all cells in the matrix
        while len(res) < rows * cols:
            # For each step size (same size of steps for two directions)
            # We have to move same number of steps for right, down and left, up. Thus, loop twice for same 'steps'
            for x in range(2):
                # Get the current direction to move
                dr, dc = directions[i]

                # Move in the current direction for 'steps' number of times
                for y in range(steps):
                    # Check if the current cell is within the matrix boundaries
                    if 0 <= r < rows and 0 <= c < cols:
                        # Add the current cell's coordinates to the result
                        res.append([r, c])

                    # Update the current cell's position based on direction
                    r, c = r + dr, c + dc

                # Move to the next direction in a clockwise manner
                # The index 'i' cycles through 0 to 3 to navigate through 'directions'
                i = (i + 1) % 4

            # After completing one full cycle of right/down or left/up directions, increase the number of steps
            # This ensures that we cover the spiral pattern correctly
            steps += 1

        # Return the list of coordinates in spiral order
        return res


c = Solution()
rows = 5
cols = 6
rStart = 1
cStart = 4
print(c.spiralMatrixIII(rows, cols, rStart, cStart))
