from collections import defaultdict


# Neetcode: https://www.youtube.com/watch?v=_g9jrLuAphs
class Solution:
    # Solved using HashMap (dictionary)
    def longestPalindrome(self, s: str) -> int:
        # Dictionary to count occurrences of each character in the string
        count = defaultdict(int)
        # Variable to keep track of the length of the longest palindrome
        res = 0

        # Count each character's occurrences in the string
        for c in s:
            count[c] += 1
            # If the count of the character is even, it can be fully used in the palindrome
            # Add 2 to the result for each pair of characters
            if count[c] % 2 == 0:
                res += 2

        # Check if there is at least one character with an odd count
        # A palindrome can have at most one character with an odd count in the center
        for val in count.values():
            if val % 2 == 1:
                res += 1  # Add one character with an odd count to the center of the palindrome
                break  # Only one odd character is needed, break after finding it

        return res

    # Solved using HashSet (more efficient)
    def longestPalindrome1(self, s: str) -> int:
        # Initialize a set to track characters
        seen = set()
        # Variable to keep track of the length of the longest palindrome
        res = 0

        # Iterate through each character in the string
        for c in s:
            if c in seen:
                # If the character is already in the set, it means we have encountered it again
                # This means we have a pair, so we remove it from the set and add 2 to the result
                seen.remove(c)
                res += 2
            else:
                # If the character is not in the set, add it to the set
                seen.add(c)

        # After processing all characters, check if there are any characters left in the set
        # This indicates that there are characters with an odd count
        # A palindrome can have at most one character with an odd count in the center
        if seen:
            res += 1  # Add one character with an odd count to the center of the palindrome

        return res


c = Solution()
s = "abccccdd"
print(c.longestPalindrome(s))  # Output: 7

s = "ccc"
print(c.longestPalindrome1(s))  # Output: 3
