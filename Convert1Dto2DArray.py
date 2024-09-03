# 2022. Convert 1D Array Into 2D Array
from typing import List


class Solution:
    # My Solution
    # Time: O(m*n), Space: O(m*n)
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []

        res = [[0] * n for _ in range(m)]
        i = 0
        for r in range(m):
            for c in range(n):
                res[r][c] = original[i]
                i += 1
        return res

    # Neetcode: https://www.youtube.com/watch?v=l-VLzZ2riTc
    # Time: O(m*n), Space: O(m*n)
    def construct2DArray1(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []

        res = []

        for r in range(m):
            start = r * n
            end = start + n
            res.append(original[start:end])

        return res


c = Solution()
original = [1, 2, 3, 4]
m = 2
n = 2
print(c.construct2DArray(original, m, n))
print(c.construct2DArray1(original, m, n))
