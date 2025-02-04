from collections import deque
from typing import List


# Neetcode: https://www.youtube.com/watch?v=mev55LTubBY&ab_channel=NeetCodeIO
# A graph is not bipartite if it has at least one cycle of odd length (odd number of edges)
# Thus, if the graph is not bipartite (odd cycle length), then it cannot be divided into distinct groups
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        odd = [0] * len(graph)  # Map node i -> odd = 1, even = -1

        def bfs(i):
            if odd[i] != 0:  # If already visited, continue
                return True

            q = deque([i])
            odd[i] = -1
            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if odd[node] == odd[nei]:
                        return False
                    elif odd[nei] == 0:
                        q.append(nei)
                        odd[nei] = -1 * odd[node]
            return True

        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True

    # Similar approach. Solved using alternating colors
    def isBipartite1(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph)  # 0: unvisited, 1: red, -1: green

        def bfs(i):
            if color[i] != 0:  # If already visited, continue
                return True

            q = deque([i])
            color[i] = 1  # Assign red color to start
            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if color[node] == color[nei]:  # Same color conflict means odd cycle
                        return False
                    elif color[nei] == 0:  # If unvisited, assign alternate color
                        q.append(nei)
                        color[nei] = -color[node]  # Alternate color (red ↔ green)
            return True

        for i in range(len(graph)):
            if color[i] == 0 and not bfs(i):  # Ensure all components are checked
                return False
        return True


c = Solution()
graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
print(c.isBipartite(graph))
print(c.isBipartite1(graph))
