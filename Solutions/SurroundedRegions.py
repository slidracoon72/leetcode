from typing import List


# Facebook Interview Question
# Graph - DFS (using "Reverse Thinking")
# Neetcode: https://www.youtube.com/watch?v=9z2BunfoZ5Y
# Time Complexity: O(m*n)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        def capture_dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture_dfs(r + 1, c)
            capture_dfs(r - 1, c)
            capture_dfs(r, c + 1)
            capture_dfs(r, c - 1)

        # Phase 1
        # Scan border region for O (O -> T)
        # Capture un-surrounded regions
        for r in range(ROWS):
            for c in range(COLS):
                if (r in [0, ROWS - 1]) or (c in [0, COLS - 1]):
                    if board[r][c] == "O":
                        capture_dfs(r, c)

        # Phase 2
        # Capture surrounded region (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # Phase 3
        # Un-capture un-surrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
