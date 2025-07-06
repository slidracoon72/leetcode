# Sliding Window
# Neetcode: https://www.youtube.com/watch?v=gqXU1UyA8pk
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Dictionary to keep track of the frequency of each character in the current window
        count = dict()
        # Variable to store the maximum length of the substring found
        res = 0
        # Left pointer for the sliding window
        l = 0

        # Iterate through the string with the right pointer
        for r in range(len(s)):
            # Update the count for the current character
            count[s[r]] = 1 + count.get(s[r], 0)

            # Check if the current window is valid, i.e., we can turn the substring into
            # one with the same characters with at most k changes.
            # (r - l + 1) is the length of the current window.
            # max(count.values()) is the count of the most frequent character in the current window.
            # (r - l + 1) - max(count.values()) gives the number of changes needed to make
            # all characters in the window the same.
            while (r - l + 1) - max(count.values()) > k:
                # If the window is not valid, shrink it from the left
                count[s[l]] -= 1  # Decrease the count of the leftmost character
                l += 1  # Move the left pointer to the right

            # Update the result with the maximum length of valid windows found so far
            res = max(res, r - l + 1)

        # Return the maximum length of the substring found
        return res


c = Solution()
s = "ABAB"
k = 2
print(c.characterReplacement(s, k))
