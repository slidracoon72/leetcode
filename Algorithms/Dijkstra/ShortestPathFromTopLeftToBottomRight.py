import heapq


class Solution:
    def shortest_path_8_directions(self, matrix):
        if not matrix or not matrix[0]:
            return float('inf')

        rows, cols = len(matrix), len(matrix[0])
        if rows == 0 or cols == 0:
            return float('inf')

        # Directions: up, down, left, right, and four diagonals
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]

        # Distance array initialized to infinity
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = matrix[0][0]  # Start with the weight of the top-left cell

        # Priority queue to store (distance, row, col)
        pq = [(matrix[0][0], 0, 0)]
        visited = set()

        while pq:
            d, i, j = heapq.heappop(pq)

            if (i, j) in visited:
                continue

            visited.add((i, j))

            # If reached bottom-right, return distance
            if i == rows - 1 and j == cols - 1:
                return d

            # Explore all 8 directions
            for di, dj in directions:
                ni, nj = i + di, j + dj

                # Check bounds and if cell is not infinity (impassable)
                if (0 <= ni < rows and 0 <= nj < cols and
                        matrix[ni][nj] != float('inf')):

                    new_dist = d + matrix[ni][nj]

                    if new_dist < dist[ni][nj]:
                        dist[ni][nj] = new_dist
                        heapq.heappush(pq, (new_dist, ni, nj))

        return dist[rows - 1][cols - 1] if dist[rows - 1][cols - 1] != float('inf') else float('inf')


# Example usage with the given 7x7 matrix
matrix = [
    [0, 4, 4, 3, 10, 3, 10],
    [3, 10, 1, 10, float('inf'), 4, 1],
    [1, float('inf'), 10, float('inf'), 3, float('inf'), 10],
    [float('inf'), 10, 10, float('inf'), 10, 3, 1],
    [1, 10, float('inf'), 4, float('inf'), 3, 10],
    [3, float('inf'), 1, 10, 1, 10, 1],
    [float('inf'), 1, 3, 10, 4, 10, 0]
]

c = Solution()
result = c.shortest_path_8_directions(matrix)
print(f"Shortest path weight from (0,0) to ({len(matrix) - 1},{len(matrix[0]) - 1}): {result}")
