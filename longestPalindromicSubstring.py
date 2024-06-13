class Solution:
    # https://www.youtube.com/watch?v=XYQecbcd6_c
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # check all odd length substrings
            l, r, = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # check if length of new palindromic substring greater than current palindromic string
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # check all even length substrings
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # check if length of new palindromic substring greater than current palindromic string
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res


c = Solution()
s1 = "babad"
s2 = "cbbd"
print(c.longestPalindrome(s1))
print(c.longestPalindrome(s2))
