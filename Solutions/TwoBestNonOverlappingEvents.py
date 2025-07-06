import heapq
from typing import List


class Solution:
    # Using Min-Heap
    # Time: O(nlogn), Space: O(n)
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Step 1: Sort events by their start time to process them in chronological order
        events.sort()

        # Initialize variables
        best_prev = float('-inf')  # Stores the maximum value of non-overlapping events processed so far
        best = max(v for _, _, v in events)  # Maximum value of a single event

        # Use a min-heap to track previous events by their end times
        heap = []  # Each entry in the heap is (endTime, value) of a previous event

        # Step 2: Iterate through the sorted events
        for s, e, v in events:
            # Process all previous events whose end time is less than the current event's start time
            while heap and heap[0][0] < s:
                end, value = heapq.heappop(heap)  # Remove the earliest ending event from the heap
                best_prev = max(best_prev, value)  # Update best_prev with the maximum value seen so far

            # Add the current event to the heap
            heapq.heappush(heap, (e, v))

            # Calculate the maximum sum of the current event and the best non-overlapping event
            best = max(best, v + best_prev)

        # Step 3: Return the maximum sum of two non-overlapping events
        return best
