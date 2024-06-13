from typing import List


class Solution:
    def insertNeetcode(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # overlapping
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)
        return res

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
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
intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
print(c.insert(intervals, newInterval))
print(c.insertNeetcode(intervals, newInterval))
