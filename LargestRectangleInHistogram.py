from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # Stack stores tuples of (index, height)

        # Iterate through each bar in the histogram
        for i, h in enumerate(heights):
            start = i  # Track the farthest left this bar can extend
            # If the current bar is shorter than the top of the stack,
            # pop from stack and calculate area
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Width = current index - index of last smaller height
                maxArea = max(maxArea, height * (i - index))
                start = index  # Update start to the index of the bar just popped
            # Push current bar with updated start index
            stack.append((start, h))

        # Process remaining bars in the stack
        for i, h in stack:
            # Width = total length - starting index
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea


c = Solution()
heights = [2, 1, 5, 6, 2, 3]
print(c.largestRectangleArea(heights))
