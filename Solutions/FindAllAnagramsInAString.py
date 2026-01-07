from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_map = [0] * 26
        p_map = [0] * 26

        for c in p:
            p_map[ord(c) - ord('a')] += 1

        res = []
        l = 0
        for r in range(len(s)):
            s_map[ord(s[r]) - ord('a')] += 1
            if (r - l + 1) == len(p):
                if s_map == p_map:
                    res.append(l)
                s_map[ord(s[l]) - ord('a')] -= 1
                l += 1
        return res


c = Solution()
s = "cbaebabacd"
p = "abc"
print(c.findAnagrams(s, p))
