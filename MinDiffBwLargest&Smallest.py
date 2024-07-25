import heapq
from typing import List


# Leetcode 1509 - Minimum Difference Between Largest and Smallest Value in Three Moves
class Solution:
    # Four possible options to remove elements after sorting:
    # Remove from - (start, end)
    # Case 1: (0,3); Case 2: (1,2); Case 3: (2,1); Case 4: (3,  0)
    # Time: O(nlogn), Space: O(n)
    # Neetcode: https://www.youtube.com/watch?v=S6cUjbQuTnE
    def minDifference(self, nums: List[int]) -> int:
        # If the array has 4 or fewer elements, we can make all elements equal in at most 3 moves
        if len(nums) <= 4:
            return 0

        # Sort the array to bring the smallest and largest values to the ends
        nums.sort()

        # Initialize the result with infinity as we are looking for the minimum difference
        res = float('inf')

        # Iterate through the first 4 elements (l = 0 to 3)
        for l in range(4):
            # 'r' is the index from the end of the array corresponding to the 3 elements we can change from the end
            r = (len(nums) - 1) - 3 + l

            # Calculate the difference between the largest and smallest values
            # after changing the three largest or smallest elements
            res = min(res, nums[r] - nums[l])

        # Return the minimum difference found
        return res

    # Time Complexity: O(n log n) for heap operations and sorting
    # Space Complexity: O(n) due to the heap storage
    def minDifference1(self, nums: List[int]) -> int:
        # If the array has 4 or fewer elements, we can make all elements equal in at most 3 moves
        if len(nums) <= 4:
            return 0

        # Get the smallest 4 elements and the largest 4 elements from nums using heaps
        # heapq.nsmallest and heapq.nlargest have a time complexity of O(n log k)
        min_four = sorted(heapq.nsmallest(4, nums))
        max_four = sorted(heapq.nlargest(4, nums))

        # Initialize the result with infinity as we are looking for the minimum difference
        res = float('inf')

        # Iterate over the first 4 elements to compare the differences
        for i in range(4):
            # Calculate the difference between the i-th smallest element in max_four
            # and the i-th largest element in min_four
            res = min(res, max_four[i] - min_four[i])

        # Return the minimum difference found
        return res


c = Solution()
nums = [5, 3, 2, 4]
print(c.minDifference(nums))
print(c.minDifference1(nums))
