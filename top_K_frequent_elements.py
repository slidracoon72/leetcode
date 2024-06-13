import collections
from typing import List


# Time Complexity : O(n * log(n))
# Space Complexity : O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        s = dict(sorted(c.items(), key=lambda item: item[1], reverse=True))
        l = []
        for c in s:
            l.append(c)
        return l[:k]

    # Similar, but a bit optimized
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        c = dict(sorted(c.items(), key=lambda item: item[1], reverse=True))
        result = list(c.keys())[:k]
        return result


c = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(c.topKFrequent(nums, k))
