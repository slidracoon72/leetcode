from typing import List


# Graph - DFS
# Time: O(N+E), Space: O(N+E)
# Neetcode: https://www.youtube.com/watch?v=m17yOR5_PpI
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Initialize a set to store the directed edges for quick lookup
        edges = {(a, b) for a, b in connections}

        # Initialize a dictionary to store the neighbors of each city
        neighbors = {city: [] for city in range(n)}

        # Set to keep track of visited cities to avoid cycles
        visited = set()

        # Variable to count the number of edges that need to be reordered
        count = 0

        # Populate the neighbors dictionary with both directions of each connection
        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        # Depth-First Search (DFS) function to traverse the graph
        def dfs(city):
            nonlocal count  # Declare that we want to use the 'count' variable from the enclosing scope
            for neighbor in neighbors[city]:
                if neighbor in visited:
                    continue  # Skip already visited neighbors

                # If the edge from neighbor to city does not exist in the original directed edges,
                # it means we need to reorder the edge from city to neighbor
                if (neighbor, city) not in edges:
                    count += 1  # Increment the count of edges that need to be reordered

                visited.add(neighbor)  # Mark the neighbor as visited
                dfs(neighbor)  # Recursively call dfs on the neighbor

        visited.add(0)  # Start the DFS from city 0
        dfs(0)  # Call DFS starting from city 0
        return count  # Return the total count of edges that need to be reordered


n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
c = Solution()
print(c.minReorder(n, connections))
