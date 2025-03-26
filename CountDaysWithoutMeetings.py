from typing import List


class Solution:
    # Solved using Difference Array Technique - Gives MLE
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        res = 0
        diff_arr = [0] * (days + 1)  # expensive to store as days can be 10**9

        for s, e in meetings:
            diff_arr[s] += 1
            if e + 1 < days + 1:
                diff_arr[e + 1] -= 1

        for i in range(1, len(diff_arr)):
            diff_arr[i] += diff_arr[i - 1]  # calculate prefix sum array
            if diff_arr[i] == 0:
                res += 1

        return res

    # Solved using Hash-Set - Gives TLE
    def countDays1(self, days: int, meetings: List[List[int]]) -> int:
        res = 0
        used = set()
        for s, e in meetings:
            for i in range(s, e + 1):
                used.add(i)

        for i in range(1, days + 1):
            if i not in used:
                res += 1

        return res

    # Optimal - Using Intervals
    # Time: O(nlogn) - for sorting, Space: O(1)
    # Neetcode: https://www.youtube.com/watch?v=VFYTULYpApM&ab_channel=NeetCodeIO
    def countDays2(self, days: int, meetings: List[List[int]]) -> int:
        # Sort the meetings by start time to process them in chronological order
        meetings.sort()
        prev_end = 0  # Tracks the end of the last processed meeting

        for start, end in meetings:
            # Ensure we start counting only from after the last processed meeting
            start = max(start, prev_end + 1)

            # Calculate the number of days occupied by the current meeting
            length = end - start + 1

            # Reduce the available days by the number of occupied days
            days -= max(length, 0)

            # Update the last processed meeting's end day
            prev_end = max(prev_end, end)

        # Remaining free days after processing all meetings
        return days


c = Solution()
days = 10
meetings = [[5, 7], [1, 3], [9, 10]]
print(c.countDays2(days, meetings))
