from collections import defaultdict
from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        arr_map = defaultdict(int)
        for i, val in nums1:
            arr_map[i] += val
        for i, val in nums2:
            arr_map[i] += val

        return sorted(arr_map.items())


c = Solution()
nums1 = [[1, 2], [2, 3], [4, 5]]
nums2 = [[1, 4], [3, 2], [4, 1]]
print(c.mergeArrays(nums1, nums2))
