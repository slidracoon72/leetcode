from typing import List


class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans = ""
        s = sorted(v)  # sorts in alphabetical order
        # print(s)
        first = s[0]
        last = s[-1]
        # print(min(len(first), len(last)))
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans


c = Solution()
l1 = ["flower", "flow", "flight"]
l2 = ["dog", "racecar", "car"]
print("Longest Prefix 1:", c.longestCommonPrefix(l1))
print("Longest Prefix 2:", c.longestCommonPrefix(l2))
