# Graph Theory Problem
# A tree is connected and has no cycles
# If there are n nodes in a tree, then there are (n - 1) edges
from collections import defaultdict
from typing import List


# Solved using Union-Find
# Time: O(E+V)
# Neetcode: https://www.youtube.com/watch?v=1lNK80tOTfc&ab_channel=NeetCodeIO
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

    def findRedundantConnection1(self, edges: List[List[int]]) -> List[int]:
        # Step 1: Build adjacency list to represent the graph
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()  # Tracks visited nodes during DFS
        cycle = set()  # Stores nodes that are part of the detected cycle
        cycleStart = -1  # Marks the start node of the cycle

        # Step 2: DFS to detect cycles and identify nodes in the cycle
        def dfs(node, par):
            nonlocal cycleStart
            # If the node is already visited, a cycle is detected
            if node in visit:
                cycleStart = node  # Mark the start of the cycle
                return True

            visit.add(node)
            for nei in adj[node]:
                if nei == par:  # Skip parent to avoid backtracking
                    continue
                # Recursively check neighbors for cycles
                if dfs(nei, node):
                    # If a cycle is found, add current node to the cycle set
                    if cycleStart != -1:
                        cycle.add(node)
                    # Reset cycleStart if we return to the starting node
                    if node == cycleStart:
                        cycleStart = -1
                    return True

            return False

        # Start DFS from node 1 (nodes are 1-indexed)
        dfs(1, -1)

        # Step 3: Find the last edge in the input that connects two cycle nodes
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]  # Return the redundant edge

        return []
