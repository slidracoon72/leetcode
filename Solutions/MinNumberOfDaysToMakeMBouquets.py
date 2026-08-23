from typing import List


# Solved using Binary Search
class Solution:
    # Time: O(nlogd); d = range from l to r, Space: O(1)
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # If we don't even have enough flowers to make m bouquets of k
        # flowers each, it's impossible no matter how long we wait
        if m * k > len(bloomDay):
            return -1

        # Define search space: min day is the earliest bloom, max day is the latest bloom
        l, r = min(bloomDay), max(bloomDay)  # l=min(bloomDay) (smallest possible answer), r=max(bloomDay) (upper bound)

        # Initialize result to the maximum possible day
        res = r  # Start with max value; we'll minimize it

        # Binary search to find the minimum day we can make m bouquets
        while l <= r:
            # Calculate mid-point day to test
            day = l + (r - l) // 2  # day is the candidate "wait until this day" value

            # Check how many bouquets we can make if we wait until 'day'
            bouquets = 0  # Total bouquets made so far
            adjacent = 0  # Count of consecutive bloomed flowers (streak)

            for bloom in bloomDay:
                if bloom <= day:  # Flower has bloomed by 'day'
                    adjacent += 1  # Extend the current streak
                    if adjacent == k:  # Streak long enough for a bouquet
                        bouquets += 1  # Make a bouquet
                        adjacent = 0  # Reset streak, flowers are used up
                else:  # Flower hasn't bloomed yet, streak breaks
                    adjacent = 0  # Reset streak

            # Check if current day is feasible
            if bouquets >= m:  # If we can make at least m bouquets by 'day'
                res = min(res, day)  # Update result with smallest valid day
                r = day - 1  # Try an earlier day to minimize it
            else:  # If we can't make enough bouquets by 'day'
                l = day + 1  # Wait longer

        # Return the minimum day found
        return res


c = Solution()
bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 1
# bloomDay = [1, 10, 3, 10, 2]
# m = 3
# k = 2
# bloomDay = [7, 7, 7, 7, 12, 7, 7]
# m = 2
# k = 3
print(c.minDays(bloomDay, m, k))
7852