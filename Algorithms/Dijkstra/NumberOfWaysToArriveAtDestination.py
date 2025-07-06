from collections import defaultdict
import heapq
from typing import List


class Solution:
    # Solved using Dijkstra's and Recursive Backtracking - Gives TLE (Passes 16/55 Testcases)
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Build adjacency list
        adj = defaultdict(list)
        for u, v, time in roads:
            adj[u].append((v, time))
            adj[v].append((u, time))

        # Step 1: Find shortest time k using Dijkstra's
        def dijkstras():
            minHeap = [(0, 0)]  # (time, node)
            visited = set()
            while minHeap:
                time, node = heapq.heappop(minHeap)
                if node in visited:
                    continue
                visited.add(node)
                if node == n - 1:
                    return time
                for nei, nei_time in adj[node]:
                    if nei not in visited:
                        heapq.heappush(minHeap, (time + nei_time, nei))
            return -1  # If no path exists

        k = dijkstras()
        if k == -1:
            return 0  # No path exists

        # Step 2: Count paths with time exactly k using backtracking
        def count_paths(node, curr_time, visited):
            if curr_time > k:  # Prune if time exceeds k
                return 0
            if node == n - 1:  # Reached target
                return 1 if curr_time == k else 0
            count = 0
            for next_node, edge_time in adj[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    count += count_paths(next_node, curr_time + edge_time, visited)
                    visited.remove(next_node)  # Backtrack
            return count

        # Start backtracking from node 0
        return count_paths(0, 0, {0})

    # Dijkstra's Algorithm - Optimized
    # Time: O((V * E) * log n), Space: O(V + E)
    # Neetcode: https://www.youtube.com/watch?v=VFCzKOH1hnk&ab_channel=NeetCodeIO
    def countPaths1(self, n: int, roads: List[List[int]]) -> int:
        # Create an adjacency list to represent the bidirectional graph
        adj = defaultdict(list)
        # Iterate over each road (edge) in the input
        for u, v, w in roads:
            # Add edge from u to v with weight w (time)
            adj[u].append((w, v))
            # Add edge from v to u with weight w (since graph is bidirectional)
            adj[v].append((w, u))

        # Define modulo constant to prevent integer overflow (common in path-counting problems)
        MOD = 10 ** 9 + 7
        # Initialize a min-heap with (cost, node) pairs, starting at node 0 with cost 0
        min_heap = [(0, 0)]  # (cost, node)
        # Array to store the minimum cost (time) to reach each node from node 0
        min_cost = [float('inf')] * n
        # Array to store the number of ways to reach each node with its minimum cost
        path_count = [0] * n
        # Base case: 1 way to reach node 0 with cost 0 (starting point)
        path_count[0] = 1
        # Initialize minimum cost to reach node 0 as 0
        min_cost[0] = 0

        # Process nodes in order of increasing cost using Dijkstra's algorithm
        while min_heap:
            # Extract the node with the smallest cost from the heap
            cost, node = heapq.heappop(min_heap)

            # Explore all neighbors of the current node
            for nei_cost, nei in adj[node]:
                # Calculate the total cost to reach the neighbor through the current node
                if cost + nei_cost < min_cost[nei]:
                    # If this path is shorter than the previously known minimum cost
                    # Update the minimum cost to reach the neighbor
                    min_cost[nei] = cost + nei_cost
                    # The number of ways to reach the neighbor is the same as the ways to reach the current node
                    path_count[nei] = path_count[node]
                    # Add the neighbor to the heap with its updated cost
                    heapq.heappush(min_heap, (min_cost[nei], nei))

                # If this path equals the minimum cost to reach the neighbor
                elif cost + nei_cost == min_cost[nei]:
                    # Add the number of ways to reach the current node to the neighbor's path count
                    # Use modulo to prevent overflow
                    path_count[nei] = (path_count[nei] + path_count[node]) % MOD

        # Return the number of ways to reach node n-1 with its minimum cost
        return path_count[n - 1]


# Example usage
if __name__ == "__main__":
    solution = Solution()
    n = 7
    roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5],
             [4, 6, 2]]
    result = solution.countPaths(n, roads)
    print(f"Number of ways: {result}")  # Output: 1
