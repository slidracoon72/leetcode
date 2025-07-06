# LC-1358 - Number of Substrings Containing All Three Characters
from collections import defaultdict


class Solution:
    # Using Sliding Window
    def numberOfSubstrings(self, s: str) -> int:
        chars = defaultdict(int)  # Dictionary to store character counts in the current window
        res = 0  # Stores the total count of valid substrings
        l = 0  # Left pointer for the sliding window

        # Iterate through the string with the right pointer
        for r in range(len(s)):
            chars[s[r]] += 1  # Add the current character to the window

            # If the window contains all three characters ('a', 'b', 'c')
            while len(chars) == 3:
                res += len(s) - r  # Count all substrings that start from index 'l' and extend to the end

                # Shrink the window from the left
                chars[s[l]] -= 1
                if chars[s[l]] <= 0:  # If the count of a character becomes zero, remove it from the dictionary
                    del chars[s[l]]
                l += 1  # Move the left pointer forward

        return res  # Return the total count of valid substrings


c = Solution()
s = "abcabc"
print(c.numberOfSubstrings(s))
