import collections
from typing import List

# DO AGAIN
# Gives TLE - 90 / 162 testcases passed
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def island_count(grid):
            if not grid:
                return 0
            rows, cols = len(grid), len(grid[0])
            visit = set()
            islands = 0

            def bfs(r, c):
                q = collections.deque()
                q.append((r, c))
                visit.add((r, c))

                while q:
                    row, col = q.popleft()
                    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                    for dr, dc in directions:
                        new_r, new_c = row + dr, col + dc
                        if (new_r in range(rows) and
                                new_c in range(cols) and
                                grid[new_r][new_c] == 1 and
                                (new_r, new_c) not in visit):
                            q.append((new_r, new_c))
                            visit.add((new_r, new_c))

            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1 and (r, c) not in visit:
                        bfs(r, c)
                        islands += 1

            return islands

        matrix = [[0] * n for _ in range(m)]
        answer = [0] * len(positions)

        i = 0
        for r, c in positions:
            matrix[r][c] = 1
            answer[i] = island_count(matrix)
            i += 1
        return answer
