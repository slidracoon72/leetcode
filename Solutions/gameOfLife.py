from typing import List


# Amazon Interview Question
# Neetcode: https://www.youtube.com/watch?v=fei4bJQdBUQ


# Define a Solution class containing the "Game of Life" logic
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Simulates the "Game of Life" rules on a given 2D board.
        The board is modified in-place, so no return value is needed.
        """

        # Define the translation table for new states:
        # Original | New | State
        #    0     |  0  |  0
        #    1     |  0  |  1
        #    0     |  1  |  2
        #    1     |  1  |  3

        # Get the number of rows and columns in the board
        ROWS, COLS = len(board), len(board[0])

        # Helper function to count the live neighbors around a given cell
        def countNeighbors(r, c) -> int:
            # Initialize a count for live neighbors
            nei = 0
            # Iterate through the surrounding 3x3 grid, excluding the current cell
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    # If out of bounds or if the current cell, skip this iteration
                    if ((i == r) and (j == c)) or i < 0 or j < 0 or i >= ROWS or j >= COLS:
                        continue
                    # Increment count if the neighboring cell is originally 'live' (state 1 or 3)
                    if board[i][j] in [1, 3]:
                        nei += 1
            return nei

        # First pass: Modify the board based on the Game of Life rules
        for r in range(ROWS):
            for c in range(COLS):
                # Count the live neighbors for the current cell
                nei = countNeighbors(r, c)
                # If the cell is 'live' and has 2 or 3 neighbors, set it to state 3 (remains live)
                if board[r][c]:
                    if nei in [2, 3]:
                        board[r][c] = 3
                # If the cell is 'dead' and has exactly 3 neighbors, set it to state 2 (becomes live)
                elif nei == 3:
                    board[r][c] = 2

        # Second pass: Apply the final state changes (state to new mapping)
        for r in range(ROWS):
            for c in range(COLS):
                # Convert state 1 to 0 (dead)
                if board[r][c] == 1:
                    board[r][c] = 0
                # Convert states 2 and 3 to 1 (live)
                elif board[r][c] in [2, 3]:
                    board[r][c] = 1


# Example input board
board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]

# Create an instance of the Solution class and run the gameOfLife method
c = Solution()
c.gameOfLife(board)

# Print the resulting board to observe the changes
print(board)
