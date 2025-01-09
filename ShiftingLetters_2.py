from collections import defaultdict
from typing import List


class Solution:
    # Brute Force - Update each substring (Gives TLE)
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        alphabets = defaultdict(int)
        ind_map = defaultdict(str)
        for i in range(26):
            alphabets[chr(ord('a') + i)] = i
            ind_map[i] = chr(ord('a') + i)

        s = list(s)
        for start, end, direction in shifts:
            d = -1 if direction == 0 else 1
            temp = ""
            for i, c in enumerate(s[start:end + 1]):
                next_char = ind_map[(alphabets[c] + d) % 26]
                temp += next_char
            s[start:end + 1] = temp
        return "".join(s)

    # Optimal Solution - LC Editorial
    # Solved using Difference Array - https://www.youtube.com/watch?v=96RG7EBF8LI&ab_channel=TLEEliminators-byPriyansh
    # Time: O(n+m), Space: O(n) where n = len(s), m = len(shifts)
    def shiftingLetters1(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        diff_array = [0] * n  # Initialize a difference array with all elements set to 0

        # Process each shift operation
        for start, end, shift in shifts:
            if shift == 1:  # If direction is forward (1)
                diff_array[start] += 1  # Increment at the start index
                if end + 1 < n:
                    diff_array[end + 1] -= 1  # Decrement at the end+1 index
            else:  # If direction is backward (0)
                diff_array[start] -= 1  # Decrement at the start index
                if end + 1 < n:
                    diff_array[end + 1] += 1  # Increment at the end+1 index

        result = list(s)
        number_of_shifts = 0

        # Apply the shifts to the string
        for i in range(n):
            # Update cumulative shifts, keeping within the alphabet range
            number_of_shifts += diff_array[i] % 26
            if number_of_shifts < 0:
                number_of_shifts += 26  # Ensure non-negative shifts

            # Calculate the new character by shifting `s[i]`
            shifted_char = chr((ord(s[i]) - ord("a") + number_of_shifts) % 26 + ord("a"))
            result[i] = shifted_char

        return "".join(result)


c = Solution()
s = "abxka"
shifts = [[2, 3, 1], [0, 2, 0], [1, 4, 0]]
print(c.shiftingLetters1(s, shifts))
