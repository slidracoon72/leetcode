import heapq


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = {}
        if v not in self.graph:
            self.graph[v] = {}
        self.graph[u][v] = w
        self.graph[v][u] = w

    def dijkstra(self, src):
        # Initialize distances from source to all other vertices as infinite
        distances = {v: float('inf') for v in self.graph}
        distances[src] = 0

        # Initialize min-heap
        min_heap = [(0, src)]  # (distance, vertex)

        # Initialize shortest paths dictionary
        shortest_paths = {v: [] for v in self.graph}

        while min_heap:
            # Extract the vertex with minimum distance value
            dist_u, u = heapq.heappop(min_heap)

            # Update shortest paths list
            shortest_paths[u].append(u)

            # Iterate through all adjacent vertices of u
            for v in self.graph[u]:
                w = self.graph[u][v]
                # If the distance to v through u is shorter
                if distances[v] > dist_u + w:
                    # Update distance of v
                    distances[v] = dist_u + w
                    # Update shortest paths list
                    shortest_paths[v] = shortest_paths[u] + [v]
                    # Push the updated distance and vertex to min-heap
                    heapq.heappush(min_heap, (distances[v], v))

        return shortest_paths


# Example usage:
if __name__ == "__main__":
    # Example graph
    g = Graph()
    g.add_edge('A', 'B', 10)
    g.add_edge('A', 'K', 3)
    g.add_edge('B', 'C', 36)
    g.add_edge('K', 'D', 16)
    g.add_edge('K', 'J', 18)
    g.add_edge('C', 'D', 3)
    g.add_edge('D', 'X', 1)
    g.add_edge('X', 'F', 10)
    g.add_edge('X', 'E', 22)
    g.add_edge('K', 'J', 18)
    g.add_edge('E', 'I', 3)
    g.add_edge('E', 'H', 10)
    g.add_edge('J', 'n', 1)
    g.add_edge('J', 'L', 16)
    g.add_edge('n', 'I', 1)
    g.add_edge('n', 'M', 4)
    g.add_edge('I', 'N', 4)
    g.add_edge('N', 'M', 21)
    g.add_edge('H', 'Z', 13)
    g.add_edge('H', 'O', 4)
    g.add_edge('Z', 'Q', 4)
    g.add_edge('Z', 'N', 16)
    g.add_edge('L', 'Y', 3)
    g.add_edge('Y', 'P', 6)
    g.add_edge('Y', 'S', 8)
    g.add_edge('P', 'S', 4)
    g.add_edge('P', 'h', 17)
    g.add_edge('S', 'U', 9)
    g.add_edge('h', 'R', 27)
    g.add_edge('h', 'O', 13)
    g.add_edge('O', 'T', 8)
    g.add_edge('T', 'U', 1)
    g.add_edge('T', 'V', 16)
    g.add_edge('U', 't', 1)
    g.add_edge('t', 'W', 8)
    g.add_edge('t', 'G', 9)

    source_node = 'A'
    shortest_paths = g.dijkstra(source_node)

    print("Shortest paths from source node", source_node)
    for vertex, path in shortest_paths.items():
        # Remove duplicate nodes from the path
        cleaned_path = list(dict.fromkeys(path))
        print("Node", vertex, ": Path:", cleaned_path)
