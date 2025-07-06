from collections import deque
from typing import List


class Solution:
    # Solved using BFS
    # Time: O(rows * cols), Space: O(rows * cols)
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])

        # Initialize highest peak array
        res = [[-1] * cols for _ in range(rows)]
        q = deque()

        # Mark starting points (water cells) for BFS
        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    q.append((r, c, 0))  # row, col, peak_height
                    res[r][c] = 0
        # BFS
        while q:
            qLen = len(q)
            for _ in range(qLen):
                r, c, peak = q.popleft()
                neighbors = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]
                for nr, nc in neighbors:
                    if nr < 0 or nr == rows or nc < 0 or nc == cols or res[nr][nc] != -1:
                        continue
                    q.append((nr, nc, peak + 1))
                    res[nr][nc] = peak + 1

        return res


c = Solution()
isWater = [[0, 0, 1], [1, 0, 0], [0, 0, 0]]
print(c.highestPeak(isWater))
