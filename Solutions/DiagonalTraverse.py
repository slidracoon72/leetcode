from typing import List


class Solution:
    # Time: O(m * n), Space: O(1)
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Step 1: Handle edge cases and initialize
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        r, c = 0, 0  # Start at top-left
        upward = True  # Direction: True = upward-right, False = downward-left

        # Step 2: Traverse until all elements are visited
        while len(result) < m * n:
            # Add current element
            result.append(mat[r][c])

            if upward:
                # Moving upward-right
                if r == 0 and c < n - 1:
                    c += 1  # Hit top, move right
                    upward = False
                elif c == n - 1:
                    r += 1  # Hit right, move down
                    upward = False
                else:
                    r -= 1
                    c += 1
            else:
                # Moving downward-left
                if r == m - 1 and c < n - 1:
                    c += 1  # Hit bottom, move right
                    upward = True
                elif c == 0:
                    r += 1  # Hit left, move down
                    upward = True
                else:
                    r += 1
                    c -= 1

        return result


c = Solution()
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat1 = [[1, 2], [3, 4]]
print(c.findDiagonalOrder(mat))
print(c.findDiagonalOrder(mat1))
