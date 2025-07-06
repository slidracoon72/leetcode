# LC - Hard

from collections import defaultdict
import heapq
from typing import List


# Solving using Dijkstra's Algorithm
# Time: O(n+m), Space: O(n+m)
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0  # Already at the destination

        # Map each bus stop to the buses that visit it
        stop_to_buses = defaultdict(list)
        for bus, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(bus)

        # Priority queue for Dijkstra's algorithm
        heap = [(0, source)]  # (number of buses taken, current bus stop)
        visited_stops = set()  # Track visited stops
        visited_buses = set()  # Track visited buses

        while heap:
            buses_taken, current_stop = heapq.heappop(heap)

            if current_stop == target:
                return buses_taken

            if current_stop in visited_stops:
                continue
            visited_stops.add(current_stop)

            # Explore all buses that visit this stop
            for bus in stop_to_buses[current_stop]:
                if bus in visited_buses:
                    continue
                visited_buses.add(bus)

                # Add all stops reachable by this new bus to the heap
                for next_stop in routes[bus]:
                    if next_stop not in visited_stops:
                        heapq.heappush(heap, (buses_taken + 1, next_stop))

        return -1  # If the target is not reachable


c = Solution()
routes = [[1, 2, 7], [3, 6, 7]]
source = 1
target = 6
print(c.numBusesToDestination(routes, source, target))
