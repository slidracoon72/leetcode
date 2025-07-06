# LC Hard

from collections import defaultdict, deque
from typing import List
import heapq


# Solved using Dijkstra's algorithm
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Create initial adjacency list representing the default road connections between cities
        adj = defaultdict(list)
        for src in range(n - 1):
            adj[src].append([src + 1, 1])  # Road from city 'src' to 'src + 1' with a distance of 1

        start, end = 0, n - 1  # Start from city 0 and end at city n-1
        res = []  # To store the results of shortest path lengths after each query
        remaining = len(queries)  # Track remaining queries for potential early termination

        for src, dst in queries:
            # If a direct road from start to end is added, the shortest path will always be 1
            if src == start and dst == end:
                # Append 1 for all remaining queries since the shortest path is now directly available
                for _ in range(remaining):
                    res.append(1)
                break  # No need to process further queries

            # Add the new road from 'src' to 'dst' with distance 1
            adj[src].append([dst, 1])
            minHeap = [(0, start)]  # Min-heap for Dijkstra's, stores (current distance, current node)
            visit = set()  # Set to keep track of visited nodes

            # Dijkstra's algorithm for finding the shortest path
            while minHeap:
                dist, node = heapq.heappop(minHeap)  # Pop the node with the smallest distance
                visit.add(node)  # Mark the node as visited

                # If we've reached the end node, store the distance in the result
                if node == end:
                    res.append(dist)
                    remaining -= 1  # Decrease the remaining queries to process
                    break

                # Explore neighbors of the current node
                for nei, nei_dist in adj[node]:
                    if nei not in visit:
                        # Push the neighbor with the updated cumulative distance
                        heapq.heappush(minHeap, (dist + nei_dist, nei))

        return res  # Return the list of shortest path lengths after each query

    # Similar approach, but optimized
    def shortestDistanceAfterQueries1(self, n: int, queries: List[List[int]]) -> List[int]:
        # Create initial adjacency list with direct paths
        adj = defaultdict(list)
        for i in range(n - 1):
            adj[i].append((i + 1, 1))  # Add direct edge from i to i+1 with weight 1

        start, end = 0, n - 1
        res = []

        def dijkstra():
            minHeap = [(0, start)]  # (distance, node)
            distance = [float('inf')] * n
            distance[start] = 0

            while minHeap:
                dist, node = heapq.heappop(minHeap)
                if node == end:
                    return dist  # Early exit if we reach the end

                for nei, nei_dist in adj[node]:
                    new_dist = dist + nei_dist
                    if new_dist < distance[nei]:
                        distance[nei] = new_dist
                        heapq.heappush(minHeap, (new_dist, nei))
            return -1

        for src, dst in queries:
            # If query adds direct edge from start to end, shortest path becomes 1
            if src == start and dst == end:
                res.extend([1] * (len(queries) - len(res)))
                break

            # add new path to adjacency list
            adj[src].append((dst, 1))
            # find shortest distance
            res.append(dijkstra())

        return res


# Solving using BFS
# Neetcode: https://www.youtube.com/watch?v=zCeZOyACpUQ&ab_channel=NeetCodeIO
class Solution2:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[i + 1] for i in range(n - 1)]

        def shortest_path_BFS():
            q = deque()
            q.append((0, 0))  # node, length
            visit = set()
            visit.add(0)

            while q:
                cur, length = q.popleft()
                if cur == n - 1:
                    return length

                # explore neighbors
                for nei in adj[cur]:
                    if nei not in visit:
                        q.append((nei, length + 1))
                        visit.add(nei)

        res = []
        for src, dst in queries:
            adj[src].append(dst)
            res.append(shortest_path_BFS())

        return res
