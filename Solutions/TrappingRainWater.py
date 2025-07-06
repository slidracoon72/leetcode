# LC - Hard

from typing import List


class Solution:
    # Optimal
    # Memory: O(N)
    def trap1(self, height: List[int]) -> int:
        # Check if the height list is empty
        if not height:
            return 0

        n = len(height)
        # Initialize arrays to store the maximum height to the left and right of each bar
        maxLeft = [0] * n
        maxRight = [0] * n

        # Calculate the maximum height to the left of each bar
        maxLeft[0] = 0  # Leftmost bar has no elements to its left, so initialize as 0
        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i - 1], height[i - 1])

        # Calculate the maximum height to the right of each bar
        maxRight[n - 1] = 0  # Rightmost bar has no elements to its right, so initialize as 0
        for i in range(n - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i + 1])

        water = 0
        # Calculate the amount of water trapped between each bar
        for i in range(n):
            # Calculate the minimum height between the maximum heights to the left and right of the current bar
            minHeight = min(maxLeft[i], maxRight[i]) - height[i]
            # If the minimum height is positive, add it to the total water trapped
            if minHeight > 0:
                water += minHeight

        return water

    # Most optimal solution - Using Two-Pointers
    # Memory Complexity: O(1) (Constant - as no data structure used)
    # Neetcode: https://www.youtube.com/watch?v=ZI2z5pq0TqA
    def trap2(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        water = 0

        # We look for max-left or max-right encountered so far, including the current value
        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                water += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                water += maxRight - height[r]

        return water

    # Not optimal
    def trap(self, height: List[int]) -> int:
        water = 0
        for i, h in enumerate(height):
            maxLeft = max(height[:i]) if i > 0 else 0
            maxRight = max(height[i + 1:]) if i < len(height) - 1 else 0
            x = min(maxLeft, maxRight)
            minHeight = x - h
            if minHeight > 0:
                water += minHeight
        return water


c = Solution()
height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
print(c.trap2(height))
