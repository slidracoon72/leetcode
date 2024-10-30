from typing import List


# LC - Hard
class Solution:
    # Neetcode: https://www.youtube.com/watch?v=Ys-q9qPpleY
    # Time: O(n^3), Space: O(n)
    # Dynamic Programming
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Calculate Longest Increasing Subsequence (LIS) for each index
        # lis[i] will store the length of the longest increasing subsequence ending at index i
        lis = [1] * n  # Initialize LIS array with 1, as each element alone is a subsequence
        for i in range(n):
            for j in range(i):
                # Check if nums[j] can contribute to increasing sequence at nums[i]
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], 1 + lis[j])

        # Step 2: Calculate Longest Decreasing Subsequence (LDS) for each index, starting from the end
        # lds[i] will store the length of the longest decreasing subsequence starting at index i
        lds = [1] * n  # Initialize LDS array with 1
        for i in reversed(range(n)):
            for j in range(i + 1, n):
                # Check if nums[j] can contribute to decreasing sequence starting at nums[i]
                if nums[j] < nums[i]:
                    lds[i] = max(lds[i], 1 + lds[j])

        # Step 3: Calculate the minimum number of removals to form a valid mountain array
        res = n  # Start with the maximum possible removals (all elements)
        for i in range(1, n - 1):  # Mountain peak can't be the first or last element
            if lis[i] > 1 and lds[i] > 1:  # Ensure it's a valid mountain peak
                # Calculate minimum removals to retain current mountain structure
                res = min(res, n - (lis[i] + lds[i] - 1))  # -1 because `i` is counted twice

        return res
