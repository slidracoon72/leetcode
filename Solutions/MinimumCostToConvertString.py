import heapq
from collections import defaultdict
from typing import List, Dict


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Create an adjacency list for the graph
        adj = defaultdict(list)
        for o, c, cst in zip(original, changed, cost):
            adj[o].append([c, cst])

        def dijkstra(src: str) -> Dict[str, int]:
            # Dictionary to store the shortest distance to each node
            shortest = {}
            # Min-heap to store nodes for exploration (cost, node)
            minHeap = [(0, src)]  # Starting with source node with 0 cost

            while minHeap:
                dist1, node1 = heapq.heappop(minHeap)

                # Skip if this node has already been visited
                if node1 in shortest:
                    continue

                # Record the shortest distance to this node
                shortest[node1] = dist1

                # Explore neighbors
                for node2, dist2 in adj[node1]:
                    if node2 not in shortest:
                        heapq.heappush(minHeap, (dist1 + dist2, node2))

            return shortest

        # Compute shortest paths from all nodes
        all_nodes = set(source + target)  # Combine unique nodes from source and target
        shortest_paths = {}
        for node in all_nodes:
            shortest_paths[node] = dijkstra(node)

        # print(shortest_paths)

        total_cost = 0
        for i in range(len(source)):
            if source[i] != target[i]:
                # Calculate minimum cost to convert source[i] to target[i]
                cost_to_change = shortest_paths[source[i]].get(target[i], -1)
                if cost_to_change == -1:
                    # If any target is unreachable, return -1 or an appropriate value
                    return -1
                total_cost += cost_to_change

        return total_cost


c = Solution()
source = "abcd"
target = "acbe"
original = ["a", "b", "c", "c", "e", "d"]
changed = ["b", "c", "b", "e", "b", "e"]
cost = [2, 5, 5, 1, 2, 20]

print(c.minimumCost(source, target, original, changed, cost))
