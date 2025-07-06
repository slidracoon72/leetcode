from collections import deque
from typing import List


class Solution:
    # Solved using Linear Traversal of a Directed Graph
    # Time: O(n), Space: O(n)
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # If both starting nodes are the same, return it directly
        if node1 == node2:
            return node1

        # Helper function to compute distance from a start node to all reachable nodes
        def compute_distance(start):
            dist = {}  # Dictionary to store distance from start to each reachable node
            cur = start
            distance = 0
            visit = set()  # Set to track visited nodes and avoid cycles

            # Traverse along the path as long as the current node is not visited and is valid
            while cur != -1 and cur not in visit:
                visit.add(cur)
                dist[cur] = distance
                distance += 1
                cur = edges[cur]  # Move to the next node in the path

            return dist

        # Compute distances from node1 and node2 to all other nodes
        n1 = compute_distance(node1)
        n2 = compute_distance(node2)

        n = len(edges)
        res = -1  # Result node index
        max_min_dist = float('inf')  # Initialize to a large number for comparison

        # Iterate through all nodes to find the closest meeting node
        for node in range(n):
            # Only consider nodes reachable from both node1 and node2
            if node in n1 and node in n2:
                max_dist = max(n1[node], n2[node])  # Take the worse (larger) distance

                # Update result if a closer node is found
                if max_dist < max_min_dist:
                    max_min_dist = max_dist
                    res = node
                # If distances are equal, pick the node with the smaller index
                elif max_dist == max_min_dist and node < res:
                    res = node

        return res

    # Solved using BFS - Similar as above
    # Time: O(n), Space: O(n)
    def closestMeetingNode1(self, edges: List[int], node1: int, node2: int) -> int:
        # Helper function to compute shortest distances using BFS
        def bfs(start):
            dist = {}
            queue = deque([(start, 0)])
            visited = set()

            while queue:
                node, d = queue.popleft()
                if node in visited or node == -1:
                    continue
                visited.add(node)
                dist[node] = d
                next_node = edges[node]
                if next_node != -1 and next_node not in visited:
                    queue.append((next_node, d + 1))

            return dist

        # Compute distance maps for both nodes
        dist1 = bfs(node1)
        dist2 = bfs(node2)

        n = len(edges)
        res = -1
        min_max_dist = float('inf')

        for i in range(n):
            if i in dist1 and i in dist2:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_max_dist:
                    min_max_dist = max_dist
                    res = i
                elif max_dist == min_max_dist and i < res:
                    res = i

        return res

    # Solved using DFS - Similar as above
    # Time: O(n), Space: O(n)
    def closestMeetingNode2(self, edges: List[int], node1: int, node2: int) -> int:
        # DFS helper function to compute distances from the start node
        def dfs(node, dist_map, visited, distance):
            if node == -1 or node in visited:
                return
            visited.add(node)
            dist_map[node] = distance
            dfs(edges[node], dist_map, visited, distance + 1)

        # Distance and visited maps for both nodes
        dist1, dist2 = {}, {}
        visited1, visited2 = set(), set()

        # Run DFS from node1 and node2
        dfs(node1, dist1, visited1, 0)
        dfs(node2, dist2, visited2, 0)

        n = len(edges)
        res = -1
        min_max_dist = float('inf')

        # Find the node with the smallest max(dist1, dist2)
        for i in range(n):
            if i in dist1 and i in dist2:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_max_dist:
                    min_max_dist = max_dist
                    res = i
                elif max_dist == min_max_dist and i < res:
                    res = i

        return res


c = Solution()
edges = [2, 2, 3, -1]
node1 = 0
node2 = 1
print(c.closestMeetingNode(edges, node1, node2))
print(c.closestMeetingNode1(edges, node1, node2))
print(c.closestMeetingNode2(edges, node1, node2))
