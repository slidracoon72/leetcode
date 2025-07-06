class Solution:

    # solving using two-pointer (Neetcode)
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        return True if i == len(s) else False


c = Solution()
s = "axe"
t = "ahbgdc"
print(c.isSubsequence(s, t))
