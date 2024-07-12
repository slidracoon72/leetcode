from collections import defaultdict
from typing import List


class Solution:
    # Solved using DFS - Iterative
    # Time: O(E+V)
    def count_connected_components(self, n: int, edges: List[List[int]]) -> int:
        # Build the graph as an adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            # Use a stack to implement DFS iteratively
            stack = [node]
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    # Add all unvisited neighbors to the stack
                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            stack.append(neighbor)

        connected_components = 0

        # Iterate over all nodes to ensure all components are counted
        for node in range(n):
            if node not in visited:
                # If the node is not visited, it's a new connected component
                dfs(node)
                connected_components += 1

        return connected_components

    # Solved using Union-Find Algorithm
    # Neetcode: https://www.youtube.com/watch?v=8f1XPm4WOUc
    def count_connected_components1(self, n: int, edges: List[List[int]]) -> int:
        # Initialize parent array - each node is initially its own parent
        par = [i for i in range(n)]

        # Initialize rank array - each node initially has a rank of 1
        rank = [1] * n  # initially, each node has rank = 1 as they are their own component

        # Find function to find the root parent of a node
        def find(n1):
            res = n1
            # Find the root of the node, with path compression
            # Path compression makes the tree flatter, speeding up future operations
            while res != par[res]:
                par[res] = par[par[res]]  # Path compression step
                res = par[res]
            return res

        # Union function to connect two nodes
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            # If both nodes have the same root parent, they are already connected
            if p1 == p2:
                return 0

            # Union by rank to keep the tree shallow
            if rank[p2] > rank[p1]:
                par[p1] = p2  # Attach smaller rank tree under the root of the higher rank tree
                rank[p2] += rank[p1]  # Update the rank
            else:
                par[p2] = p1  # Attach smaller rank tree under the root of the higher rank tree
                rank[p1] += rank[p2]  # Update the rank

            return 1  # A union was performed, indicating two components merged

        connected_components = n  # Initially, there are n components (each node is its own component)

        # Iterate through all edges to connect components
        for n1, n2 in edges:
            connected_components -= union(n1, n2)  # Perform union and decrease the count if a union occurs

        return connected_components  # Return the number of connected components


n = 5
edges = [[0, 1], [1, 2], [3, 4]]
c = Solution()
print(c.count_connected_components(n, edges))
print(c.count_connected_components1(n, edges))
