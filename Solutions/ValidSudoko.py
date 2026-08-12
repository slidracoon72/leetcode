from collections import defaultdict
from typing import List


# Neetcode: https://www.youtube.com/watch?v=TjFXEUCMqI8
#  Time and Space: O(N^2) = O(9^2)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)  # Key = ( r/3, c/3 )

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                        board[r][c] in cols[c] or
                        board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

    # Similar as above
    def isValidSudoku1(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                cur = board[r][c]
                if cur == ".":
                    continue

                if cur in rows[r] or cur in cols[c] or cur in square[(r // 3, c // 3)]:
                    return False

                rows[r].add(cur)
                cols[c].add(cur)
                square[(r // 3, c // 3)].add(cur)

        return True


board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

c = Solution()
print(c.isValidSudoku(board))
