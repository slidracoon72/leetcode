from collections import defaultdict
from typing import List

# Neetcode: https://www.youtube.com/watch?v=MsdLjL87BEo&ab_channel=NeetCodeIO
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # Initialize a dictionary to count occurrences of each unique row pattern
        count = defaultdict(int)

        # Iterate through each row in the matrix
        for row in matrix:
            # Convert the row into a tuple to use as a key in the dictionary
            row_key = tuple(row)

            # Check if the row starts with "1"
            # If it does, create a flipped version of the row where 1 becomes 0 and 0 becomes 1
            if row[0]:
                row_key = tuple([0 if n else 1 for n in row])

            # Increment the count for the current (or flipped) row pattern
            count[row_key] += 1

        # Return the maximum value from the count dictionary,
        # which represents the highest number of rows that can become identical after flipping
        return max(count.values())
