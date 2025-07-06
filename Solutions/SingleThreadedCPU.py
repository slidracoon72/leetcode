import heapq
from typing import List


class Solution:
    # Solved using Min-Heap
    # Time: O(nlogn), Space: O(n)
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Min-heap for tasks not yet available to process, ordered by enqueue time
        pending = []
        # Min-heap for tasks ready to be processed, ordered by processing time and index
        available = []

        # Push all tasks into the pending heap with structure: (enqueueTime, processingTime, index)
        for i, (enqueueTime, processingTime) in enumerate(tasks):
            heapq.heappush(pending, (enqueueTime, processingTime, i))

        time = 0  # Current time
        res = []  # Result list to store the order of task execution

        # Continue processing while there are tasks left in either heap
        while pending or available:
            # Move all tasks whose enqueue time <= current time from pending to available
            while pending and pending[0][0] <= time:
                _, processingTime, i = heapq.heappop(pending)
                heapq.heappush(available, (processingTime, i))

            # If no task is currently available, jump time to the next task's enqueue time
            if not available:
                time = pending[0][0]
                continue

            # Pop the task with the shortest processing time (and smallest index if tied)
            processingTime, i = heapq.heappop(available)
            time += processingTime  # Advance current time by the task's processing time
            res.append(i)  # Append task index to result

        return res  # Return the execution order of tasks


c = Solution()
tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]
print(c.getOrder(tasks))
