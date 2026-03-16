# ASUS Singapore Question

import heapq
from typing import List


class Solution:
    def mergeKSortedLists(self, lists: List[List[int]]) -> List[int]:
        """
        Merge k sorted lists into one sorted list.

        Approach: Min-Heap (Priority Queue)
        - Push the first element of each list into a min-heap.
        - Each heap entry stores (value, list_index, element_index)
          so we can efficiently pull the next element from the same list.
        - Repeatedly pop the smallest element and push the next
          element from that list until the heap is empty.

        Time Complexity:  O(N log k)
            N = total number of elements across all lists
            k = number of lists
        Space Complexity: O(k) for the heap + O(N) for the output
        """
        result = []
        min_heap = []

        # Seed the heap with the first element of each non-empty list
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(min_heap, (lst[0], i, 0))  # (value, list_index, element_index)

        # Extract the minimum element and advance that list's pointer
        while min_heap:
            val, list_idx, elem_idx = heapq.heappop(min_heap)
            result.append(val)

            next_idx = elem_idx + 1
            if next_idx < len(lists[list_idx]):
                next_val = lists[list_idx][next_idx]
                heapq.heappush(min_heap, (next_val, list_idx, next_idx))

        return result


c = Solution()
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
print(c.mergeKSortedLists(lists))
