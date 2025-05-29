from collections import defaultdict
from typing import List


# Techdose: https://www.youtube.com/watch?v=8MJXe4YMtng&ab_channel=Techdose
class Solution:
    # Using Hash-Set
    # Time: O(n), Space: O(n)
    def longestPalindrome(self, words: List[str]) -> int:
        d = defaultdict(int)  # Dictionary to store word frequencies
        res = 0  # Length of the palindrome

        for word in words:
            pal = word[::-1]  # Reverse of the word

            if pal in d:  # If reverse exists, form a pair
                res += 4  # Add 4 characters (word + reverse)
                d[pal] -= 1  # Decrease reverse count
                if d[pal] == 0:
                    del d[pal]  # Remove if count is 0
            else:
                d[word] += 1  # Add word to dictionary

        # Check for any palindrome word (e.g., "aa") to place in the middle
        for word in d:
            if word == word[::-1]:
                res += 2  # Add 2 characters for one palindrome word
                break  # Only one middle word is needed

        return res

    # Using Matrix to keep track of count of palindromes
    # Time: O(n), Space: O(1) as we use matrix of fixed size
    def longestPalindrome1(self, words: List[str]) -> int:
        freq = [[0] * 26 for _ in range(26)]
        palindrome_count = 0
        mid_count = 0

        for word in words:
            a = ord(word[0]) - ord('a')
            b = ord(word[1]) - ord('a')

            # check for (a,b) if palindrome (b,a) exists
            if freq[b][a] > 0:
                palindrome_count += 4
                freq[b][a] -= 1
                if a == b:
                    mid_count -= 1
            else:
                freq[a][b] += 1
                if a == b:
                    mid_count += 1

        if mid_count > 0:
            palindrome_count += 2

        return palindrome_count


c = Solution()
words1 = ["lc", "cl", "gg"]
print(c.longestPalindrome(words1))
words2 = ["ab", "ty", "yt", "lc", "cl", "ab"]
print(c.longestPalindrome1(words2))
