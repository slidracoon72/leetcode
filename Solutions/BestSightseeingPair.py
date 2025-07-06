from typing import List


class Solution:
    # Brute Force - O(n^2)
    # Passes 45/55 Test cases
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = 0
        for i in range(len(values) - 1):
            for j in range(i + 1, len(values)):
                res = max(res, values[i] + values[j] + i - j)
        return res

    # Neetcode: https://www.youtube.com/watch?v=YAYnMfHbjz4&ab_channel=NeetCodeIO
    # Dynamic Programming
    # Time: O(n), Space: O(1)
    def maxScoreSightseeingPair1(self, values: List[int]) -> int:
        # Initialize the result to store the maximum score found so far
        res = 0
        # `cur_max` represents the maximum value of (values[i] + i) we've seen so far,
        # adjusted for the next iteration by subtracting 1 for distance.
        cur_max = values[0] - 1

        # Iterate through the array starting from the second element
        for j in range(1, len(values)):
            # Update the result with the maximum score using the current value at `j`
            # and the best `cur_max` seen so far
            res = max(res, cur_max + values[j])
            # Update `cur_max` for the next iteration
            # Include the current value adjusted for its index, minus 1 for the distance
            cur_max = max(cur_max, values[j]) - 1

        # Return the maximum score found
        return res

    # Similar Approach - Dynamic Programming
    # Time: O(n), Space: O(1)
    def maxScoreSightseeingPair2(self, values):
        n = len(values)

        # The left score is initially just the value of the first element.
        max_left_score = values[0]

        max_score = 0

        for i in range(1, n):
            current_right_score = values[i] - i
            # Update the maximum score by combining the best left score so far with the current right score.
            max_score = max(max_score, max_left_score + current_right_score)

            current_left_score = values[i] + i
            # Update the maximum left score up to the current index.
            max_left_score = max(max_left_score, current_left_score)

        return max_score
