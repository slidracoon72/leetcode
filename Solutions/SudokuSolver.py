# LC - Hard

from collections import defaultdict
from typing import List


class Solution:
    # Solves the Sudoku puzzle in-place using backtracking.
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Use dictionaries of sets to keep track of numbers
        # already present in each row, column, and 3x3 square.
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)  # Key: (row//3, col//3)

        # Pre-populate sets with the existing numbers on the board.
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != ".":  # If the cell is not empty
                    rows[r].add(val)
                    cols[c].add(val)
                    squares[(r // 3, c // 3)].add(val)

        # Backtracking DFS function
        def dfs(r, c):
            # If we reach end of a row, move to next row
            if c == 9:
                return dfs(r + 1, 0)
            # If we reach past last row, board is solved
            if r == 9:
                return True

            # Skip already filled cells
            if board[r][c] != ".":
                return dfs(r, c + 1)

            # Try placing digits 1–9 in the current cell
            for i in range(1, 10):
                i = str(i)
                # Check if 'i' is valid (not in same row, col, or 3x3 square)
                if i not in rows[r] and i not in cols[c] and i not in squares[(r // 3, c // 3)]:
                    # Place the digit tentatively
                    board[r][c] = i
                    rows[r].add(i)
                    cols[c].add(i)
                    squares[(r // 3, c // 3)].add(i)

                    # Recursively solve next cell
                    if dfs(r, c + 1):
                        return True

                    # Backtrack: undo the placement
                    board[r][c] = "."
                    rows[r].remove(i)
                    cols[c].remove(i)
                    squares[(r // 3, c // 3)].remove(i)

            # If no valid digit works, trigger backtracking
            return False

        # Start solving from top-left cell
        dfs(0, 0)
        # return board


c = Solution()
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(c.solveSudoku(board))
