from typing import List


# Neetcode: https://www.youtube.com/watch?v=LVBDzeUmNIQ
# Time: O(nlogn), Space: O(1)
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Sort the list of time points lexicographically (which works for "HH:MM" format)
        timePoints.sort()

        # Helper function to convert time in "HH:MM" format to total minutes
        def time_to_min(time):
            h, m = map(int, time.split(":"))
            return h * 60 + m  # Convert hours to minutes and add minutes

        # Initialize res with the time difference between the last and the first time points,
        # accounting for the circular nature of the clock (i.e., wrapping around 24 hours).
        # Example:
        # timePoints = ["23:50", "00:10"]
        # time_to_min("23:50") = 1430 minutes
        # time_to_min("00:10") = 10 minutes
        # 24 * 60 = 1440 minutes (1 day)
        # res = 1440 - 1430 + 10 = 20 minutes (the difference when wrapping from "23:50" to "00:10")
        res = 24 * 60 - time_to_min(timePoints[-1]) + time_to_min(timePoints[0])

        # Loop through sorted time points to find the minimum time difference
        for i in range(len(timePoints) - 1):
            cur = time_to_min(timePoints[i + 1])  # Convert current time point to minutes
            prev = time_to_min(timePoints[i])  # Convert previous time point to minutes
            diff = cur - prev  # Calculate the time difference between consecutive points
            res = min(res, diff)  # Update res if the current difference is smaller
            if res == 0:  # If the minimum possible difference is found, return 0 immediately
                return 0

        return res  # Return the minimum time difference found

    # res = 24 * 60 - time_to_min(timePoints[-1]) + time_to_min(timePoints[0])
    # Lets say sorted array in hours = [2, 3, 4]
    # For loop will find 3-2, 4-3 but diff b/w 2(current day) and 4(prev day) has to be calculated.
    # The diff b/w 4 of previous day and 2 of current day is 12 - 4 + 2 = 10 hours

    # Using Bucket Sort
    def findMinDifference1(self, timePoints: List[str]) -> int:
        # Helper function to convert time in "HH:MM" format to total minutes
        def time_to_min(time):
            h, m = map(int, time.split(":"))
            return h * 60 + m  # Convert hours to minutes and add minutes

        exists = [False] * (60 * 24)
        first_m, last_m = 60 * 24, 0
        for t in timePoints:
            m = time_to_min(t)
            if exists[m]:
                return 0
            exists[m] = True
            first_m = min(first_m, m)
            last_m = max(last_m, m)

        res = 60 * 24 - last_m + first_m
        prev_m = first_m
        for m in range(first_m + 1, len(exists)):
            if exists[m]:
                diff = m - prev_m
                res = min(res, diff)
                prev_m = m

        return res
