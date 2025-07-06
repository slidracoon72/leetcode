import heapq
from collections import defaultdict
from typing import List


# LC-1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
# Solved using Dijkstra's Algorithm
# Neetcode: https://www.youtube.com/watch?v=--wKPR3ByJc
# Time: O((n^3)*(logn))
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize an adjacency list to store the graph
        adj = defaultdict(list)

        # Build the graph using the edges input
        for c1, c2, w in edges:
            adj[c1].append((c2, w))
            adj[c2].append((c1, w))

        # Define a helper function to perform Dijkstra's algorithm from a given source city
        def dijkstra(src):
            # Initialize a min-heap with the source node and a distance of 0
            heap = [(0, src)]  # (distance, node)
            # A set to keep track of visited nodes
            visit = set()

            while heap:
                # Pop the node with the smallest distance from the heap
                dist, node = heapq.heappop(heap)
                # If the node has already been visited, skip it
                if node in visit:
                    continue
                # Mark the node as visited
                visit.add(node)
                # Iterate over the neighbors of the current node
                for nei, dist_adj in adj[node]:
                    # Calculate the distance to the neighbor
                    nei_dist = dist + dist_adj
                    # If the distance to the neighbor is within the threshold, add it to the heap
                    if nei_dist <= distanceThreshold:
                        heapq.heappush(heap, (nei_dist, nei))
            # Return the count of reachable cities excluding the source city itself
            return len(visit) - 1

        # Initialize result variables to store the city with the smallest number of reachable cities
        res, min_count = -1, n
        # Iterate over each city to find the number of reachable cities using Dijkstra's algorithm
        for src in range(n):
            count = dijkstra(src)
            # If the current city has fewer or equal reachable cities than the previous minimum,
            # update the result. In case of a tie, prefer the city with the greater number.
            if count <= min_count:
                res, min_count = src, count
        # Return the city with the smallest number of reachable cities within the distance threshold
        return res
