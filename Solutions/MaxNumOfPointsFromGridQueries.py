# LC - Hard
# LC-2503: Maximum Number of Points From Grid Queries
import heapq
from collections import deque
from typing import List


class Solution:
    # Solved using BFS like NumberOfIslands.py
    # Gives TLE - Passes 17/21 Test Cases
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        answer = [0] * len(queries)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(k):
            if grid[0][0] >= k:  # If starting point is invalid, no points are reachable
                return 0

            seen = set([(0, 0)])  # Start with (0, 0) marked as visited
            count = 1  # Count starting point if valid
            q = deque([(0, 0)])

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc

                    if (0 <= new_r < rows and 0 <= new_c < cols and
                            (new_r, new_c) not in seen and grid[new_r][new_c] < k):
                        q.append((new_r, new_c))
                        seen.add((new_r, new_c))
                        count += 1

            return count

        for i, q in enumerate(queries):
            answer[i] = bfs(q)

        return answer

    # Solved by Sorting Queries + Min-Heap Expansion
    # Time: O(klogk + nlogn), Space: O(n + k) where n = size of grid = rows * cols, k = len(queries)
    def maxPoints1(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # Get grid dimensions
        rows, cols = len(grid), len(grid[0])
        # Initialize result array with zeros for each query
        answer = [0] * len(queries)
        # Pair each query with its original index and sort by query value
        queries = sorted([(q, i) for i, q in enumerate(queries)])  # Format: [(query_val, index)]

        # Initialize min-heap with starting cell (value, row, col) at (0, 0)
        minHeap = [(grid[0][0], 0, 0)]  # Priority queue sorted by grid value
        # Track visited cells to avoid cycles
        seen = {(0, 0)}
        # Count of reachable cells for current query
        count = 0
        # Define 4-directional movements: down, up, right, left
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Process each query in ascending order
        for q, i in queries:
            # Expand reachable cells while heap has values less than current query
            while minHeap and minHeap[0][0] < q:
                # Increment count for each valid cell processed
                count += 1
                # Pop smallest value cell from heap
                val, row, col = heapq.heappop(minHeap)

                # Explore all 4 adjacent cells
                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc
                    # Check if new position is within bounds and unvisited
                    if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in seen:
                        # Add new cell to heap with its grid value
                        heapq.heappush(minHeap, (grid[new_r][new_c], new_r, new_c))
                        # Mark as visited
                        seen.add((new_r, new_c))

            # Assign count to answer for this query’s original index if start is valid
            answer[i] = count if grid[0][0] < q else 0

        # Return the array with counts for each query
        return answer


c = Solution()
grid = [[1, 2, 3], [2, 5, 7], [3, 5, 1]]
queries = [5, 6, 2]
print(c.maxPoints1(grid, queries))
