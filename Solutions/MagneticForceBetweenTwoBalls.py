from typing import List


# Solved using Binary Search
# Similar to KokoEatingBananas.py (Aggressive Cows on GeeksForGeeks)
class Solution:
    # Time: O(nlogn + nlogs); s = range from l to r, Space: O(1)
    def maxDistance(self, position: List[int], m: int) -> int:
        # Sort positions so we can greedily place balls left to right
        position.sort()

        # Define search space: min force is 1, max force is the largest gap
        l, r = 1, position[-1] - position[0]  # l=1 (smallest possible force), r=max gap (upper bound)

        # Initialize result to 0; we'll maximize it
        res = 0  # Start with 0; we'll maximize this

        # Binary search to find the maximum possible minimum force
        while l <= r:
            # Calculate mid-point force to test
            mid = l + (r - l) // 2  # mid is the candidate minimum magnetic force

            # Check if we can place all m balls with at least 'mid' spacing
            count = 1  # Always place the first ball at the first basket
            last = position[0]  # Track position of the last placed ball

            for i in range(1, len(position)):
                if position[i] - last >= mid:  # Far enough from last placed ball
                    count += 1  # Place a ball here
                    last = position[i]  # Update last placed position

            # Check if current force 'mid' is feasible
            if count >= m:  # If we managed to place all m balls
                res = max(res, mid)  # Update result with largest valid force
                l = mid + 1  # Try a larger force to maximize it
            else:  # If we couldn't place all m balls
                r = mid - 1  # Decrease force to fit more balls

        # Return the maximum minimum force found
        return res


c = Solution()
position = [1, 2, 3, 4, 7]
m = 3
# position = [5, 4, 3, 2, 1, 1000000000]
# m = 2
print(c.maxDistance(position, m))
