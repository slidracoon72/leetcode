# LC-1769 Minimum Number of Operations to Move All Balls to Each Box
from typing import List


# Neetcode: https://www.youtube.com/watch?v=ZmH3gHiIqfI
# Time: O(n), Space: O(1)
# Similar to ProductOfArrayExceptSelf.py
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)  # Get the total number of boxes
        answer = [0] * n  # Initialize the result list with zeros

        # Traverse from left to right
        moves, balls = 0, 0  # Initialize moves and balls counters
        for i in range(n):
            answer[i] = moves + balls  # Update the current position with cumulative moves
            moves = moves + balls  # Increment moves by the number of balls so far
            balls += int(boxes[i])  # Add the current box's ball count to balls (1 if box has a ball, 0 otherwise)

        # Traverse from right to left
        moves, balls = 0, 0  # Reset moves and balls counters for the right-to-left traversal
        for i in range(n - 1, -1, -1):
            answer[i] += moves + balls  # Add the cumulative moves from the right side
            moves = moves + balls  # Increment moves by the number of balls so far
            balls += int(boxes[i])  # Add the current box's ball count to balls

        return answer  # Return the result list containing minimum operations for each box


c = Solution()
boxes = "001011"
print(c.minOperations(boxes))
