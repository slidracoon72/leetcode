from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> str:
        pointer1 = 0
        pointer2 = len(s) - 1
        while pointer1 < pointer2:
            s[pointer1], s[pointer2] = s[pointer2], s[pointer1]
            pointer1 += 1
            pointer2 -= 1

        return "".join(s)


c = Solution()
s1 = ["h", "e", "l", "l", "o"]
s2 = ["H", "a", "n", "n", "a", "h"]
print(c.reverseString(s1))
print(c.reverseString(s2))
