# DO AGAIN

import heapq
from typing import List


class Solution:
    # Greedy algorithm - maximize the number of events that can be attended
    # Time Complexity: O(n log n) due to sorting and heap operations
    # Space Complexity: O(n) for storing events in the min-heap
    def maxEvents(self, events: List[List[int]]) -> int:
        # Sort events by start day to process them in chronological order
        events.sort()

        n = len(events)  # Total number of events
        day = 1  # Current day being processed
        count = 0  # Number of events attended
        min_heap = []  # Min-heap to store end days of events that can be attended
        i = 0  # Index to track current event in sorted events list

        # Continue processing while there are events to consider or events in the heap
        while i < n or min_heap:
            # If heap is empty, jump to the start day of the next unprocessed event
            if not min_heap:
                day = max(day, events[i][0])

            # Add all events that start on the current day to the heap
            while i < n and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1])  # Store event's end day
                i += 1

            # Remove events that have already ended (end day < current day)
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            # If there are events available, attend the one that ends soonest
            if min_heap:
                heapq.heappop(min_heap)  # Remove the earliest-ending event
                count += 1  # Increment attended events count

            # Advance to the next day
            day += 1

        # Return the total number of events attended
        return count


c = Solution()
events = [[1, 2], [2, 3], [3, 4], [5, 6], [5, 6], [5, 6]]
print(c.maxEvents(events))
