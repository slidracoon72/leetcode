import heapq
from collections import defaultdict
from typing import List


class Solution:
    # Prim's Algorithm (Minimum Spanning Tree)
    # Time: O(n^2 * logn), Space: O(n^2)
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)  # Total number of points
        adj = defaultdict(list)  # Adjacency list to store graph as (neighbor, cost)

        # Build the adjacency list with Manhattan distances between every pair of points
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                manh_dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((j, manh_dist))
                adj[j].append((i, manh_dist))

        heap = [(0, 0)]  # Min-heap to pick the next minimum-cost edge (cost, node)
        visit = set()  # Set to keep track of visited nodes
        total_cost = 0  # Total cost to connect all points (MST weight)

        # Prim's Algorithm to find Minimum Spanning Tree
        while heap:
            cost, index = heapq.heappop(heap)

            # Skip if already visited
            if index in visit:
                continue

            # Add node to visited set and include edge cost in total
            visit.add(index)
            total_cost += cost

            # If all nodes are visited, break early
            if len(visit) == N:
                break

            # Add all unvisited neighbors of the current node to the heap
            for nei, nei_cost in adj[index]:
                if nei not in visit:
                    heapq.heappush(heap, (nei_cost, nei))

        return total_cost  # Return the total cost to connect all points


c = Solution()
points = [[0, 0], [2, 2], [3, 3], [2, 4], [4, 2]]
print(c.minCostConnectPoints(points))
