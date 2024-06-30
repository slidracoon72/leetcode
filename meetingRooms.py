from typing import List


# class Interval(object):
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end


class Solution:
    def can_attend_meetings(self, intervals: List) -> bool:
        if not intervals:
            return True  # since no intervals, no conflicts

        # sorting according to the start time
        intervals.sort(key=lambda x: x[0])

        for i in range(len(intervals) - 1):
            # if end time of current meeting is greater than start time of next meeting
            if intervals[i][1] > intervals[i + 1][0]:
                return False

        return True


c = Solution()
# intervals = [(0, 30), (5, 10), (15, 20)]
intervals = [(5, 8), (9, 15)]
print((c.can_attend_meetings(intervals)))
