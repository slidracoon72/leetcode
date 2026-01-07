from typing import List
from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # DFS to compute height of tree rooted at node
        def dfs(node, parent):
            height = 0
            for nei in adj[node]:
                if nei == parent:
                    continue
                height = max(height, 1 + dfs(nei, node))
            return height

        res = []
        min_height = float("inf")

        for i in range(n):
            h = dfs(i, -1)
            if h < min_height:
                min_height = h
                res = [i]
            elif h == min_height:
                res.append(i)

        return res
