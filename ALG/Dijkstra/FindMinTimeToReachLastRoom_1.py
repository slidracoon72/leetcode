import heapq
from typing import List


# Solving using Dijkstra's Algorithm
class Solution:
    # Time: O(rows * cols * log(rows * cols))
    # Space: O(rows * cols)
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # Get the number of rows and columns from the moveTime grid
        rows, cols = len(moveTime), len(moveTime[0])
        # Define the target position, which is the bottom-right corner of the grid
        target = (rows - 1, cols - 1)

        # Initialize a min-heap with the starting position (0, 0) and time 0
        minHeap = [(0, 0, 0)]  # (time, row, col)
        visit = {(0, 0)}  # Set to keep track of visited cells

        # Loop until there are no more cells to process in the heap
        while minHeap:
            # Pop the cell with the minimum time from the heap
            time, row, col = heapq.heappop(minHeap)

            # If we've reached the target cell, return the time taken
            if (row, col) == target:
                return time

            # Define the possible neighboring cells (up, down, left, right)
            neighbors = [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]
            for nr, nc in neighbors:
                # Check if the neighboring cell is within bounds and not visited
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visit:
                    # Calculate the next time to reach the neighboring cell
                    # Wait if we arrive before the required moveTime for that cell
                    next_time = max(time, moveTime[nr][nc]) + 1
                    # Push the neighboring cell and the calculated time into the min-heap
                    heapq.heappush(minHeap, (next_time, nr, nc))
                    # Mark the neighboring cell as visited
                    visit.add((nr, nc))

        # If the target cell is unreachable, return -1
        return -1
