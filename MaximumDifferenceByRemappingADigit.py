class Solution:
    # Time: O(n), Space: O(n)
    def minMaxDifference(self, num: int) -> int:
        # Convert the input number to a string for easy manipulation
        s = str(num)
        n = len(s)

        # Create a copy of the string to compute the minimum version later
        t = s

        pos = 0
        # Find the first digit from the left that is not '9'
        # This will be the digit to replace with '9' to get the maximum number
        while pos < n and s[pos] == '9':
            pos += 1

        # If there's a digit that is not '9', replace all of its occurrences with '9'
        if pos < n:
            s = s.replace(s[pos], '9')

        # Replace all occurrences of the first digit in the original number with '0'
        # to get the minimum possible number
        t = t.replace(t[0], '0')

        # Return the difference between the maximum and minimum values
        return int(s) - int(t)


c = Solution()
print(c.minMaxDifference(11891))
print(c.minMaxDifference(90))
