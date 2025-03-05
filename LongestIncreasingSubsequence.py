from typing import List


# Dynamic Programing (1D)
# Time: O(n^2)
# Neetcode: https://www.youtube.com/watch?v=cjWnW0hdF1Y
class Solution:
    # Bottom-Up Approach
    def lengthOfLIS(self, nums: List[int]) -> int:
        # LIS[i] will hold the length of the longest increasing subsequence
        # that ends with the element at index i
        dp = [1] * len(nums)

        # We iterate from the end of the list to the beginning
        for i in range(len(nums) - 1, -1, -1):
            # For each element at index i, we check all elements to its right
            for j in range(i + 1, len(nums)):
                # If the current element is less than the element at index j,
                # it means we can append the element at index j to the subsequence
                # ending at index i to form a longer increasing subsequence.
                if nums[i] < nums[j]:
                    # Update LIS[i] to be the maximum of its current value
                    # or the length of the subsequence ending at index j plus 1.
                    dp[i] = max(dp[i], 1 + dp[j])

        # The length of the longest increasing subsequence is the maximum value in LIS.
        return max(dp)

    # Top-Down Approach
    def lengthOfLIS_1(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n

        for i in range(n):  # i = index of current number
            for j in range(i):  # j = index of previous number
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)


c = Solution()
print(c.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(c.lengthOfLIS_1([10, 9, 2, 5, 3, 7, 101, 18]))
