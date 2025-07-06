# LC - Hard
# DO AGAIN

from typing import List


class Solution:
    def find(self, dsuf: List[int], v: int) -> int:
        if dsuf[v] == -1:
            return v
        dsuf[v] = self.find(dsuf, dsuf[v])  # Path compression
        return dsuf[v]

    def traverse_component(self, bitwise_and: List[int], curr: int, visited: List[bool],
                           adj: List[List[tuple]]) -> None:
        visited[curr] = True
        for nbr, wt in adj[curr]:
            bitwise_and[0] &= wt  # Update bitwise AND
            if not visited[nbr]:
                self.traverse_component(bitwise_and, nbr, visited, adj)

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # Step 1: Initialize disjoint-set and adjacency list
        dsuf = [-1] * n
        adj = [[] for _ in range(n)]
        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))

            px = self.find(dsuf, u)
            py = self.find(dsuf, v)
            if px != py:
                dsuf[px] = py  # Union

        # Step 2: Precompute minimum walk cost (bitwise AND) for each component
        parent_cost = {}
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                bitwise_and = [0 if not adj[i] else adj[i][0][1]]
                self.traverse_component(bitwise_and, i, visited, adj)
                parent = self.find(dsuf, i)
                parent_cost[parent] = bitwise_and[0]

        # Step 3: Answer each query
        ans = []
        for u, v in query:
            px = self.find(dsuf, u)
            py = self.find(dsuf, v)
            if px == py:
                ans.append(parent_cost[px])
            else:
                ans.append(-1)
        return ans
