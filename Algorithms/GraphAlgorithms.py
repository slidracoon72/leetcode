from collections import defaultdict, deque
from typing import List, Dict, Set, Tuple
import heapq


class GraphAlgorithms:
    """
    Comprehensive collection of graph algorithms commonly tested in coding interviews.
    Each algorithm includes time complexity, space complexity, and detailed comments.
    """
    
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = set()
        self.recursion_stack = set()
    
    def add_edge(self, u: int, v: int, weight: int = 1):
        """Add a directed edge from u to v with optional weight."""
        self.graph[u].append((v, weight))
    
    def add_undirected_edge(self, u: int, v: int, weight: int = 1):
        """Add an undirected edge between u and v with optional weight."""
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
    
    def bfs(self, start: int) -> List[int]:
        """
        Breadth-First Search traversal of the graph.
        
        Time Complexity: O(V + E) where V = vertices, E = edges
        Space Complexity: O(V) for the queue and visited set
        
        Args:
            start: Starting vertex for BFS traversal
            
        Returns:
            List of vertices in BFS order
        """
        if start not in self.graph:
            return []
        
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            # Visit all adjacent vertices
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs_recursive(self, start: int) -> List[int]:
        """
        Depth-First Search using recursion.
        
        Time Complexity: O(V + E)
        Space Complexity: O(V) for recursion stack and visited set
        
        Args:
            start: Starting vertex for DFS traversal
            
        Returns:
            List of vertices in DFS order
        """
        visited = set()
        result = []
        
        def dfs_helper(vertex: int):
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_helper(neighbor)
        
        if start in self.graph:
            dfs_helper(start)
        
        return result
    
    def dfs_iterative(self, start: int) -> List[int]:
        """
        Depth-First Search using iteration (stack).
        
        Time Complexity: O(V + E)
        Space Complexity: O(V) for stack and visited set
        
        Args:
            start: Starting vertex for DFS traversal
            
        Returns:
            List of vertices in DFS order
        """
        if start not in self.graph:
            return []
        
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            vertex = stack.pop()
            
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                # Add unvisited neighbors to stack (in reverse order to maintain DFS order)
                for neighbor, _ in reversed(self.graph[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result
    
    def topological_sort_dfs(self, num_vertices: int) -> List[int]:
        """
        Topological Sort using DFS (for DAG - Directed Acyclic Graph).
        
        Time Complexity: O(V + E)
        Space Complexity: O(V) for recursion stack and visited sets
        
        Args:
            num_vertices: Total number of vertices in the graph
            
        Returns:
            Topologically sorted order of vertices, or empty list if cycle detected
        """
        visited = set()
        recursion_stack = set()
        result = []
        
        def dfs_topo(vertex: int) -> bool:
            """Returns True if cycle is detected."""
            visited.add(vertex)
            recursion_stack.add(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    if dfs_topo(neighbor):
                        return True
                elif neighbor in recursion_stack:
                    return True  # Back edge found - cycle detected
            
            recursion_stack.remove(vertex)
            result.append(vertex)
            return False
        
        # Check for cycles and build topological order
        for vertex in range(num_vertices):
            if vertex not in visited:
                if dfs_topo(vertex):
                    return []  # Cycle detected
        
        return result[::-1]  # Reverse to get correct topological order
    
    def topological_sort_kahn(self, num_vertices: int) -> List[int]:
        """
        Topological Sort using Kahn's algorithm (BFS approach).
        
        Time Complexity: O(V + E)
        Space Complexity: O(V) for queue and in-degree array
        
        Args:
            num_vertices: Total number of vertices in the graph
            
        Returns:
            Topologically sorted order of vertices, or empty list if cycle detected
        """
        # Calculate in-degrees
        in_degree = [0] * num_vertices
        for vertex in self.graph:
            for neighbor, _ in self.graph[vertex]:
                in_degree[neighbor] += 1
        
        # Add vertices with in-degree 0 to queue
        queue = deque()
        for vertex in range(num_vertices):
            if in_degree[vertex] == 0:
                queue.append(vertex)
        
        result = []
        count = 0  # Count of processed vertices
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            count += 1
            
            # Reduce in-degree of all neighbors
            for neighbor, _ in self.graph[vertex]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If count != num_vertices, there's a cycle
        return result if count == num_vertices else []
    
    def dijkstra(self, start: int, num_vertices: int) -> List[int]:
        """
        Dijkstra's algorithm for finding shortest paths from a single source.
        
        Time Complexity: O((V + E) log V) with binary heap
        Space Complexity: O(V) for distance array and priority queue
        
        Args:
            start: Source vertex
            num_vertices: Total number of vertices
            
        Returns:
            Array of shortest distances from start to all vertices
        """
        # Initialize distances
        distances = [float('inf')] * num_vertices
        distances[start] = 0
        
        # Priority queue: (distance, vertex)
        pq = [(0, start)]
        visited = set()
        
        while pq:
            current_dist, current_vertex = heapq.heappop(pq)
            
            if current_vertex in visited:
                continue
            
            visited.add(current_vertex)
            
            # Relax all edges from current vertex
            for neighbor, weight in self.graph[current_vertex]:
                if neighbor not in visited:
                    new_dist = current_dist + weight
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heapq.heappush(pq, (new_dist, neighbor))
        
        return distances
    
    def bellman_ford(self, start: int, num_vertices: int) -> List[int]:
        """
        Bellman-Ford algorithm for finding shortest paths (handles negative weights).
        
        Time Complexity: O(VE)
        Space Complexity: O(V) for distance array
        
        Args:
            start: Source vertex
            num_vertices: Total number of vertices
            
        Returns:
            Array of shortest distances, or None if negative cycle detected
        """
        # Initialize distances
        distances = [float('inf')] * num_vertices
        distances[start] = 0
        
        # Relax all edges V-1 times
        for _ in range(num_vertices - 1):
            for vertex in self.graph:
                for neighbor, weight in self.graph[vertex]:
                    if distances[vertex] != float('inf') and distances[vertex] + weight < distances[neighbor]:
                        distances[neighbor] = distances[vertex] + weight
        
        # Check for negative cycles
        for vertex in self.graph:
            for neighbor, weight in self.graph[vertex]:
                if distances[vertex] != float('inf') and distances[vertex] + weight < distances[neighbor]:
                    return None  # Negative cycle detected
        
        return distances
    
    def floyd_warshall(self, num_vertices: int) -> List[List[int]]:
        """
        Floyd-Warshall algorithm for finding shortest paths between all pairs.
        
        Time Complexity: O(V^3)
        Space Complexity: O(V^2) for distance matrix
        
        Args:
            num_vertices: Total number of vertices
            
        Returns:
            2D array of shortest distances between all pairs
        """
        # Initialize distance matrix
        distances = [[float('inf')] * num_vertices for _ in range(num_vertices)]
        
        # Set diagonal to 0
        for i in range(num_vertices):
            distances[i][i] = 0
        
        # Set direct edges
        for vertex in self.graph:
            for neighbor, weight in self.graph[vertex]:
                distances[vertex][neighbor] = weight
        
        # Floyd-Warshall algorithm
        for k in range(num_vertices):
            for i in range(num_vertices):
                for j in range(num_vertices):
                    if distances[i][k] != float('inf') and distances[k][j] != float('inf'):
                        distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
        
        return distances
    
    def detect_cycle_dfs(self) -> bool:
        """
        Detect cycle in directed graph using DFS.
        
        Time Complexity: O(V + E)
        Space Complexity: O(V) for visited sets
        
        Returns:
            True if cycle exists, False otherwise
        """
        visited = set()
        recursion_stack = set()
        
        def has_cycle(vertex: int) -> bool:
            visited.add(vertex)
            recursion_stack.add(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    if has_cycle(neighbor):
                        return True
                elif neighbor in recursion_stack:
                    return True
            
            recursion_stack.remove(vertex)
            return False
        
        for vertex in self.graph:
            if vertex not in visited:
                if has_cycle(vertex):
                    return True
        
        return False
    
    def detect_cycle_undirected_dfs(self) -> bool:
        """
        Detect cycle in undirected graph using DFS.
        
        Time Complexity: O(V + E)
        Space Complexity: O(V) for visited set
        
        Returns:
            True if cycle exists, False otherwise
        """
        visited = set()
        
        def has_cycle(vertex: int, parent: int) -> bool:
            visited.add(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    if has_cycle(neighbor, vertex):
                        return True
                elif neighbor != parent:
                    return True  # Back edge to non-parent vertex
            
            return False
        
        for vertex in self.graph:
            if vertex not in visited:
                if has_cycle(vertex, -1):
                    return True
        
        return False
    
    def count_connected_components(self) -> int:
        """
        Count number of connected components in undirected graph.
        
        Time Complexity: O(V + E)
        Space Complexity: O(V) for visited set
        
        Returns:
            Number of connected components
        """
        visited = set()
        count = 0
        
        def dfs_component(vertex: int):
            visited.add(vertex)
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_component(neighbor)
        
        for vertex in self.graph:
            if vertex not in visited:
                dfs_component(vertex)
                count += 1
        
        return count


# Example usage and testing
if __name__ == "__main__":
    # Create a sample graph
    ga = GraphAlgorithms()
    
    # Add edges for a sample directed graph
    ga.add_edge(0, 1, 4)
    ga.add_edge(0, 2, 3)
    ga.add_edge(1, 2, 1)
    ga.add_edge(1, 3, 2)
    ga.add_edge(2, 3, 4)
    ga.add_edge(3, 4, 2)
    ga.add_edge(4, 1, -1)
    
    print("Graph Algorithms Demo:")
    print("=====================")
    
    print(f"BFS from vertex 0: {ga.bfs(0)}")
    print(f"DFS Recursive from vertex 0: {ga.dfs_recursive(0)}")
    print(f"DFS Iterative from vertex 0: {ga.dfs_iterative(0)}")
    
    # Test shortest path algorithms
    print(f"Dijkstra distances from 0: {ga.dijkstra(0, 5)}")
    print(f"Bellman-Ford distances from 0: {ga.bellman_ford(0, 5)}")
    
    # Test cycle detection
    print(f"Cycle in directed graph: {ga.detect_cycle_dfs()}")
    
    # Test topological sort
    ga2 = GraphAlgorithms()
    ga2.add_edge(0, 1)
    ga2.add_edge(0, 2)
    ga2.add_edge(1, 3)
    ga2.add_edge(2, 3)
    ga2.add_edge(3, 4)
    
    print(f"Topological Sort (DFS): {ga2.topological_sort_dfs(5)}")
    print(f"Topological Sort (Kahn): {ga2.topological_sort_kahn(5)}") 