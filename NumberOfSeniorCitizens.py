from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for d in details:
            if int(d[11:13]) > 60:
                res += 1
        return res


c = Solution()
details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
print(c.countSeniors(details))
