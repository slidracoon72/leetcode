# 2914. Minimum Number of Changes to Make Binary String Beautiful
class Solution:
    # Checking substrings of even length
    # Time: O(n), Space: O(1)
    def minChanges(self, s: str) -> int:
        res = 0  # Initialize the result to count the number of changes
        l = 0  # Initialize the left pointer

        # Iterate through the string using the right pointer
        for r in range(len(s)):
            # Check if the characters at the left and right pointers are different
            if s[l] != s[r]:
                # If the current substring length (r + 1) is even
                if (r + 1) % 2 == 0:
                    res += 1  # Increment the count for required changes
                l = r  # Move the left pointer to the current position of the right pointer

        return res  # Return the total number of changes needed

    # Checking pairs of length = 2
    # Time: O(n), Space: O(1)
    def minChanges1(self, s: str) -> int:
        res = 0  # Initialize a counter to keep track of the number of changes required

        # Loop through the string in steps of 2, as we are checking pairs of characters
        for i in range(0, len(s) - 1, 2):
            # Check if the current pair of characters are different
            if s[i] != s[i + 1]:
                res += 1  # Increment the counter if the pair is different

        return res  # Return the total number of changes needed


c = Solution()
s = "00101100"
print(c.minChanges(s))
print(c.minChanges1(s))
