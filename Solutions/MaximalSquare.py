# Google Interview Question

from typing import List


class Solution:
    # Top-Down Recursion with Memoization
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        cache = {}
        self.max_side = 0

        # Time: O(m*n), Space: O(m*n)
        def helper(r, c):
            if r >= row or c >= col:
                return 0

            if (r, c) not in cache:
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diag = helper(r + 1, c + 1)

                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, diag, right)
                    self.max_side = max(self.max_side, cache[(r, c)])

            return cache[(r, c)]

        helper(0, 0)
        return self.max_side ** 2
