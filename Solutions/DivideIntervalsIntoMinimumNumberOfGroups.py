from typing import List


class Solution:
    # Solve by finding the maximum number of overlapping intervals (groups needed)
    # Neetcode: https://www.youtube.com/watch?v=FVjKrhdMutc
    # Time: O(nlogn), Space: O(n)
    def minGroups(self, intervals: List[List[int]]) -> int:
        # Separate the start and end times from the intervals
        start, end = [], []
        for s, e in intervals:
            start.append(s)  # Collect start times
            end.append(e)  # Collect end times

        # Sort the start and end times separately
        start.sort()  # Sort the start times in ascending order
        end.sort()  # Sort the end times in ascending order

        # Initialize variables:
        # 'groups' will track the number of overlapping intervals at any time
        # 'res' will store the maximum number of overlapping intervals found (i.e., the result)
        groups, res = 0, 0

        # i is for iterating over start times, j is for iterating over end times
        i, j = 0, 0

        # Loop through the intervals based on the start times
        while i < len(intervals):
            # If the current start time is less than or equal to the current end time
            if start[i] <= end[j]:
                groups += 1  # Increment the count of overlapping intervals (a new group starts)
                i += 1  # Move to the next start time
            else:
                groups -= 1  # An interval ends, so decrement the count of overlapping intervals
                j += 1  # Move to the next end time

            # Update the result with the maximum number of overlapping intervals seen so far
            res = max(res, groups)

        # Return the maximum number of overlapping intervals (i.e., minimum groups needed)
        return res

    # Similar - Without using "groups" variable
    def minGroups1(self, intervals: List[List[int]]) -> int:
        start, end = [], []
        for s, e in intervals:
            start.append(s)
            end.append(e)

        start.sort()
        end.sort()

        res = 0
        i, j = 0, 0
        while i < len(intervals):
            if start[i] <= end[j]:
                i += 1
            else:
                j += 1
            res = max(res, i - j)

        return res
