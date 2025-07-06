from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        j = 0  # pointer for spaces

        l = 0
        for r in range(len(s)):
            if r == spaces[j]:
                res.append(s[l:r])
                j += 1
                l = r
            if j == len(spaces):
                res.append(s[l:])
                break

        return " ".join(res)


c = Solution()
s = "LeetcodeHelpsMeLearn"
spaces = [8, 13, 15]
print(c.addSpaces(s, spaces))
