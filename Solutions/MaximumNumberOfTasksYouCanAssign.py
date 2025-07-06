# LC - Hard
# DO AGAIN

from collections import deque
from typing import List


class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        n, m = len(tasks), len(workers)
        left, right = 0, min(n, m)

        def check(x: int) -> bool:
            task_ptr = 0
            q = deque()
            p = pills
            # Iterate over the x strongest workers (sorted ascending, take last x)
            for worker in workers[m - x:]:
                # Add all tasks that can be handled by this worker with a pill
                while task_ptr < x and tasks[task_ptr] <= worker + strength:
                    q.append(tasks[task_ptr])
                    task_ptr += 1
                # Assign the smallest task without pill if possible
                if q and q[0] <= worker:
                    q.popleft()
                else:
                    # Use a pill to take the largest possible task
                    if p > 0 and q:
                        p -= 1
                        q.pop()
                    else:
                        return False
            return True

        # Binary search for the maximum feasible tasks
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left
