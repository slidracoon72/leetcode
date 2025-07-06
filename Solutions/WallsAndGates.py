from collections import deque
from typing import List


# Neetcode: https://www.youtube.com/watch?v=e69C6xhiSQE
# Solving using Multi-Source BFS - Simultaneous Tracking
# Similar to Rotten Oranges problem
# Time: O(rows * cols)
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        visit = set()
        q = deque()

        # helper function
        def addRoom(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in visit or rooms[r][c] == -1:
                return
            visit.add((r, c))
            q.append([r, c])

        # add gates to queue and visit set
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        # find min distance from gate to neighbors
        dist = 0
        while q:
            # BFS level traversal
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            # Level ends, increase distance
            dist += 1


c = Solution()
rooms = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1],
         [0, -1, 2147483647, 2147483647]]
print(c.wallsAndGates(rooms))
