import heapq
from typing import List


class Solution:
    # Using Min-Heap
    # Time: O(nlogn), Space: O(n)
    def findScore(self, nums: List[int]) -> int:
        heap = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(heap)
        marked = set()
        score = 0

        while heap:
            n, i = heapq.heappop(heap)
            # Skip if already marked
            if i in marked:
                continue

            # Add the value of the chosen integer to the score
            score += n
            marked.add(i)

            # Mark neighbors
            if i - 1 >= 0:
                marked.add(i - 1)
            if i + 1 < len(nums):
                marked.add(i + 1)

        return score

    # Using Sorted List - Similar approach as above (More efficient)
    # Time: O(nlogn), Space: O(n)
    def findScore1(self, nums: List[int]) -> int:
        # Create a list of (value, index) pairs and sort by value, then by index
        indexed_nums = sorted((val, idx) for idx, val in enumerate(nums))
        marked = set()  # Set to track marked elements
        score = 0

        for value, index in indexed_nums:
            if index not in marked:  # If the current element is not marked
                score += value  # Add its value to the score
                marked.add(index)  # Mark the current element
                if index + 1 < len(nums):
                    marked.add(index + 1)
                if index - 1 >= 0:
                    marked.add(index - 1)
        return score
