# LC-1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
from typing import List


# Sliding Window Problem
# Neetcode: https://www.youtube.com/watch?v=D8B4tKxMTnY
# Time: O(n), Space: O(1)
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        # Initialize with first k-1 values
        # For eg. If k = 3, initial with 2 elements
        curSum = sum(arr[:k - 1])
        for l in range(len(arr) - k + 1):
            # add kth value (right of window) (3rd element)
            # l + k - 1 gives the right end of window
            curSum += arr[l + k - 1]
            # Check if average is greater than or equal to threshold
            if curSum / k >= threshold:
                res += 1
            # shift the window by removing the left-most element
            curSum -= arr[l]
        return res


c = Solution()
arr = [2, 2, 2, 2, 5, 5, 5, 8]
k = 3
threshold = 4
print(c.numOfSubarrays(arr, k, threshold))
