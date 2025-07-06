# LC-1718: Construct the Lexicographically Largest Valid Sequence
from typing import List


class Solution:
    # Using Backtracking (Recursion)
    # Time: O(n!), Space: O(n)
    def constructDistancedSequence(self, n: int) -> List[int]:
        # Initialize the result sequence with size 2*n-1 filled with 0s
        # Each number from 1 to n should appear twice, except 1 which appears once
        res = [0] * (2 * n - 1)
        used = set()  # Set to track numbers that have been placed

        def backtrack(i):  # 'i' is the pointer to the 'res' array
            if i == len(res):  # If we have filled the entire array, return True (solution found)
                return True

            for num in reversed(range(1, n + 1)):  # Iterate from n to 1 (lexicographically largest first)
                # If the number is already used, skip it
                if num in used:
                    continue
                # If num > 1, it needs to be placed twice. Check if the second position is valid and not set.
                if num > 1 and (i + num >= len(res) or res[i + num] > 0):
                    continue

                # Place the number in the sequence
                res[i] = num
                used.add(num)
                if num > 1:
                    res[i + num] = num  # Place the second occurrence

                # Move to the next empty position
                j = i + 1
                while j < len(res) and res[j] > 0:
                    j += 1

                # Recursively attempt to fill the rest with the sequence
                if backtrack(j):
                    return True  # If a valid sequence is found, return True

                # Backtrack: Undo the decision
                res[i] = 0
                used.remove(num)
                if num > 1:
                    res[i + num] = 0  # Remove the second occurrence

            return False  # If no valid placement found, backtrack

        backtrack(0)  # Start backtracking from the first position
        return res  # Return the filled sequence


c = Solution()
print(c.constructDistancedSequence(3))
print(c.constructDistancedSequence(5))
