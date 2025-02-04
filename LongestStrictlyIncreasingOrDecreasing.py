# LC-3105. Longest Strictly Increasing or Strictly Decreasing Subarray
from typing import List


class Solution:
    # Time: O(n), Space: O(1)
    # Making 2 passes
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        def helper(increasing):
            inc, dec = 1, 1
            l = 0
            for r in range(1, n):
                if increasing:
                    if nums[r - 1] < nums[r]:
                        inc = max(inc, r - l + 1)
                    else:
                        l = r
                else:
                    if nums[r - 1] > nums[r]:
                        dec = max(dec, r - l + 1)
                    else:
                        l = r
            return inc if increasing else dec

        inc = helper(True)  # Find longest increasing subarray
        dec = helper(False)  # Find longest decreasing subarray

        return max(inc, dec)

    # Time: O(n), Space: O(1)
    # Optimized - In one pass
    def longestMonotonicSubarray1(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        inc, dec = 1, 1  # Stores the length of increasing and decreasing subarrays
        max_len = 1  # Stores the longest monotonic subarray length

        for i in range(1, n):
            if nums[i] > nums[i - 1]:  # Increasing sequence
                inc += 1
                dec = 1  # Reset decreasing count
            elif nums[i] < nums[i - 1]:  # Decreasing sequence
                dec += 1
                inc = 1  # Reset increasing count
            else:  # Reset both if no monotonicity
                inc = dec = 1

            max_len = max(max_len, inc, dec)

        return max_len


c = Solution()
nums1 = [1, 4, 3, 3, 2]
nums2 = [3, 3, 3, 3]
nums3 = [3, 2, 1]
print(c.longestMonotonicSubarray(nums1))
print(c.longestMonotonicSubarray1(nums2))
print(c.longestMonotonicSubarray1(nums3))
