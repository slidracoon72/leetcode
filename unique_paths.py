class Solution:
    # Neetcode solution : https://www.youtube.com/watch?v=IlEsdxuD4lY
    # Solving using Dynamic Programming
    # Time: O(m * n)
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow

        return row[0]


c = Solution()
m = 3
n = 7
print(c.uniquePaths(m, n))
