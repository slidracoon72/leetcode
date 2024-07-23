from collections import defaultdict
from typing import List


# Time: O(n + nlogn), Space: O(n)
# Neetcode: # https://www.youtube.com/watch?v=OPvcR1e4lfg
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_set = set(arr2)  # for faster lookup O(1)
        arr1_count = defaultdict(int)
        end = []  # to store values not in arr2

        for n in arr1:
            if n not in arr2_set:
                end.append(n)
            arr1_count[n] += 1
        end.sort()

        res = []
        for n in arr2:
            for _ in range(arr1_count[n]):
                res.append(n)

        return res + end


c = Solution()
arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
print(c.relativeSortArray(arr1, arr2))
