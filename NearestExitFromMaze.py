from collections import deque
from typing import List

# BFS - Graph Traversal
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS, COLS = len(maze), len(maze[0])
        q = deque()
        q.append((entrance[0], entrance[1], 0))  # (row, col, steps)
        maze[entrance[0]][entrance[1]] = '+'  # Mark the entrance as visited

        # Directions for moving up, down, left, and right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, steps = q.popleft()
            for dr, dc in directions:
                row, col = r + dr, c + dc
                # Check if the new position is within bounds and not a wall
                if 0 <= row < ROWS and 0 <= col < COLS and maze[row][col] == '.':
                    # Check if this cell is an exit
                    if row == 0 or row == ROWS - 1 or col == 0 or col == COLS - 1:
                        return steps + 1
                    # Mark the cell as visited and add to the queue
                    maze[row][col] = '+'
                    q.append((row, col, steps + 1))

        return -1  # No exit found
