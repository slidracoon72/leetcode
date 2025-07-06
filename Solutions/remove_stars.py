class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == '*':
                stack.pop()
            else:
                stack.append(c)

        return str.join("", stack)


c = Solution()
s1 = "leet**cod*e"
s2 = "erase*****"
print(c.removeStars(s1))
print(c.removeStars(s2))
print(c.removeStars(s1))
