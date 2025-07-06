from typing import List


class Solution:
    # Time: O(m*n), Space: O(m*n)
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        unguarded = (m * n) - len(guards) - len(walls)
        matrix = [[0] * n for _ in range(m)]  # 0: unguarded, "G": guard, "W": wall, 1: guarded

        # Mark guards and walls on the matrix
        for r, c in guards:
            matrix[r][c] = "G"
        for r, c in walls:
            matrix[r][c] = "W"

        # Directions for the guards' vision (north, south, east, west)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Propagate guard visibility
        for r, c in guards:
            for dr, dc in directions:
                row, col = r + dr, c + dc
                # Traverse in the current direction until hitting a wall, guard, or boundary
                while 0 <= row < m and 0 <= col < n:
                    if matrix[row][col] in ("G", "W"):  # Stop at guard or wall
                        break
                    if matrix[row][col] == 0:  # Mark as guarded if unoccupied
                        matrix[row][col] = 1
                        unguarded -= 1
                    row += dr
                    col += dc

        return unguarded
