# LC Hard

import heapq
from typing import List


# Solving using Dijkstra's Algorithm
class Solution:
    # Neetcode: https://www.youtube.com/watch?v=Kj98r8IgJOQ&ab_channel=NeetCodeIO
    # Time: O(rows * cols * log(rows * cols))
    # Space: O(rows * cols)
    def minimumTime(self, grid: List[List[int]]) -> int:
        # If the cells (0, 1) and (1, 0) require more than 1 second to access, it's impossible to move forward.
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        rows, cols = len(grid), len(grid[0])
        target = (rows - 1, cols - 1)  # Define the target cell (bottom-right)

        # Min-heap to keep track of the cells to visit with their respective time costs (time, row, col)
        minHeap = [(0, 0, 0)]  # Start with the top-left cell (0, 0) at time 0
        visit = {(0, 0)}  # Set to track visited cells to avoid cycles

        while minHeap:
            # Get the cell with the smallest time cost
            time, row, col = heapq.heappop(minHeap)

            # If we've reached the target cell, return the time taken
            if (row, col) == target:
                return time

            # Generate all possible neighboring cells (up, down, left, right)
            neighbors = [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]
            for nr, nc in neighbors:
                # Check if the neighbor is within grid bounds and not visited
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visit:
                    wait = 0  # Additional wait time adjustment

                    # Check if the time difference causes us to wait based on even/odd constraints
                    if abs(grid[nr][nc] - time) % 2 == 0:
                        wait = 1

                    # Calculate the next possible time to visit this cell
                    next_time = max(grid[nr][nc] + wait, time + 1)
                    heapq.heappush(minHeap, (next_time, nr, nc))  # Push the neighbor into the heap
                    visit.add((nr, nc))  # Mark the neighbor as visited

        # Return -1 if the target cell is not reachable
        return -1


c = Solution()
grid = [[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]]
print(c.minimumTime(grid))
