from typing import List


class Solution:
    # Time: O(n^2), Space: O(n^2)
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        res = [0, 0]
        seen = set()

        # Find repeated value
        for r in range(n):
            for c in range(n):
                if grid[r][c] in seen:
                    res[0] = grid[r][c]
                seen.add(grid[r][c])

        # Find missing value
        for x in range(1, n ** 2 + 1):
            if x not in seen:
                res[1] = x
                break

        return res


c = Solution()
grid = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
print(c.findMissingAndRepeatedValues(grid))
