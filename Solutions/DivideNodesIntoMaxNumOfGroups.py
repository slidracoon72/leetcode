# LC - Hard
# 2493. Divide Nodes Into the Maximum Number of Groups
from collections import defaultdict, deque
from typing import List


# Neetcode: https://www.youtube.com/watch?v=Gn0ADjje8Rg&ab_channel=NeetCodeIO
# A graph is not bipartite if it has at least one cycle of odd length (odd number of edges)
# Thus, if the graph is not bipartite (odd cycle length), then it cannot be divided into distinct groups
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)  # Adjacency list to represent the graph
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        # Function to get all connected components starting from a given source node
        def get_connected_components(src):
            q = deque([src])
            component = {src}  # Set to store nodes in the same connected component
            while q:
                node = q.popleft()
                for nei in adj[node]:
                    if nei in component:
                        continue  # Skip already visited nodes
                    q.append(nei)
                    component.add(nei)
                    visit.add(nei)  # Mark node as visited

            return component

        # BFS function to find the longest valid path (group assignment) in the component starting from 'src'
        def longest_path(src):
            q = deque([(src, 1)])  # (node, group)
            dist = {src: 1}  # Dictionary to track group numbers for each node

            while q:
                node, group = q.popleft()
                for nei in adj[node]:
                    if nei in dist:
                        # If a cycle is detected where the same group is assigned to both nodes
                        if dist[nei] == group:
                            return -1  # Indicates an odd-length cycle (graph is not bipartite)
                        continue
                    q.append((nei, group + 1))
                    dist[nei] = group + 1  # Assign group number to the neighbor

            return max(dist.values())  # Return the maximum group number

        visit = set()  # Set to keep track of visited nodes
        res = 0  # Stores the final count of the maximum group assignments
        for i in range(1, n + 1):
            if i in visit:
                continue  # Skip already visited nodes

            visit.add(i)
            component = get_connected_components(i)  # Get the connected component containing node i

            max_cnt = 0  # Store the maximum group count for this component
            for src in component:
                length = longest_path(src)  # length is the group number
                # If an odd-length cycle is detected, return -1 as the graph is not bipartite
                if length == -1:
                    return -1
                max_cnt = max(max_cnt, length)  # Update max count for this component
            res += max_cnt  # Add the max count from this component to the result

        return res  # Return the final result


c = Solution()
n = 6
edges = [[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]]
print(c.magnificentSets(n, edges))
