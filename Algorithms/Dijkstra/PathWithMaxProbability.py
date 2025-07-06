import heapq
from collections import defaultdict
from typing import List


# Solved using Dijkstra's algorithm
# Using MaxHeap since we want maximum probability
# Neetcode: https://www.youtube.com/watch?v=kPsDTGcrzGM
# Time: O((E+V)*logV), Space: O(V+E)
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        # Step 1: Create an adjacency list to represent the graph
        adj = defaultdict(list)
        for e, sp in zip(edges, succProb):
            src, dst = e[0], e[1]
            # Add both directions (src -> dst and dst -> src) with the success probability
            adj[src].append([dst, sp])
            adj[dst].append([src, sp])

        # Step 2: Use a max-heap (priority queue) to store (-probability, node)
        # We use negative probability because Python's heapq is a min-heap by default
        maxHeap = [(-1, start_node)]
        # Set to keep track of visited nodes to avoid revisiting them
        visit = set()

        # Step 3: Perform Dijkstra's algorithm
        while maxHeap:
            # Pop the node with the maximum probability (negated to positive)
            prob, cur = heapq.heappop(maxHeap)
            visit.add(cur)  # Mark the node as visited

            # If we reached the end node, return the probability (negate it back)
            if cur == end_node:
                return prob * -1

            # Explore neighbors of the current node
            for nei, edgeProb in adj[cur]:
                if nei not in visit:  # Only proceed if the neighbor hasn't been visited
                    # Push the new probability (accumulated) and neighbor node to the heap
                    heapq.heappush(maxHeap, (prob * edgeProb, nei))

        # If the end node is not reachable, return 0
        return 0
