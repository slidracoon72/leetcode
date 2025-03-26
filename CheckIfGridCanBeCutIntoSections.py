from typing import List


class Solution:
    # Interval Problem - Similar to CountDaysWithoutMeetings.py
    # Neetcode: https://www.youtube.com/watch?v=X9QtxzsAsYo&ab_channel=NeetCodeIO
    # Time: O(nlogn), Space: O(n)
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # Extract x-coordinates (left and right) of rectangles
        x = [(r[0], r[2]) for r in rectangles]  # (x1, x2) = (left, right)
        # Extract y-coordinates (bottom and top) of rectangles
        y = [(r[1], r[3]) for r in rectangles]  # (y1, y2) = (bottom, top)

        # Sort the intervals based on starting points
        x.sort()
        y.sort()

        # Function to count non-overlapping intervals
        def count_non_overlapping(intervals) -> int:
            count = 0  # Counter for non-overlapping segments
            prev_end = -1  # Tracks the end of the last added segment

            for start, end in intervals:
                # If the start of the current segment is beyond or at the end of the last added segment
                if start >= prev_end:
                    count += 1  # Increment count for a new non-overlapping segment
                # Update the latest end encountered so far
                prev_end = max(prev_end, end)

            return count  # Return the number of non-overlapping segments

        # Check if the maximum number of non-overlapping intervals in x or y directions is at least 3
        return max(count_non_overlapping(x), count_non_overlapping(y)) >= 3


c = Solution()
n = 5
rectangles = [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]
print(c.checkValidCuts(n, rectangles))
