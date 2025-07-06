# Sliding Window Approach
# Neetcode: https://www.youtube.com/watch?v=QzcxeJZByNM&ab_channel=NeetCodeIO Ï
# Time:O(N) Space:O(1)
class Solution:
    # Solving using the invert technique. The goal is to find the maximum window in the middle
    # such that the count of "a", "b", "c" on the left and right sides remains >= k.
    def takeCharacters(self, s: str, k: int) -> int:
        # Step 1: Get the total count of each character ('a', 'b', 'c') in the string.
        count = [0, 0, 0]  # Initialize count array for 'a', 'b', and 'c'.
        for x in s:
            count[ord(x) - ord('a')] += 1  # Map 'a', 'b', 'c' to indices 0, 1, 2 and increment count.

        # Step 2: Check if it's possible to take at least 'k' of each character.
        if min(count) < k:
            return -1  # If any character occurs fewer than 'k' times, return -1 as it's not possible.

        # Step 3: Use a sliding window to calculate the minimum substring removal.
        res = float('inf')  # Initialize the result with infinity (to find the minimum value).
        l = 0  # Left pointer of the sliding window.

        for r in range(len(s)):  # Iterate through the string with the right pointer.
            # Since the character at index 'r' is now inside the window, decrement its outside count.
            count[ord(s[r]) - ord('a')] -= 1

            # Adjust the window by moving the left pointer to ensure the counts outside the window remain >= k.
            while min(count) < k:  # If any count outside the window drops below 'k':
                count[ord(s[l]) - ord('a')] += 1  # Increment the outside count for the leftmost character.
                l += 1  # Shrink the window by moving the left pointer.

            # Update the result by minimizing the length of the string to remove.
            # The length to remove is the total string length minus the current window size.
            res = min(res, len(s) - (r - l + 1))

        # Step 4: Return the minimum substring removal length.
        return res


c = Solution()
s = "aabaaaacaabc"
k = 2
print(c.takeCharacters(s, k))
