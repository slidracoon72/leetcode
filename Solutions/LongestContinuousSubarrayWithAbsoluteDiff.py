# LC-1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
from collections import deque
from typing import List


# Neetcode: https://www.youtube.com/watch?v=V-ecDfY5xEw&ab_channel=NeetCodeIO
# Similar to SlidingWindowMaximum.py
class Solution:
    # Monotonically Decreasing Queue - For Max Queue
    # Monotonically Increasing Queue - For Min Queue
    # Time: O(n), Space: O(n)
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q = deque()  # Monotonically increasing deque (to track the minimums in the current window)
        max_q = deque()  # Monotonically decreasing deque (to track the maximums in the current window)
        res = 0  # To store the maximum length of the subarray satisfying the condition

        l = 0  # Left pointer for the sliding window
        # Iterate through the array with the right pointer
        for r in range(len(nums)):
            # Maintain the increasing nature of the min_q (remove elements greater than nums[r])
            while min_q and min_q[-1] > nums[r]:
                min_q.pop()

            # Maintain the decreasing nature of the max_q (remove elements smaller than nums[r])
            while max_q and max_q[-1] < nums[r]:
                max_q.pop()

            # Append the current element to both deques
            min_q.append(nums[r])
            max_q.append(nums[r])

            # If the absolute difference between the max and min in the window exceeds the limit
            while max_q[0] - min_q[0] > limit:
                # Remove the leftmost element from the max_q if it matches nums[l]
                if nums[l] == max_q[0]:
                    max_q.popleft()
                # Remove the leftmost element from the min_q if it matches nums[l]
                if nums[l] == min_q[0]:
                    min_q.popleft()
                # Shrink the window by moving the left pointer
                l += 1

            # Update the result with the maximum window size found so far
            res = max(res, r - l + 1)

        return res


c = Solution()
nums = [10, 1, 2, 4, 7, 2]
limit = 5
print(c.longestSubarray(nums, limit))
