# LC - Hard
import collections
from typing import List


# Neetcode: https://www.youtube.com/watch?v=DfljaUwZsOk&ab_channel=NeetCode
class Solution:
    # Monotonically Decreasing Queue
    # Time: O(n), Space: O(n)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []  # Result list to store the maximums of each window
        q = collections.deque()  # Deque to store indices of elements in the current window
        l = r = 0  # Left (l) and right (r) pointers to define the sliding window

        while r < len(nums):  # Iterate through the array with the right pointer
            # Remove indices of elements from the deque that are smaller than the current element
            # (nums[r]) since they cannot be the maximum in any upcoming window
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            # Add the current index to the deque
            q.append(r)

            # Remove the leftmost index from the deque if it is out of the current window
            if l > q[0]:
                q.popleft()

            # If the current window size is >= k, record the maximum for this window
            if (r + 1) >= k:
                # The maximum is at the index stored at the front of the deque
                res.append(nums[q[0]])
                # Move the left pointer to shrink the window
                l += 1

            # Move the right pointer to expand the window
            r += 1

        return res


c = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(c.maxSlidingWindow(nums, k))
