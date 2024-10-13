# LC - Hard

import heapq
from typing import List


class Solution:
    # Neetcode: https://www.youtube.com/watch?v=L_0aPFMgGpU
    # Function to find the smallest range that includes at least one number from each of the k sorted lists
    # Time: O(n*logk), Space: O(k)
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Get the number of lists
        k = len(nums)

        # Initialize the left and right bounds of the current smallest range
        left = right = nums[0][0]  # Start with the first element of the first list

        # Create a min-heap to keep track of the minimum element across all lists
        min_heap = []

        # Initialize the range and populate the heap with the first element of each list
        for i in range(k):
            l = nums[i]
            left = min(left, l[0])  # Find the minimum value to start the left bound
            right = max(right, l[0])  # Find the maximum value to start the right bound
            # Push the first element of each list along with the list index (i) and the element index (0)
            heapq.heappush(min_heap, (l[0], i, 0))  # (element, list index, element index)

        # Set the initial result range to [left, right]
        res = [left, right]

        # Iterate through the heap until we exhaust one of the lists
        while True:
            # Pop the smallest element from the heap
            n, i, idx = heapq.heappop(min_heap)
            # Move to the next element in the list from which the element was popped
            idx += 1
            # If we've reached the end of one list, return the current best range since one list is exhausted
            if idx == len(nums[i]):
                return res

            # Get the next value from the list and push it into the heap
            next_val = nums[i][idx]
            heapq.heappush(min_heap, (next_val, i, idx))

            # Update the left bound to the minimum value in the heap (smallest element across all lists)
            left = min_heap[0][0]
            # Update the right bound to the maximum value encountered so far
            right = max(right, next_val)

            # Check if the current range is smaller than the previous best range
            if right - left < res[1] - res[0]:
                # Update the result range if the current range is smaller
                res = [left, right]
