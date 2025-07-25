from typing import List
from collections import deque


class Solution:
    # Solved using BFS - Level Order Traversal
    def openLock(self, deadends: List[str], target: str) -> int:
        # If "0000" is a deadend, we can't even start
        if "0000" in deadends:
            return -1

        # Helper function to generate all possible next states (children)
        def children(lock):
            res = []
            for i in range(4):
                # Turn the wheel one step forward
                digit = str((int(lock[i]) + 1) % 10)
                # Rebuild the string with the updated digit (strings are immutable)
                # Update ith value with the new digit
                res.append(lock[:i] + digit + lock[i + 1:])

                # Turn the wheel one step backward
                digit = str((int(lock[i]) - 1 + 10) % 10)  # 0 - 1 = -1 => - 1 + 10 = 9 => 9 % 10 = 9 Thus, 0 -> 9
                res.append(lock[:i] + digit + lock[i + 1:])
            return res

        # Initialize BFS queue with the starting lock state "0000" and 0 turns
        q = deque([("0000", 0)])

        # Set to track visited states and avoid revisiting deadends
        visit = set(deadends)

        # BFS loop
        while q:
            lock, turns = q.popleft()

            # If we reached the target lock combination, return the number of turns
            if lock == target:
                return turns

            # Explore all possible next combinations from current lock
            for child in children(lock):
                if child not in visit:
                    q.append((child, turns + 1))  # Add next state with incremented turn count
                    visit.add(child)  # Mark as visited to avoid cycles

        # If target was never reached
        return -1


c = Solution()
deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
print(c.openLock(deadends, target))
