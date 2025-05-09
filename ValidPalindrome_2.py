class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                # Either skip left or right
                skipL, skipR = s[l + 1: r + 1], s[l:r]
                return (skipL == skipL[::-1]) or (skipR == skipR[::-1])
            l, r = l + 1, r - 1

        return True


c = Solution()
s = "abca"
print(c.validPalindrome(s))
