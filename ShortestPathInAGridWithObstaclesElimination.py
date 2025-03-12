# LC - Hard
import heapq
from collections import deque
from typing import List


# Similar to MinObstacleRemovalToReachCorner.py
class Solution:
    # Solved using Dijkstra's Algorithm
    # Time: O(rows * cols * k * log(rows * cols * k)), Space: O(rows * cols * k)
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # Get grid dimensions: rows (m) and columns (n)
        rows, cols = len(grid), len(grid[0])

        # Initialize min-heap with starting state: (steps, row, col, remaining_obstacles)
        # Start at (0, 0) with 0 steps and k obstacles to eliminate
        minHeap = [(0, 0, 0, k)]

        # Visited set to track states: (row, col, remaining_obstacles)
        # Prevents revisiting the same position with the same elimination capacity
        visit = {(0, 0, k)}

        # Process states in order of minimum steps using Dijkstra's algorithm
        while minHeap:
            # Pop the state with the fewest steps from the heap
            steps, row, col, rem_obs = heapq.heappop(minHeap)

            # If we reached the target (bottom-right corner), return the steps
            if (row, col) == (rows - 1, cols - 1):
                return steps

            # Define 4 possible moves: down, up, right, left
            nei = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]

            # Explore each neighboring cell
            for r, c in nei:
                # Skip if the new position is out of bounds
                if r < 0 or c < 0 or r == rows or c == cols:
                    continue

                # Calculate remaining obstacles after moving to this cell
                # Subtract 1 if it's an obstacle (grid[r][c] = 1), 0 if empty
                new_k = rem_obs - grid[r][c]

                # Define the new state with updated position and remaining obstacles
                new_state = (r, c, new_k)

                # If we can move (new_k >= 0) and haven't visited this state before
                if new_k >= 0 and new_state not in visit:
                    # Mark this state as visited
                    visit.add(new_state)
                    # Add to heap with incremented steps
                    heapq.heappush(minHeap, (steps + 1, r, c, new_k))

        # If heap is exhausted and target not reached, return -1 (no path possible)
        return -1

    # Solved using BFS
    def shortestPath1(self, grid: list[list[int]], k: int) -> int:
        # Get grid dimensions
        rows, cols = len(grid), len(grid[0])

        # If grid is 1x1, no steps needed
        if rows == 1 and cols == 1:
            return 0

        # Queue: (row, col, remaining_k, steps)
        # Start at (0, 0) with k eliminations and 0 steps
        q = deque([(0, 0, k, 0)])

        # Visited set: (row, col, remaining_k)
        # Tracks states to avoid revisiting with same or fewer eliminations
        visit = {(0, 0, k)}

        # Directions: down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # BFS loop
        while q:
            row, col, rem_k, steps = q.popleft()

            # Reached target
            if row == rows - 1 and col == cols - 1:
                return steps

            # Explore 4 directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                # Check if within bounds
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    # Remaining eliminations after this move
                    new_k = rem_k - grid[new_row][new_col]
                    new_state = (new_row, new_col, new_k)

                    # If we can move (new_k >= 0) and haven't visited this state
                    if new_k >= 0 and new_state not in visit:
                        visit.add(new_state)
                        # Add to queue with incremented steps
                        q.append((new_row, new_col, new_k, steps + 1))

        # No path found within k eliminations
        return -1


c = Solution()
grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
k = 1
print(c.shortestPath(grid, k))
print(c.shortestPath1(grid, k))
