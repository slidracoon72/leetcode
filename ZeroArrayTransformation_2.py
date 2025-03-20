from typing import List


class Solution:
    # Solving using Difference Array - ideal for range updates
    # Invert the problem - Convert 0-array to nums
    # Techdose: https://www.youtube.com/watch?v=Ap8NIgIqM2A&ab_channel=Techdose
    # Time Complexity: O(N + Q), Space Complexity: O(N)
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        diff = [0] * (n + 1)  # Difference array to efficiently apply range updates
        sum_val = 0  # Tracks the cumulative sum (prefix sum) of applied decrements
        pos = 0  # Tracks the number of queries processed

        # Iterate through each element in nums
        for i in range(n):
            # If the current value in nums (adjusted by sum_val) is still greater than 0,
            # apply more queries until nums[i] becomes 0 or negative.
            while sum_val + diff[i] < nums[i]:
                if pos == len(queries):  # If all queries are exhausted but nums[i] is still > 0, return -1
                    return -1

                start, end, val = queries[pos]  # Get the next query (range update)
                pos += 1  # Move to the next query

                if end < i:  # If the query range does not affect the current index, skip it
                    continue

                # Apply the decrement in the range using the difference array technique
                diff[max(start, i)] += val  # Apply decrement at the start index
                if end + 1 < n:
                    diff[end + 1] -= val  # Revert decrement after the range

            # Apply accumulated difference updates
            sum_val += diff[i]

        # Return the number of queries used to make all elements ≤ 0
        return pos


c = Solution()
nums = [2, 0, 2]
queries = [[0, 2, 1], [0, 2, 1], [1, 1, 3]]
print(c.minZeroArray(nums, queries))
