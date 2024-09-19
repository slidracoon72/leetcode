from typing import List


class Solution:
    # Neetcode: https://www.youtube.com/watch?v=BJnMZNwUk1M
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        res = []
        top, left = 0, 0
        bottom, right = len(matrix), len(matrix[0])

        while left < right and top < bottom:

            # get every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # get every i in right column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            # if only one row/column exist
            if not (left < right and top < bottom):
                break

            # get every i in bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # get every i in left column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
c = Solution()
print(c.spiralOrder(matrix))
