from typing import List


class Solution:
    # Greedy
    # Time: O(n), Space: O(n)
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [n - 1]
        maxRight = heights[n - 1]

        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > maxRight:
                res.append(i)
                maxRight = heights[i]

        return res[::-1]

    # Monotonic Stack - Decreasing
    # Time: O(n), Space: O(n)
    def findBuildings1(self, heights: List[int]) -> List[int]:
        stack = []

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] <= h:
                stack.pop()
            stack.append(i)

        return stack


c = Solution()
heights = [4, 2, 3, 2, 1]
print(c.findBuildings(heights))
print(c.findBuildings1(heights))
