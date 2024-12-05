from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_map = [(i, arr[i]) for i in range(len(arr))]
        for i, v in arr_map:
            if 2 * v in arr and arr.index(2 * v) != i:
                return True
        return False


c = Solution()
arr = [10, 2, 5, 3]
print(c.checkIfExist(arr))
