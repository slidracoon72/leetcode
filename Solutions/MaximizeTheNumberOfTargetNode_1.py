# LC-3372: Maximize the Number of Target Nodes After Connecting Trees I

from collections import defaultdict, deque
from typing import List


# Solved using BFS - Level Order Traversal
# Techdose: https://www.youtube.com/watch?v=whTiu63X1CI&ab_channel=Techdose
# Time: O(V1 * (V1+E1) + V2 * (V2+E2)), Space: O(V1+E1+V2+E2)
class Solution:
    # Method to find the maximum number of target nodes reachable within k edges across two graphs
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        # Initialize adjacency lists for both graphs
        adj1, adj2 = defaultdict(list), defaultdict(list)

        # Build adjacency list for the first graph (undirected)
        for u, v in edges1:
            adj1[u].append(v)  # Add edge from u to v
            adj1[v].append(u)  # Add edge from v to u (undirected)

        # Build adjacency list for the second graph (undirected)
        for u, v in edges2:
            adj2[u].append(v)  # Add edge from u to v
            adj2[v].append(u)  # Add edge from v to u (undirected)

        # BFS function to count nodes reachable within k edges from a starting node
        def bfs(i, adj, k):
            # Initialize a queue for BFS, storing (node, parent) pairs
            q = deque()
            q.append((i, -1))  # Start with node i, no parent (-1)
            count = 0  # Track number of nodes reachable within k edges

            # Continue BFS while queue is not empty and k edges remain
            while q and k >= 0:
                size = len(q)  # Number of nodes at current level
                count += size  # Add nodes at this level to count
                # Process nodes level by level
                for _ in range(size):
                    node, parent = q.popleft()  # Get current node and its parent
                    # Explore neighbors
                    for nei in adj[node]:
                        if nei != parent:  # Skip the parent to avoid backtracking
                            q.append((nei, node))  # Add neighbor with current node as parent
                k -= 1  # Decrement remaining edge count when level is traversed

            return count  # Return total nodes reachable

        # Calculate number of nodes in each graph (edges + 1 for 0-based indexing)
        m, n = len(edges1) + 1, len(edges2) + 1

        # Find the maximum number of nodes reachable in the second graph within k-1 edges
        # It takes one hop/edge to connect tree1 to tree2, so we have (k-1) remaining edges
        best = 0
        for i in range(n):
            # Update best with the maximum nodes reachable from any node in graph 2
            best = max(best, bfs(i, adj2, k - 1))

        # Calculate result for each node in the first graph
        res = [0] * m  # Initialize result array for graph 1
        for i in range(m):
            # Get nodes reachable from node i in graph 1 within k edges
            nodes = bfs(i, adj1, k)
            # Add the best result from graph 2 to nodes reachable in graph 1
            res[i] = nodes + best

        return res  # Return array with total reachable nodes for each node in graph 1


c = Solution()
edges1 = [[0, 1], [0, 2], [2, 3], [2, 4]]
edges2 = [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]]
k = 2
print(c.maxTargetNodes(edges1, edges2, k))
