# LC - Hard
# DO AGAIN
# LC-3373: Maximize the Number of Target Nodes After Connecting Trees II


from collections import defaultdict, deque
from typing import List


class Solution:
    # Solved similarly as Part 1 - Gives TLE (815 / 825 testcases passed)
    # Method to find the maximum number of target nodes for each node in the first tree
    # after connecting it to a node in the second tree, where target nodes have an even-distance path
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        # Initialize adjacency lists for both trees
        adj1, adj2 = defaultdict(list), defaultdict(list)

        # Build adjacency list for the first tree (undirected)
        for u, v in edges1:
            adj1[u].append(v)  # Add edge from u to v
            adj1[v].append(u)  # Add edge from v to u (undirected)

        # Build adjacency list for the second tree (undirected)
        for u, v in edges2:
            adj2[u].append(v)  # Add edge from u to v
            adj2[v].append(u)  # Add edge from v to u (undirected)

        # BFS function to count nodes at even and odd distances from a starting node
        def bfs(start, adj, max_nodes):
            # Initialize queue for BFS, storing (node, parent, distance) tuples
            q = deque([(start, -1, 0)])
            # Track visited nodes to avoid cycles
            visited = {start}
            # Count nodes at even and odd distances
            counts = [0, 0]  # [even_count, odd_count]
            counts[0] = 1  # Start node is at distance 0 (even)

            # Perform BFS
            while q:
                node, parent, dist = q.popleft()
                # Explore neighbors
                for nei in adj[node]:
                    if nei not in visited:  # Skip visited nodes
                        visited.add(nei)
                        new_dist = dist + 1
                        # Increment even or odd count based on new distance
                        counts[new_dist % 2] += 1
                        # Only continue BFS if we haven't exceeded max_nodes
                        if len(visited) < max_nodes:
                            q.append((nei, node, new_dist))

            return counts

        # Number of nodes in each tree
        n, m = len(edges1) + 1, len(edges2) + 1

        # Precompute even and odd distance counts for each node in both trees
        even_odd1 = [bfs(i, adj1, n) for i in range(n)]  # List of [even, odd] for tree 1
        even_odd2 = [bfs(i, adj2, m) for i in range(m)]  # List of [even, odd] for tree 2

        # Initialize result array
        result = [0] * n

        # For each node in the first tree
        for i in range(n):
            max_targets = 0
            # Try connecting to each node in the second tree
            for j in range(m):
                # Get even and odd counts for node i in tree 1
                even1, odd1 = even_odd1[i]
                # Get even and odd counts for node j in tree 2
                even2, odd2 = even_odd2[j]
                # Total target nodes:
                # - Even distance nodes in tree 1 (same parity as i to i is 0, even)
                # - If distance to i is even, need odd distance in tree 2 (since i->j adds 1 edge)
                # - If distance to i is odd, need even distance in tree 2
                targets = even1 + (odd2 if even1 else even2)
                # Update maximum target nodes for node i
                max_targets = max(max_targets, targets)
            result[i] = max_targets

        return result  # Return array of maximum target nodes for each node in tree 1


# LC - Editorial Solution
class Solution1:
    def maxTargetNodes(
            self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> List[int]:
        def dfs(node, parent, depth, children, color):
            res = 1 - depth % 2
            color[node] = depth % 2
            for child in children[node]:
                if child == parent:
                    continue
                res += dfs(child, node, depth + 1, children, color)
            return res

        def build(edges, color):
            n = len(edges) + 1
            children = [[] for _ in range(n)]
            for u, v in edges:
                children[u].append(v)
                children[v].append(u)
            res = dfs(0, -1, 0, children, color)
            return [res, n - res]

        n = len(edges1) + 1
        m = len(edges2) + 1
        color1 = [0] * n
        color2 = [0] * m
        count1 = build(edges1, color1)
        count2 = build(edges2, color2)
        res = [0] * n
        for i in range(n):
            res[i] = count1[color1[i]] + max(count2[0], count2[1])
        return res
