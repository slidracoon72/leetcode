class Solution:
    def reverseWords(self, s: str) -> str:
        s = (s.strip()).split(" ")
        l = []

        for x in s:
            if x:
                l.append(x)

        rev = ""
        for i in range(len(l) - 1, -1, -1):
            rev += l[i] + " "

        return rev.strip()


# a = "a good   example"
a = "  hello world  "
# a = "the sky is blue"
c = Solution()
print(c.reverseWords(a))
