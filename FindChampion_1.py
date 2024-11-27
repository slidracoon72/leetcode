from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        res = -1
        ind = -1
        for i, row in enumerate(grid):
            if sum(row) > res:
                res = sum(row)
                ind = i
        return ind


c = Solution()
grid = [[0, 0, 1], [1, 0, 1], [0, 0, 0]]
print(c.findChampion(grid))
