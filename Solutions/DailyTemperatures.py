from typing import List


# A "monotonic stack" is a stack data structure where the elements are maintained in a specific order,
# either strictly increasing or strictly decreasing. The main idea is to ensure that each element in
# the stack has a specific relationship (either always greater or always lesser) with its neighbors.
# This property makes monotonic stacks particularly useful for solving problems that involve finding
# the next greater or smaller element in a sequence, such as the "daily temperatures" problem.

# Types of Monotonic Stacks:
# Monotonically Increasing Stack: Each element is less than or equal to the element above it.
# Monotonically Decreasing Stack: Each element is greater than or equal to the element above it.


# Monotonic Stack (Decreasing)
# Time and Space Complexity: O(n)
# Neetcode: https://www.youtube.com/watch?v=cTBiBSnjO3c
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize the result array with all 0's
        res = [0] * len(temperatures)

        # Stack to keep track of temperatures and their indices
        stack = []  # Each element in stack is a pair [temperature, index]

        # Iterate over the list of temperatures
        for i, t in enumerate(temperatures):
            # While the stack is not empty and the current temperature is greater than the
            # temperature at the top of the stack, it means we have found a warmer day
            while stack and t > stack[-1][0]:
                prevTemp, prevInd = stack.pop()  # Get the previous temperature and index
                res[prevInd] = i - prevInd  # Calculate the number of days and update result
            # Push the current temperature and its index onto the stack
            stack.append([t, i])

        # Return the result array containing the number of days to wait for a warmer temperature
        return res


c = Solution()
temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]
temperatures2 = [30, 38, 30, 36, 35, 40, 28]
print(c.dailyTemperatures(temperatures1))
print(c.dailyTemperatures(temperatures2))
