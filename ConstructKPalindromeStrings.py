from collections import Counter


# Neetcode: https://www.youtube.com/watch?v=D00qGvqmqN0&ab_channel=NeetCodeIO
# Time: O(n), Space: O(n)
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # If k is greater than the length of the string, it's impossible to construct k palindromes
        # because we need at least one character per palindrome.
        if k > len(s):
            return False

        if len(s) == k:
            return True

        # Count the frequency of each character in the string.
        c = Counter(s)

        # Count the number of characters that have an odd frequency.
        # Each odd frequency requires a separate palindrome because palindromes can have at most one odd character.
        odd = 0
        for v in c.values():
            odd += v % 2

        # Return True if the number of odd frequencies is less than or equal to k.
        # This ensures we can use the remaining characters to construct the required palindromes.
        return odd <= k


c = Solution()
s = "annabelle"
k = 2
print(c.canConstruct(s, k))
