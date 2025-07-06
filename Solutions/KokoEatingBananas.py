import math
from typing import List


# Neetcode: https://www.youtube.com/watch?v=U2SozAs9RzA
# Solved using Binary Search
class Solution:
    # Time: O(nlogs); s = range from l to r, Space: O(1)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Define search space: min rate is 1, max rate is the largest pile
        l, r = 1, max(piles)  # l=1 (smallest possible rate), r=max(piles) (upper bound)

        # Initialize result to the maximum possible rate
        res = r  # Start with max value; we'll minimize it

        # Binary search to find the minimum eating speed
        while l <= r:
            # Calculate mid-point rate to test
            k = (l + r) // 2  # k is the eating speed (bananas per hour)

            # Compute total hours needed to eat all piles at rate k
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)  # Hours per pile = ceil(pile size / rate)

            # Check if current rate k is feasible
            if hours <= h:  # If hours are within limit h
                res = min(res, k)  # Update result with smallest valid rate
                r = k - 1  # Try a smaller rate to minimize k
            else:  # If hours exceed h
                l = k + 1  # Increase rate to finish faster

        # Return the minimum eating speed found
        return res


c = Solution()
piles = [3, 6, 7, 11]
h = 8
# # piles = [30, 11, 23, 4, 20]
# # h = 5
# piles = [30, 11, 23, 4, 20]
# h = 6
print(c.minEatingSpeed(piles, h))
