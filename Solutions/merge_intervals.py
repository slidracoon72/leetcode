from typing import List

# O(n log n) - Neetcode: https://www.youtube.com/watch?v=44H3cEC2fFM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sorting by start value
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            # if overlapping, update the interval
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            # if not overlapping, directly add the interval
            else:
                output.append([start, end])

        return output


c = Solution()
intervals = [[1, 3], [2, 6], [5, 10], [15, 18]]
print(c.merge(intervals))
