import heapq
from typing import List, Tuple


class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


class Solution:
    # Using Min-Heap
    # Time: O(nlogn), Space: O(n)
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Sort intervals based on the start time of each meeting
        intervals.sort(key=lambda x: x.start)

        # Min-heap to keep track of the end times of ongoing meetings
        min_heap = []

        for i in intervals:
            # If the meeting with the earliest end time has ended before the current meeting starts,
            # we can reuse that room (i.e., remove the earliest ending meeting)
            if min_heap and min_heap[0] <= i.start:
                heapq.heappop(min_heap)

            # Add the current meeting's end time to the heap
            heapq.heappush(min_heap, i.end)

        # The size of the heap represents the number of rooms needed at the same time
        return len(min_heap)

    # Sliding Window
    # Time: O(nlogn), Space: O(n)
    # Neetcode: https://www.youtube.com/watch?v=FdzJmTCVyJU
    def minMeetingRooms1(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                count += 1  # count of ongoing meetings
                s += 1
            else:
                count -= 1  # since meeting finished, we decrement ongoing meetings
                e += 1
            res = max(res, count)
        return res
