import heapq
from collections import Counter, deque

# follow Neetcode
class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        count = Counter(tasks)
        print(count)
        maxHeap = [-cnt for cnt in count.values()]
        print(maxHeap)
        heapq.heapify(maxHeap)
        print(maxHeap)

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
tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
n = 2
print(c.leastInterval(tasks, n))
