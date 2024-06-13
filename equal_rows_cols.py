class Solution:
    def equalPairs(self, grid) -> int:
        cols = list()
        n = len(grid)
        for i in range(n):
            for j in range(n):
                cols.append(grid[j][i])

        list_of_cols = [cols[i:i + n] for i in range(0, len(cols), n)]

        c = 0
        for x in grid:
            for y in list_of_cols:
                if x == y:
                    c += 1
        return c


a = Solution()
grid1 = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
grid2 = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
grid3 = [[3, 1, 2, 2], [1, 4, 4, 4], [2, 4, 2, 2], [2, 5, 2, 2]]
print(a.equalPairs(grid3))
print(a.equalPairs(grid2))
print(a.equalPairs(grid1))
