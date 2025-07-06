from collections import deque
from typing import List


class Solution:
    # Solved using BFS
    # Neetcode: https://www.youtube.com/watch?v=6lH4nO3JfLk&ab_channel=NeetCode
    # Time: O(n*n), Space: O(n*n)
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()  # Reverse board to make row 0 the bottom row

        # Convert a square number (1 to n^2) to board coordinates [r, c]
        def intToPos(square):
            r = (square - 1) // n
            c = (square - 1) % n
            if r % 2:  # For odd rows, reverse column direction (right to left)
                c = n - 1 - c
            return [r, c]

        q = deque()
        q.append([1, 0])  # [square, moves] - start at square 1 with 0 moves
        visit = set()
        visit.add(1)  # Mark square 1 as visited

        while q:
            square, moves = q.popleft()

            # Try all possible die rolls (1 to 6)
            for i in range(1, 7):
                nextSquare = square + i
                # Skip if nextSquare exceeds the target (n^2)
                if nextSquare > n * n:
                    continue

                r, c = intToPos(nextSquare)
                # Check if there's a snake or ladder at this position, then make the hop again
                if board[r][c] != -1:
                    nextSquare = board[r][c]

                # If we've reached the target square, return the number of moves
                if nextSquare == n * n:
                    return moves + 1

                # If the square hasn't been visited, add it to the queue
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, moves + 1])

        return -1  # Return -1 if no path to n^2 is found


c = Solution()
board = [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1],
         [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]
print(c.snakesAndLadders(board))
