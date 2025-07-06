# LC Hard
from collections import deque
from typing import List


class Solution:
    # Solving using BFS
    # Neetcode: https://www.youtube.com/watch?v=C8wonkVDWz8&ab_channel=NeetCodeIO
    # Time: O(6!), Space: O(6!)
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # adjacent indices of each index in a (2 * 3) matrix
        adj = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        # convert 'board' matrix to its string representation
        b = "".join([str(c) for row in board for c in row])

        q = deque([(b.index("0"), b, 0)])  # i (index of 0), board, length
        visit = {b}

        while q:
            i, b, length = q.popleft()

            if b == "123450":
                return length

            b_arr = list(b)
            for j in adj[i]:
                new_b_arr = b_arr.copy()
                new_b_arr[i], new_b_arr[j] = b_arr[j], b_arr[i]
                new_b = "".join(new_b_arr)

                if new_b not in visit:
                    visit.add(new_b)
                    q.append((j, new_b, length + 1))

        return -1


c = Solution()
board = [[4, 1, 2], [5, 0, 3]]
print(c.slidingPuzzle(board))
