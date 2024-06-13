from typing import List


# Intervals
# Time: O(nlogn) {sorting array} + O(n) {iterating through intervals} = O(nlogn)
# Neetcode: https://www.youtube.com/watch?v=nONCGxWoUfM
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals based on their start time
        intervals.sort()

        # Initialize the result counter to count the number of intervals to be removed
        res = 0

        # Initialize prevEnd to the end time of the first interval
        prevEnd = intervals[0][1]

        # Iterate over the remaining intervals, starting from the second interval
        for start, end in intervals[1:]:
            # Check if the current interval does not overlap with the previous interval
            if start >= prevEnd:
                # If not overlapping, update prevEnd to the end time of the current interval
                prevEnd = end
            else:
                # If overlapping, increment the result counter
                res += 1
                # Update prevEnd to the minimum of the current end and previous end
                # This is to ensure we keep the interval with the earliest end time,
                # which increases the chance of non-overlapping with subsequent intervals
                prevEnd = min(prevEnd, end)

        # Return the total number of intervals that need to be removed
        return res


c = Solution()
intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
# intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
# intervals = [[1, 2], [1, 2], [1, 2]]
# intervals = [[1, 2], [2, 3]]
print(c.eraseOverlapIntervals(intervals))
