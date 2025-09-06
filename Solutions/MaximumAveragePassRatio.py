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

    # Similar as above
    # Time: O(nlogn + klogn), Space: O(N)
    def maxAverageRatio1(self, classes: List[List[int]], extraStudents: int) -> float:
        # Function to calculate the *gain* in pass ratio
        # if we add one more passing student to a class
        def gain(p, t):
            return ((p + 1) / (t + 1)) - (p / t)

        # Max-heap (using negative values because Python heapq is a min-heap)
        # Each entry in heap = (-gain, p, t)
        maxHeap = []
        for p, t in classes:
            g = gain(p, t)  # initial gain for this class
            heapq.heappush(maxHeap, (-g, p, t))  # push negative gain for max-heap behavior

        # Distribute extra students to maximize overall average pass ratio
        for _ in range(extraStudents):
            current_gain, p, t = heapq.heappop(maxHeap)  # get class with max potential gain
            p += 1  # add one passing student
            t += 1  # total students increases as well
            current_gain = gain(p, t)  # recalculate new gain
            heapq.heappush(maxHeap, (-current_gain, p, t))  # push updated class back to heap

        # Calculate final average pass ratio
        total = 0
        n = len(classes)
        while maxHeap:
            _, p, t = heapq.heappop(maxHeap)
            total += p / t  # accumulate ratio of each class

        return total / n  # return average across all classes


c = Solution()
classes = [[1, 2], [3, 5], [2, 2]]
extraStudents = 2
print(c.maxAverageRatio(classes, extraStudents))
