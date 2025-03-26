from collections import defaultdict
from typing import List


class Solution:
    # Solved using DFS
    # Time: O(V + E), Space: O(V + E)
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build the adjacency list for the undirected graph
        # adj[vertex] will store a list of vertices connected to vertex
        # Since the graph is undirected, each edge (a, b) adds b to a's list and a to b's list
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # Step 2: Initialize a set to track visited nodes
        # This prevents revisiting nodes during DFS and helps identify new components
        seen = set()

        # Step 3: Define a DFS function to collect vertices in a connected component
        # Parameters:
        # - node: The current vertex being processed
        # - component: A list to store all vertices in the current connected component
        def dfs(node, component):
            # If the node has already been visited, skip it
            if node in seen:
                return
            # Mark the node as visited and add it to the current component
            seen.add(node)
            component.append(node)
            # Recursively visit all neighbors of the current node
            for nei in adj[node]:
                dfs(nei, component)

        # Step 4: Process each vertex to find connected components
        # res will count the number of complete connected components
        res = 0
        for node in range(n):
            # If the node hasn't been visited, it's part of a new connected component
            if node not in seen:
                # Initialize a list to store vertices in the current component
                component = []
                # Use DFS to collect all vertices in this component
                dfs(node, component)

                # Step 5: Check if the component is complete
                # k is the number of vertices in the component
                k = len(component)
                # A component is complete if every vertex is connected to all other vertices
                # In a complete graph with k vertices, each vertex must have degree k-1
                # (since it connects to all other vertices in the component)
                # Check if the degree of each vertex in the component is k-1
                if all([k - 1 == len(adj[vertex]) for vertex in component]):
                    res += 1

        # Step 6: Return the total number of complete connected components
        return res


c = Solution()
n = 6
edges = [[0, 1], [0, 2], [1, 2], [3, 4]]
print(c.countCompleteComponents(n, edges))

n = 6
edges = [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]
print(c.countCompleteComponents(n, edges))
