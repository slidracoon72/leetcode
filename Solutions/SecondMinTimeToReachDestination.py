from collections import defaultdict, deque
from typing import List


# LC Hard Problem
# Solved using BFS
# Time: O(E+V), Space: O(E+V) where E is the number of edges and V is the number of vertices
# Neetcode: https://www.youtube.com/watch?v=2F7gwxfy1CU
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # Create an adjacency list for the undirected graph
        adj = defaultdict(list)
        # Populate the adjacency list with edges
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # print(adj)

        # BFS Queue initialized with the start node (vertex 1)
        q = deque([1])
        cur_time = 0  # Current time in minutes
        res = -1  # To keep track of the time for the shortest path to node n
        visit_times = defaultdict(list)  # Dictionary to keep track of visit times for each node

        while q:
            # Get the current level length of the BFS
            qLen = len(q)

            # Process all nodes at the current level
            for i in range(qLen):
                node = q.popleft()  # Remove node from the front of the queue

                # Check if we reached the destination node
                if node == n:
                    # If this is not the shortest path, return the current time
                    if res != -1:
                        return cur_time
                    # If this is the shortest path, update res to the current time
                    res = cur_time

                # Explore all neighbors of the current node
                for nei in adj[node]:
                    # Get the list of visit times for this neighbor
                    nei_times = visit_times[nei]

                    # Add the neighbor to the queue if it has not been visited or if it's visited at a different time
                    if len(nei_times) == 0 or (len(nei_times) == 1 and nei_times[0] != cur_time):
                        q.append(nei)
                        # print("cur_time: ", cur_time)
                        visit_times[nei].append(cur_time)
                        # nei_times.append(cur_time) -> this is the same

            # Check if the current time is during a red light period
            if (cur_time // change) % 2 == 1:
                # Wait until the light turns green
                cur_time += change - (cur_time % change)

            # Increment the time by the traversal time of the edges
            cur_time += time


c = Solution()
n = 5
edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
time = 3
change = 5

print(c.secondMinimum(n, edges, time, change))
