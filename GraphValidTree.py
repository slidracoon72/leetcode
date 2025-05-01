# Time & Space Complexity: O(E + V)
# Neetcode: https://www.youtube.com/watch?v=bXsUuownnoQ

class Solution:
    def validTree(self, n, edges):
        # A graph is a valid tree if:
        # 1. There are no cycles
        # 2. All nodes are connected

        # If no nodes, the graph is trivially a tree
        if not n:
            return True

        # Create an adjacency list to represent the graph
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            # For an undirected graph, add the connection both ways
            adj[n1].append(n2)
            adj[n2].append(n1)

        # A set to keep track of visited nodes
        visit = set()

        def dfs(i, prev):
            # If we encounter a node that we've seen before, there is a cycle
            if i in visit:
                return False

            # Mark this node as visited
            visit.add(i)

            # Check all adjacent nodes
            for nei in adj[i]:
                # Ignore the node we came from to prevent false cycle detection
                if nei == prev:
                    continue

                # Recursively perform DFS, if a cycle is detected return False
                if not dfs(nei, i):
                    return False

            return True

        # Perform DFS starting from node 0. Ensure there are no cycles
        # and that all nodes are connected (visited).
        return dfs(0, -1) and n == len(visit)


c = Solution()
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(c.validTree(n, edges))
