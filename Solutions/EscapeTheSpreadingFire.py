# LC - Hard
# DO AGAIN

from collections import deque
from math import inf
from typing import List


class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # Record the arrival time OverflowError() fire
        fire = [[inf] * n for _ in range(m)]
        # BFS to find time fire reach each cell
        queue_fire = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue_fire.append((i, j))
        time = 0
        while queue_fire:
            for _ in range(len(queue_fire)):
                i, j = queue_fire.popleft()
                fire[i][j] = time
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_i, new_j = i + di, j + dj
                    if (
                            0 <= new_i < m
                            and 0 <= new_j < n
                            and grid[new_i][new_j] == 0
                            and fire[new_i][new_j] == inf
                    ):
                        queue_fire.append((new_i, new_j))
            time += 1
        fire[m - 1][n - 1] += 1

        queue = deque([(0, 0, fire[0][0] - 1)])  # i, j, max_wait_time
        time = 0
        visited = set((0, 0))
        res = []
        while queue:
            for _ in range(len(queue)):
                i, j, bonus_time = queue.popleft()
                if bonus_time >= 0:
                    # Reached safehouse
                    if i == m - 1 and j == n - 1:
                        res.append(bonus_time)
                        continue

                    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        new_i, new_j = i + di, j + dj
                        if (
                                0 <= new_i < m
                                and 0 <= new_j < n
                                and grid[new_i][new_j] == 0
                                and (new_i, new_j) not in visited
                        ):
                            # There could be 2 paths arriving at the safehouse at the same time, we want to consider both of them.
                            if not (new_i == m - 1 and new_j == n - 1):
                                visited.add((new_i, new_j))
                            queue.append(
                                (
                                    new_i,
                                    new_j,
                                    min(
                                        bonus_time, fire[new_i][new_j] - (time + 1) - 1
                                    ),
                                )
                            )
            time += 1
        if not res:
            return -1
        if max(res) == inf:
            return 10 ** 9
        return max(res)


grid = [
    [0, 0, 0, 2, 0, 2, 0, 0, 0],
    [0, 2, 0, 0, 2, 0, 2, 0, 0],
    [0, 0, 2, 0, 0, 2, 0, 0, 0],
    [0, 1, 2, 2, 0, 0, 0, 0, 0],
    [1, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 2, 0, 0, 0, 0, 2],
    [0, 2, 0, 1, 2, 0, 0, 0, 0]
]
c = Solution()
print(c.maximumMinutes(grid))
