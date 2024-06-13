from typing import List, Tuple


class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


# Sliding Window
# Time: O(nlogn), Space: O(n)
# Neetcode: https://www.youtube.com/watch?v=FdzJmTCVyJU
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
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


# Helper function to convert list of tuples to list of Interval objects
def convert_to_intervals(tuples: List[Tuple[int, int]]) -> List[Interval]:
    return [Interval(start, end) for start, end in tuples]


# Example usage
c = Solution()

# Example 1
intervals1 = [(0, 30), (5, 10), (15, 20)]
intervals1_converted = convert_to_intervals(intervals1)
print(c.minMeetingRooms(intervals1_converted))  # Output: 2

# Example 2
intervals2 = [(2, 7), (9, 12), (13, 19)]
intervals2_converted = convert_to_intervals(intervals2)
print(c.minMeetingRooms(intervals2_converted))  # Output: 1
