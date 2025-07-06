from typing import List
from collections import defaultdict
import heapq


class Solution:
    # Dijkstra's Algorithm
    # Time: O((V * E) * log V), Space: O(V + E)
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for fr, to, p in flights:
            adj[fr].append((to, p))

        minHeap = [(0, src, 0)]  # (price, node, stops)
        prices = {}  # (node, stops) -> price

        while minHeap:
            price, node, stops = heapq.heappop(minHeap)

            if node == dst:
                return price

            if stops > k:
                continue

            for nei, nei_price in adj[node]:
                new_price = price + nei_price
                new_stops = stops + 1

                if (nei, new_stops) not in prices or new_price < prices[(nei, new_stops)]:
                    prices[(nei, new_stops)] = new_price
                    heapq.heappush(minHeap, (new_price, nei, new_stops))

        return -1


c = Solution()
n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1
print(c.findCheapestPrice(n, flights, src, dst, k))
