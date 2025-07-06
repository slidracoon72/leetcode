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

    # Similar as above
    def reverseString1(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


c = Solution()
s1 = ["h", "e", "l", "l", "o"]
s2 = ["H", "a", "n", "n", "a", "h"]
print(c.reverseString(s1))
print(c.reverseString(s2))
