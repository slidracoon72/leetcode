from typing import List


class Solution:
    # Solved using Sliding Window
    # Time: O(n^2); Getting TLE - 58 / 62 testcases passed
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, 0
        res = 0
        while i < n:
            temp = 0
            window = set()
            while j < n and nums[j] not in window:
                cur = nums[j]
                window.add(cur)
                temp += cur
                j += 1

            res = max(res, temp)
            i += 1
            j = i

        return res

    # Solved using Sliding Window
    # Time: O(n), Space: O(n)
    def maximumUniqueSubarray1(self, nums: List[int]) -> int:
        seen = set()  # Set to store unique elements in the current window
        res, cur_sum = 0, 0  # res stores the max sum, cur_sum stores sum of current window

        l = 0  # Left pointer of the sliding window
        for r in range(len(nums)):  # Right pointer of the sliding window
            # If duplicate found, shrink the window from the left
            while nums[r] in seen:
                cur_sum -= nums[l]  # Subtract value at left pointer
                seen.remove(nums[l])  # Remove from set
                l += 1  # Move left pointer forward

            # Add the new unique number to the window
            seen.add(nums[r])
            cur_sum += nums[r]

            # Update result if current sum is greater
            res = max(res, cur_sum)

        return res  # Return the maximum sum of a unique-element subarray


c = Solution()
nums = [4, 2, 4, 5, 6]
print(c.maximumUniqueSubarray1(nums))
