from collections import defaultdict
from typing import List


# Leetcode - Hard
# Topological Sort, DFS
# Topological sort is an algorithm used to order the vertices of a directed acyclic graph (DAG)
# such that for every directed edge 𝑢 → 𝑣 u→v, vertex 𝑢 u comes before vertex  𝑣 v in the ordering.
# It is commonly used in scenarios like scheduling tasks, ordering prerequisites, and resolving dependencies.
# Neetcode: https://www.youtube.com/watch?v=khTKB1PzCuw
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # Helper function to perform Depth First Search (DFS) for topological sort
        # path is to detect cycle
        def dfs(src, adj, visit, path, order):
            if src in path:  # If a cycle is detected
                return False
            if src in visit:  # If already visited
                return True

            path.add(src)  # Add to current path
            for nei in adj[src]:  # Visit all neighbors
                if not dfs(nei, adj, visit, path, order):  # If a cycle is detected in any neighbor
                    return False
            path.remove(src)  # Remove from current path

            visit.add(src)  # Mark as visited
            order.append(src)  # Add to order
            return True

        # Helper function to perform topological sort
        def topo_sort(edges):
            adj = defaultdict(list)
            for src, dest in edges:  # Create adjacency list
                adj[src].append(dest)

            visit, path = set(), set()  # Sets for visited nodes and current path
            order = []  # List to store topological order
            for src in range(1, k + 1):  # Iterate over all nodes from 1 to k
                if src not in visit:  # If node is not visited
                    if not dfs(src, adj, visit, path, order):  # Perform DFS
                        return []  # Return empty list if a cycle is detected
            return order[::-1]  # Return reversed order

        # Get the topological order for rows and columns
        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)

        # If no valid topological order exists, return an empty matrix
        if not row_order or not col_order:
            return []

        # Maps to get the row and column index for each value
        val_to_row = {n: i for i, n in enumerate(row_order)}
        val_to_col = {n: i for i, n in enumerate(col_order)}

        # Initialize the result matrix with zeros
        res = [[0] * k for _ in range(k)]

        # Place each number in the matrix based on the topological order
        for num in range(1, k + 1):
            r = val_to_row[num]  # Get the row index for the number
            c = val_to_col[num]  # Get the column index for the number
            res[r][c] = num  # Place the number in the matrix

        return res


c = Solution()
k = 3
rowConditions = [[1, 2], [3, 2]]
colConditions = [[2, 1], [3, 2]]
print(c.buildMatrix(k, rowConditions, colConditions))
