class Solution:
    # Neetcode: https://www.youtube.com/watch?v=-VVN0FI0KFo
    # Time: O(n), Space: O(1)
    def minimumSteps(self, s: str) -> int:
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] == "0":
                res += r - l
                l += 1
        return res
