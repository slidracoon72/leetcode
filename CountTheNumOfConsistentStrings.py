from typing import List


class Solution:
    # Time: O(n*m), Space: O(1)
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        allowed = set(allowed)
        for x in words:
            l = 0
            for c in x:
                if c not in allowed:
                    break
                else:
                    l += 1

            if l == len(x):
                res += 1

        return res

    # Similar Solution
    def countConsistentStrings1(self, allowed: str, words: List[str]) -> int:
        res = len(words)
        allowed = set(allowed)
        for x in words:
            for c in x:
                if c not in allowed:
                    res -= 1
                    break

        return res

    # Using Bit-Mask
    # Neetcode: https://www.youtube.com/watch?v=CFa2TgIHMN0
    def countConsistentStrings2(self, allowed: str, words: List[str]) -> int:
        # Initialize a bitmask for the allowed characters
        # The bitmask will be a 26-bit integer representing which characters (a-z) are allowed
        bit_mask = 0

        # For each character in the 'allowed' string, we update the bitmask
        for c in allowed:
            # ord(c) - ord('a') gives the position of the character in the alphabet (0 for 'a', 1 for 'b', etc.)
            # 1 << (ord(c) - ord('a')) creates a bit with 1 in the position corresponding to the character's place in the alphabet
            bit = 1 << (ord(c) - ord('a'))

            # Combine the current bit with the bitmask using the bitwise OR operation.
            # This sets the corresponding bit in the bitmask to 1, indicating that this character is allowed.
            bit_mask = bit_mask | bit

        # Initialize the result with the total number of words
        res = len(words)

        # For each word in the list of words, we check if all its characters are allowed
        for w in words:
            # Check each character in the word
            for c in w:
                # Create a bit for the current character in the same way we did for the allowed characters
                bit = 1 << (ord(c) - ord('a'))

                # Perform a bitwise AND between the character's bit and the allowed bitmask.
                # If the result is 0, the character is not in the allowed set, meaning the word is inconsistent.
                if bit & bit_mask == 0:
                    # If an inconsistent character is found, decrease the result count by 1
                    res -= 1
                    # Break out of the loop as we no longer need to check the rest of the characters in the word
                    break

        # Return the final count of consistent strings
        return res
