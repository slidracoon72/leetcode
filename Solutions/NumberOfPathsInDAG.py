# Number of Unique Paths in a Directed Acyclic Graph
from collections import defaultdict


class Solution:
    def num_paths(self, edges, start_node, end_node):
        """
        Calculates the number of unique paths from a start_node to an end_node
        in a directed acyclic graph.

        Args:
            edges (list): A list of tuples representing directed edges (u, v).
            start_node: The starting node.
            end_node: The target ending node.

        Returns:
            int: The total number of unique paths.
        """
        # Build the adjacency list representation of the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        # Memoization cache to store the number of paths from a node
        memo = {}

        def dfs(current_node):
            # If the number of paths from this node is already calculated, return it
            if current_node in memo:
                return memo[current_node]

            # Base case: if we have reached the end_node, we've found one path
            if current_node == end_node:
                return 1

            # Recursive case: explore all neighbors
            count = 0
            for neighbor in graph[current_node]:
                count += dfs(neighbor)

            # Store the result in the memoization cache
            memo[current_node] = count

            return count

        return dfs(start_node)


# Example usage based on the problem description
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('B', 'C'),
    ('C', 'E'),
    ('E', 'D'),
    ('D', 'F')
]

start_node = 'A'
end_node = 'F'

c = Solution()
result = c.num_paths(edges, start_node, end_node)
print(f"The number of unique paths from {start_node} to {end_node} is: {result}")
