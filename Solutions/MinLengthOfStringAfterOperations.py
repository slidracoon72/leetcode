from collections import Counter


class Solution:
    # Solved in a similar approach to UniqueLength-3PalindromicSubsequences.py
    # Time: O(n), Space: O(n)
    def minimumLength(self, s: str) -> int:
        # Initialize a counter for characters on the right side of the current position
        right = Counter(s)

        # Set to track characters encountered so far on the left side
        left = set()

        # Variable to track the total number of characters removed
        removed = 0

        # Iterate through the string
        for i, char in enumerate(s):
            # Decrease the count of the current character in the right counter
            right[char] -= 1

            # Check if the current character can act as the center for removal
            if char in left and right[char] > 0:
                # If the character exists both on the left and right, remove two characters
                removed += 2
                # Remove the most recent occurrence of the character from the left set
                left.remove(char)
            else:
                # Add the character to the left set
                left.add(char)

        # The minimum length of the string is the original length minus the removed characters
        return len(s) - removed

    # LC Editorial Solution - Similar approach
    # Time: O(n), Space: O(n)
    def minimumLength1(self, s: str) -> int:
        # Step 1: Count the frequency of each character in the string
        char_frequency_map = Counter(s)

        # Step 2: Calculate the number of characters to delete
        delete_count = 0
        for frequency in char_frequency_map.values():
            if frequency % 2 == 1:
                # If frequency is odd, delete all except one
                delete_count += frequency - 1
            else:
                # If frequency is even, delete all except two
                delete_count += frequency - 2

        # Step 3: Return the minimum length after deletions
        return len(s) - delete_count


c = Solution()
s = "abaacbcbb"
print(c.minimumLength(s))
print(c.minimumLength1(s))
