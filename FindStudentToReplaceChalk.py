# 1894. Find the Student that Will Replace the Chalk
from typing import List


class Solution:
    # Getting TLE as using while loop for each round
    # Simulating all the rounds
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)

        i = 0
        while k >= 0:
            i = i % n
            if chalk[i] > k:
                return i
            k -= chalk[i]
            i += 1

    # Time: O(N), Space: O(1)
    # Simulating only the last round
    def chalkReplacer1(self, chalk: List[int], k: int) -> int:
        # Step 1: Calculate the total chalk usage in one complete round
        total_chalk = sum(chalk)

        # Step 2: Reduce k by the total chalk to handle full rounds
        k %= total_chalk

        # Step 3: Find the first student who can't complete their task
        for i, chalk_needed in enumerate(chalk):
            if k < chalk_needed:
                return i
            k -= chalk_needed
