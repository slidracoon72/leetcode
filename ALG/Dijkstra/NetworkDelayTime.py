import heapq
from collections import defaultdict
from typing import List


class Solution:
    # Dijkstra's Algorithm
    # Time: O((V * E) * log V), Space: O(V + E)
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))

        minHeap = [(0, k)]  # (time, node)
        visit = set()

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in visit:
                continue

            visit.add(node)
            if len(visit) == n:
                return time

            for nei, nei_time in adj[node]:
                heapq.heappush(minHeap, (time + nei_time, nei))

        return -1


c = Solution()
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(c.networkDelayTime(times, n, k))
