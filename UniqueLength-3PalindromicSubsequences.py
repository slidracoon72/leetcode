from collections import Counter


# Neetcode: https://www.youtube.com/watch?v=2JG5rLM3vz8&ab_channel=NeetCodeIO
# Time: O(n), Space: O(n)
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # A palindrome of length 3 consists of identical outer characters and any middle character (eg. "aba")
        # Set to store unique palindromic subsequences (middle_char, outer_char)
        res = set()

        # Set to track characters encountered so far on the left of the current position
        left = set()

        # Counter to track the frequency of characters to the right of the current position
        right = Counter(s)

        # Iterate through each character in the string, treating it as the potential middle character
        for mid in s:
            # Decrease the count of the current middle character in the right tracker
            right[mid] -= 1

            # Check all characters in the left set to see if they can form a palindrome
            for c in left:
                # If the character also exists on the right, it can form a palindrome
                if right[c]:
                    # Add the (middle_char, outer_char) pair to the result set
                    res.add((mid, c))

            # Add the current middle character to the left set
            left.add(mid)

        # The number of unique palindromic subsequences is the size of the result set
        return len(res)


c = Solution()
s1 = "aabca"
s2 = "adc"
s3 = "bbcbaba"
strings = [s1, s2, s3]

for i in range(len(strings)):
    print(c.countPalindromicSubsequence(strings[i]))
