from typing import List


# Solved using Difference Array technique - Efficient for range-based updates
# Difference Array Tutorial: https://www.youtube.com/watch?v=96RG7EBF8LI&ab_channel=TLEEliminators-byPriyansh
# Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        diff_arr = [0] * n  # Initialize the difference array to track cumulative shifts

        # Build the difference array using the shifts input
        for i in range(n):
            start, end = 0, i  # Each shift starts from index 0 and ends at index i
            diff_arr[start] += shifts[end]  # Increment at the start of the range
            if end + 1 < n:  # Ensure end+1 is within bounds before decrementing
                diff_arr[end + 1] -= shifts[end]

        # Initialize the result array as a list of characters from the input string
        res = list(s)
        cumulative_shift = 0  # Tracks the cumulative shift while traversing the string - similar to taking prefix-sum

        # Apply the shifts and calculate the resultant characters
        for i, (c, d) in enumerate(zip(res, diff_arr)):
            cumulative_shift += d % 26  # Update the cumulative shift (mod 26 to wrap around) (take prefix sum)
            if cumulative_shift < 0:  # Ensure the shift is non-negative
                cumulative_shift += 26

            # Calculate the new character after applying the cumulative shift
            next_char = chr((ord(c) - ord('a') + cumulative_shift) % 26 + ord('a'))
            res[i] = next_char  # Update the result with the new character

        return "".join(res)  # Join the result list into a string and return


c = Solution()
s = "abc"
shifts = [3, 5, 9]
print(c.shiftingLetters(s, shifts))
