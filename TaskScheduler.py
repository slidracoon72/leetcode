import heapq
from collections import Counter, deque


# Neetcode: https://youtu.be/s8p8ukTyA2I
class Solution:
    # Time: O(m), Space: O(1) where m = no. of tasks
    def leastInterval(self, tasks, n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time


c = Solution()
tasks = ["A", "A", "A", "B", "C"]
n = 3

print(c.leastInterval(tasks, n))
