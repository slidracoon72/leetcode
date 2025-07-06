from collections import defaultdict
from typing import List


# Hierholzer's Algorithm
# This problem is about finding a valid Eulerian path in a directed graph formed by the input pairs.
# An Eulerian path is a trail in a graph that visits every edge exactly once. If we can construct such a path,
# the result is guaranteed to be valid.

# Eulerian Path:
# An Eulerian path exists in a directed graph if and only if:
# At most one node has out-degree - in-degree = 1 (start of the path).
# At most one node has in-degree - out-degree = 1 (end of the path).
# All other nodes have in-degree == out-degree.
# This ensures we can traverse all edges exactly once.
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # Step 1: Build the graph
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1

        # Step 2: Find the starting node for the Eulerian path
        start_node = pairs[0][0]
        for node in graph:
            if out_degree[node] > in_degree[node]:
                start_node = node
                break

        # Step 3: Hierholzer's algorithm to find the Eulerian path
        # Run DFS from start node
        result = []

        def dfs(node):
            while graph[node]:
                next_node = graph[node].pop()
                dfs(next_node)  # first explore
                result.append([node, next_node])  # then append

        dfs(start_node)

        # Step 4: Return the result in reverse order
        return result[::-1]


c = Solution()
pairs = [[5, 1], [4, 5], [11, 9], [9, 4]]
print(c.validArrangement(pairs))
