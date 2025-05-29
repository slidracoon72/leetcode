# LC - Hard

from collections import defaultdict
from typing import List


class Solution:
    # Solved using DFS
    # Neetcode: https://www.youtube.com/watch?v=xLoDjKczUSk&ab_channel=NeetCodeIO
    # Time: O(n*(n+m)*26), O(n*26 + m)
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # Build adjacency list for directed graph, mapping each node to its neighbors
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)

        # Initialize variables: n is number of nodes, res tracks max color frequency
        n, res = len(colors), 0
        # count[i][c] stores max frequency of color c in paths starting at node i
        count = [[0] * 26 for _ in range(n)]

        def dfs(node: int) -> int:
            # Detect cycle: if node is in current path, return infinity (invalid path)
            if node in path:
                return float('inf')
            # Skip already visited nodes to avoid recomputation (memoization)
            if node in visit:
                return 0

            # Mark node as visited and add to current path
            visit.add(node)
            path.add(node)

            # Get color index (0-25) for current node based on its color (a-z)
            colorIndex = ord(colors[node]) - ord('a')
            # Initialize count for current node's color to 1
            count[node][colorIndex] = 1

            # Explore neighbors recursively
            for nei in adj[node]:
                # If neighbor's DFS detects a cycle, propagate infinity
                if dfs(nei) == float('inf'):
                    return float('inf')

                # Update max frequency for each color at current node
                for c in range(26):
                    # Max of current count or (1 if color matches node's color else 0) + neighbor's count
                    count[node][c] = max(
                        count[node][c],
                        (1 if c == colorIndex else 0) + count[nei][c]
                    )

            # Remove node from path after exploring all neighbors (backtrack)
            path.remove(node)
            # Return max frequency of any color at this node
            return max(count[node])

        # visit tracks fully explored nodes, path tracks nodes in current DFS path
        visit, path = set(), set()
        # Run DFS from each node to find max color frequency across all paths
        for i in range(n):
            res = max(dfs(i), res)

        # Return -1 if cycle detected (infinity), else max color frequency
        return -1 if res == float('inf') else res


c = Solution()
colors = "abaca"
edges = [[0, 1], [0, 2], [2, 3], [3, 4]]
print(c.largestPathValue(colors, edges))
