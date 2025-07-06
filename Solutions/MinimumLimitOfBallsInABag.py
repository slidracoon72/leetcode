import heapq
from math import ceil
from typing import List


class Solution:
    # Neetcode: https://www.youtube.com/watch?v=MQlC8EoOdZ0&ab_channel=NeetCodeIO
    # Time: O(n * log m)
    # Using Binary Search (similar to KokoEatingBananas.py and MinimizedMaxOfProductsToStore.py)
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # Helper function to check if it's possible to split all bags
        # such that the maximum number of balls in any bag is <= max_balls
        def can_divide(max_balls):
            ops = 0  # Tracks the total number of operations needed
            for n in nums:
                # Calculate the number of splits required for bag 'n' to be <= max_balls
                # ceil(n / max_balls) gives the number of resulting bags if split
                # Subtract 1 because one operation splits one bag into two
                ops += ceil(n / max_balls) - 1

                # If the required operations exceed maxOperations, return False
                if ops > maxOperations:
                    return False
            # If within allowed operations, return True
            return True

        # Binary search range: the minimum possible penalty is 1, 
        # and the maximum is the largest bag in nums
        l, r = 1, max(nums)
        res = r  # Initialize result with the largest possible penalty

        # Perform binary search to find the smallest maximum bag size
        while l < r:
            m = l + ((r - l) // 2)  # Calculate mid-point of current range
            # Check if we can achieve a penalty of m
            if can_divide(m):
                res = m  # Update the result if m is achievable
                r = m  # Narrow the search range to the left (smaller penalties)
            else:
                l = m + 1  # Narrow the search range to the right (larger penalties)

        # Return the smallest maximum bag size (penalty) found
        return res

    # Solved using MaxHeap (11/58 Test Cases Passed)
    # Splitting max number equally
    def minimumSize1(self, nums: List[int], maxOperations: int) -> int:
        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)

        i = 0
        while i <= maxOperations:
            top = -1 * heapq.heappop(maxHeap)
            first = top // 2
            second = top - first
            heapq.heappush(maxHeap, -1 * first)
            heapq.heappush(maxHeap, -1 * second)
            i += 1

        return -1 * maxHeap[0]
