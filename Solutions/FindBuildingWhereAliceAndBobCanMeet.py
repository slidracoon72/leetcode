# LC - Hard
import heapq
from collections import defaultdict
from typing import List


# Neetcode: https://www.youtube.com/watch?v=HJaSuUOUH90&ab_channel=NeetCodeIO
class Solution:
    # Brute Force (Passes 944/952 Test Cases)
    # Time: O(q*n), Space: O(q)
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # Initialize the result array with -1 for each query
        # This will store the index of the leftmost building taller than the specified range or remain -1 if none is found
        res = [-1] * len(queries)

        # Iterate through each query and process it
        for i, q in enumerate(queries):
            # Extract and sort the range to ensure l <= r
            l, r = sorted(q)

            # If the range is a single building or the rightmost building is taller than the leftmost
            if l == r or heights[r] > heights[l]:
                # The answer for this query is the rightmost building (index r)
                res[i] = r
                continue

            # Otherwise, look for a building taller than both heights[l] and heights[r] in the right portion
            for j in range(r + 1, len(heights)):
                # Check if the current building is taller than the max height in the specified range
                if heights[j] > max(heights[l], heights[r]):
                    # Update the result for this query with the index of the found building
                    res[i] = j
                    break

        # Return the results for all queries
        return res

    # Optimized - Using Min-Heap
    # Time: O(n + qlogq) where n = len(heights) and q = len(quereies)
    def leftmostBuildingQueries1(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # Initialize the result array with -1 for each query.
        # This will store the index of the leftmost building taller than the required height or remain -1 if none is found.
        res = [-1] * len(queries)

        # Create a dictionary to group queries by their right endpoint.
        # Key: right index `r`, Value: list of tuples (required_height, query_index).
        groups = defaultdict(list)

        # Preprocess the queries and populate the groups.
        for i, q in enumerate(queries):
            # Extract and sort the range to ensure l <= r.
            l, r = sorted(q)

            # Case 1: If the range is a single building or the rightmost building is taller than the leftmost.
            if l == r or heights[r] > heights[l]:
                res[i] = r  # The answer for this query is the rightmost building (index r).
            else:
                # Otherwise, calculate the required height (max of heights[l] and heights[r]) and group the query.
                h = max(heights[l], heights[r])
                groups[r].append((h, i))

        # Use a min-heap to keep track of the queries that are still pending for evaluation.
        # The heap stores tuples (required_height, query_index), sorted by required_height.
        minHeap = []

        # Iterate over each building by its index and height.
        for i, h in enumerate(heights):
            # Add queries associated with the current index `i` to the heap.
            for q_h, q_i in groups[i]:
                heapq.heappush(minHeap, (q_h, q_i))  # Push the required height and query index into the heap.

            # Process the heap to resolve queries that can now be satisfied.
            while minHeap and h > minHeap[0][0]:
                # If the current height satisfies the required height of the top query in the heap.
                q_h, q_i = heapq.heappop(minHeap)  # Remove the query from the heap.
                res[q_i] = i  # Update the result for this query with the current building index.

        # Return the results for all queries.
        return res
