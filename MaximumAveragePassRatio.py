import heapq
from typing import List


class Solution:
    # Using Max-Heap. Take the class which gives the max gain in ratio upon adding a student.
    # Time: O(nlogn + klogn), Space: O(N)
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Calculate the gain when adding one student
        def gain(p, total):
            return (p + 1) / (total + 1) - p / total

        # Create a max-heap with negative gains (Python heap is min-heap by default)
        maxHeap = [(-gain(p, total), p, total) for p, total in classes]
        heapq.heapify(maxHeap)

        # Assign extra students
        for _ in range(extraStudents):
            current_gain, p, total = heapq.heappop(maxHeap)
            p += 1
            total += 1
            heapq.heappush(maxHeap, (-gain(p, total), p, total))

        # Calculate the total average pass ratio
        total_ratio = sum(p / total for _, p, total in maxHeap)
        return total_ratio / len(classes)


c = Solution()
classes = [[1, 2], [3, 5], [2, 2]]
extraStudents = 2
print(c.maxAverageRatio(classes, extraStudents))
