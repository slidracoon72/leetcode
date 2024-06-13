from collections import deque
from typing import List


# Breadth-First Search (BFS) approach to solve the problem
# BFS simulates simultaneous, level-by-level spread of rot
# Time Complexity: O(m * n) where m is the number of rows and n is the number of columns
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Initialize a deque for BFS and variables to track the grid dimensions, minutes passed, and the count of fresh oranges
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        minutes, fresh = 0, 0

        # Loop through the grid to add initial rotten oranges to the queue and count the fresh oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])  # Append the position of rotten oranges to the queue
                if grid[r][c] == 1:
                    fresh += 1  # Count the fresh oranges

        # Define the four possible directions for movement (up, down, left, right)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Perform BFS while there are rotten oranges in the queue and fresh oranges remain
        while q and fresh > 0:
            qLen = len(q)  # Get the current length of the queue
            for _ in range(qLen):
                r, c = q.popleft()  # Pop the leftmost rotten orange position from the queue
                for dr, dc in directions:
                    row, col = r + dr, c + dc  # Calculate the new position based on the current direction

                    # Check if the new position is within bounds and contains a fresh orange
                    if row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] != 1:
                        continue  # Skip if the new position is out of bounds or not a fresh orange

                    # If the new position has a fresh orange, make it rotten
                    if grid[row][col] == 1:
                        q.append([row, col])  # Add the new rotten orange position to the queue
                        grid[row][col] = 2  # Update the grid to mark the orange as rotten
                        fresh -= 1  # Decrease the count of fresh oranges
            minutes += 1  # Increment the minute counter after processing all positions in the current level

        # If there are no fresh oranges left, return the number of minutes passed; otherwise, return -1
        return minutes if fresh == 0 else -1
