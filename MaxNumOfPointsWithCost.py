from typing import List


class Solution:
    # My Solution
    # Passes 91/157 testcases
    def maxPoints1(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        coords = []
        for r in range(rows):
            i, j = r, 0
            cur_max = points[i][j]
            for c in range(1, cols):
                if points[r][c] >= cur_max:
                    cur_max = points[r][c]
                    i, j = r, c
            coords.append([cur_max, i, j])

        res, i, j = coords[0]
        for c in range(1, len(coords)):
            r_max, row, col = coords[c]
            res += r_max - abs(j - col)
            j = col
        return res

    # Solved using Dynamic Programming - Top-Down Approach
    # Neetcode: https://www.youtube.com/watch?v=ik1y7fz8AOc
    # Time: O(m * n), Space: O(n)
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])

        # Initialize the first row as the starting points
        prev_row = points[0]

        # Iterate through each row starting from the second row
        for r in range(1, rows):
            # Make a copy of the current row points
            next_row = points[r].copy()

            # Arrays to store max values when moving left to right and right to left
            left, right = [0] * cols, [0] * cols

            # Fill the left array - max points attainable moving left to right
            left[0] = prev_row[0]
            for c in range(1, cols):
                # Take the maximum of the current column value and the previous column minus the penalty
                left[c] = max(prev_row[c], left[c - 1] - 1)

            # Fill the right array - max points attainable moving right to left
            right[cols - 1] = prev_row[cols - 1]
            for c in range(cols - 2, -1, -1):
                # Take the maximum of the current column value and the next column minus the penalty
                right[c] = max(prev_row[c], right[c + 1] - 1)

            # Update the current row with the maximum of either moving from the left or right
            for c in range(cols):
                next_row[c] += max(left[c], right[c])

            # Move to the next row by setting the current row as the previous row
            prev_row = next_row

        # The maximum points will be the maximum value in the last processed row
        return max(prev_row)


c = Solution()
# points = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
points = [[1, 5], [2, 3], [4, 2]]
print(c.maxPoints(points))
