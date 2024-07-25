class Solution:
    # Two-Pointer approach
    # Time Complexity: O(len(s) + len(t))
    # Space Complexity: O(1)
    # Neetcode: https://www.youtube.com/watch?v=gKDmO8ZLRD8

    def appendCharacters(self, s: str, t: str) -> int:
        # Initialize pointers for both strings s and t
        i, j = 0, 0

        # Traverse through both strings using the two pointers
        while i < len(s) and j < len(t):
            # If characters match, move both pointers
            if s[i] == t[j]:
                j += 1
            # If characters do not match, move pointer i of string s
            i += 1

        # The number of characters to be appended is the remaining length of t
        return len(t) - j

