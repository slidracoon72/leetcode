import heapq
from collections import defaultdict
from typing import List, Dict


# Dijkstra's Algorith is a greedy, BFS algorithm to find the shortest path from a source to a destination
# Here, we find the shortest path from a source node to all the other nodes in the directed, weighted graph
# Given: n nodes (0 to n-1), edges: (src, dest, weight), src: starting point
# Return: Dict with node and distance pair from source(src)
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # Initialize an adjacency list to store the graph
        adj = defaultdict(list)

        # Build the directed graph using the edges input
        for s, d, weight in edges:
            adj[s].append([d, weight])  # node, weight
            # adj[s].append((d, weight)) -> can also append in tuple form

        # Dictionary to store the shortest distance from the source node to each node
        shortest = {}

        # since we want minimum distance, weight goes as the first parameter for the min-heap
        # Min-heap (priority queue) to store (distance, node) pairs for the algorithm
        # Initialize with the source node and a distance of 0
        minHeap = [[0, src]]  # weight, node

        # Process the heap until it is empty
        while minHeap:
            # Pop the node with the smallest distance from the heap
            dist1, node1 = heapq.heappop(minHeap)
            # If the node has already been processed, skip it
            if node1 in shortest:
                continue
            # Record the shortest distance to this node
            shortest[node1] = dist1

            # Iterate over the neighbors of the current node
            for node2, dist2 in adj[node1]:
                # If the neighbor has not been processed, push it onto the heap with the updated distance
                if node2 not in shortest:
                    heapq.heappush(minHeap, [dist1 + dist2, node2])

        # Ensure all nodes are included in the result, even if they are unreachable (distance = -1)
        # Sometimes, graphs can be disconnected
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest


c = Solution()
n = 5
edges = [[0, 1, 10], [0, 2, 3], [1, 3, 2], [2, 1, 4], [2, 3, 8], [2, 4, 2], [3, 4, 5]]
src = 0
print(c.shortestPath(n, edges, src))
