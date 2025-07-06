from typing import List, Counter


class Solution:
    # Time: O(n), Space: O(n)
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        res = -1
        for key, freq in count.items():
            if key == freq:
                res = max(res, freq)
        return res


c = Solution()
arr = [1, 2, 2, 3, 3, 3]
print(c.findLucky(arr))
