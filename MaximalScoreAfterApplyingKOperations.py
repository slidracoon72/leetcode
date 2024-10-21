import heapq
from math import ceil
from typing import List


class Solution:
    # Solving the problem using a Max-Heap
    # Time: O(nlogn + klogn), Space: O(n)
    def maxKelements(self, nums: List[int], k: int) -> int:
        # Create a max-heap (in Python, heapq provides a min-heap by default,
        # so we push negative values to simulate a max-heap)
        max_heap = []
        for n in nums:
            # Push the negative value of each element into the heap to create a max-heap
            heapq.heappush(max_heap, -1 * n)

        score = 0  # Initialize the score to 0

        # Perform exactly k operations
        for i in range(k):
            # Pop the largest element from the heap (which is the most negative number, so multiply by -1)
            temp = -1 * heapq.heappop(max_heap)

            # Add the value of the popped element to the score
            score += temp

            # Push back the updated value (ceil of temp divided by 3) into the heap
            # Again, we push the negative of the result to maintain the max-heap property
            heapq.heappush(max_heap, -1 * (ceil(temp / 3)))

        # Return the final score after k operations
        return score

    # Similar - Using Heapify
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)

        score = 0
        for i in range(k):
            temp = -1 * heapq.heappop(max_heap)
            score += temp
            heapq.heappush(max_heap, -1 * (ceil(temp / 3)))

        return score
