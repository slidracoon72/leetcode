# LC - Hard
from typing import List


# Neetcode: https://www.youtube.com/watch?v=1IzCRCcK17A
# Time Complexity: O(n) where n is the length of the ratings array (two passes through the array)
# Space Complexity: O(n) due to the additional array 'arr' used to store the candy count for each student
class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = len(ratings)
        # Initialize an array to store the number of candies each student should receive, starting with 1 candy each
        arr = [1] * l

        # First pass: left to right
        # Purpose: Ensure that any student with a higher rating than their left neighbor gets more candies
        # Skip the first value since it does not have a left neighbor
        for i in range(1, l):
            if ratings[i] > ratings[i - 1]:  # If the current student has a higher rating than the one on the left
                arr[i] = arr[i - 1] + 1  # Give them one more candy than the left neighbor

        # Second pass: right to left
        # Purpose: Ensure that any student with a higher rating than their right neighbor gets more candies
        # Skip the last value since it does not have a right neighbor
        for i in range(l - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:  # If the current student has a higher rating than the one on the right
                # Ensure that the current student has the maximum required candies (considering both left and right passes)
                arr[i] = max(arr[i], arr[i + 1] + 1)

        # The total number of candies needed is the sum of the values in the 'arr' array
        return sum(arr)


c = Solution()
ratings = [1, 0, 2]
print(c.candy(ratings))
