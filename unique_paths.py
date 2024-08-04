class Solution:
    # Neetcode solution : https://www.youtube.com/watch?v=IlEsdxuD4lY
    # Solving using Dynamic Programming: Bottom-Up
    # Time: O(m * n), Space: O(n)
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize last row as all 1's
        row = [1] * n

        # Traverse from second last row till first row
        # Last row and col will always be 1 as from them, we can only go down and right respectively
        for i in range(m - 1):
            # Initialize new row
            newRow = [1] * n

            # Start from second last column
            for j in range(n - 2, -1, -1):
                # Current value is sum of right and bottom elements
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow

        return row[0]


c = Solution()
m = 3
n = 7
print(c.uniquePaths(m, n))
