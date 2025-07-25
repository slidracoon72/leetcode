import heapq
from typing import List


# Solving using Dijkstra's Algorithm
class Solution:
    # Time: O(rows * cols * log(rows * cols))
    # Space: O(rows * cols)
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        target = (rows - 1, cols - 1)

        # Possible directions: down, up, right, left
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Min-heap to prioritize paths with lowest current effort
        heap = [(0, 0, 0)]  # (effort so far, row, col)

        # Set to keep track of visited cells to avoid reprocessing
        visit = set()

        while heap:
            # Pop the cell with the lowest effort from the heap
            effort, r, c = heapq.heappop(heap)

            # If we reached the destination cell, return the effort
            if (r, c) == target:
                return effort

            # Skip if already visited
            if (r, c) in visit:
                continue

            # Mark the current cell as visited
            visit.add((r, c))

            # Get the height of the current cell
            cur = heights[r][c]

            # Check all 4 neighboring cells
            for dr, dc in directions:
                row, col = r + dr, c + dc

                # If within bounds and not yet visited
                if 0 <= row < rows and 0 <= col < cols and (row, col) not in visit:
                    # Calculate the max effort required so far to move to this neighbor
                    max_effort = max(effort, abs(cur - heights[row][col]))

                    # Push the neighbor into the heap with updated effort
                    heapq.heappush(heap, (max_effort, row, col))

        # If we somehow exit the loop without reaching the target
        return 0


c = Solution()
heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
print(c.minimumEffortPath(heights))
