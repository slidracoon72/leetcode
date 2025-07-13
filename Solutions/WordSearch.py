from typing import List


class Solution:
    # Time: O(m * 4^n), Space: O(n); where m is the number of cells in the board and n is the length of the word
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])  # Get the dimensions of the board
        path = set()  # Keep track of the cells visited in the current path to avoid revisiting

        # DFS function to explore all possible paths for the word starting from (r, c)
        def dfs(r, c, i):
            # If we've matched all characters in the word
            if i == len(word):
                return True

            # Check boundaries, character match, and if the cell has already been visited
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                    word[i] != board[r][c] or (r, c) in path):
                return False

            path.add((r, c))  # Mark the current cell as visited

            # Explore all 4 directions: down, up, right, left
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            path.remove((r, c))  # Backtrack: unmark the current cell
            return res

        # Try to start the DFS from every cell in the board
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):  # If DFS finds the word, return True
                    return True

        return False  # If no path matches the word, return False


c = Solution()
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(c.exist(board, word))
