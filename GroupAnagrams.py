from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())


c = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(c.groupAnagrams(strs))
