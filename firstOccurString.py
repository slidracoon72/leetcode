class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):

            # this is an abstracted code
            if haystack[i:i + len(needle)] == needle:
                return i

            #  this does the same thing as above
            # for j in range(len(needle)):
            #     if haystack[i + j] != needle[j]:
            #         break
            #     if j == len(needle) - 1:
            #         return i
        return -1


c = Solution()
print(c.strStr("sadbutsad", "sad"))
print(c.strStr("leetcode", "leeto"))
print(c.strStr("walgreen", "green"))
