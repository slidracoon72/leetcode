from typing import List


# Time: O(M*N), Space: O(M*N)
# Solving using DFS (reverse thinking - moving from water to land, not land to water)
# Applying DFS from border cells and moving inwards, therefore, we check that
# current height is greater than or equal to previous height
# Neetcode: https://www.youtube.com/watch?v=s-VkcjHqkGI
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            # Check false conditions
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
                    (r, c) in visit or heights[r][c] < prevHeight):
                return

            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Traversing upper and lower rows
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        # Traversing left and right cols
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # Loop entire matrix to find common cells
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res


c = Solution()
heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
print(c.pacificAtlantic(heights))
