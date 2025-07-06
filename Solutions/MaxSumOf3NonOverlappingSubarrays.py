# LC - Hard
from typing import List


class Solution:
    # Neetcode: https://www.youtube.com/watch?v=SfjeJ1qyCVg&ab_channel=NeetCodeIO
    # Time: O(n), Space: O(n)
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Preprocessing step: calculate the sum of all subarrays of size k
        # `k_sums[i]` will store the sum of the subarray starting at index `i`
        k_sums = [sum(nums[:k])]  # Calculate the first subarray sum
        for i in range(k, len(nums)):  # Calculate subsequent subarray sums in O(1) for each
            k_sums.append(k_sums[-1] + nums[i] - nums[i - k])

        # Initialize a memoization dictionary for dynamic programming
        dp = {}

        # Helper function to get the maximum sum of `cnt` subarrays starting from index `i`
        def get_max_sum(i, cnt):
            # Base case: if 3 subarrays are chosen or the remaining elements are insufficient
            if cnt == 3 or i > len(nums) - k:
                return 0
            # Return cached result if available
            if (i, cnt) in dp:
                return dp[(i, cnt)]

            # Option 1: Include the current subarray in the sum
            include = k_sums[i] + get_max_sum(i + k, cnt + 1)
            # Option 2: Skip the current subarray
            skip = get_max_sum(i + 1, cnt)

            # Store the maximum result in the memoization table
            dp[(i, cnt)] = max(include, skip)
            return dp[(i, cnt)]

        # Helper function to reconstruct the indices of the 3 subarrays
        def get_indices():
            i = 0  # Start from the first index
            indices = []  # To store the starting indices of the chosen subarrays

            # Loop until all 3 subarrays are selected or no more valid subarrays
            while i <= len(nums) - k and len(indices) < 3:
                # Option 1: Include the current subarray
                include = k_sums[i] + get_max_sum(i + k, len(indices) + 1)
                # Option 2: Skip the current subarray
                skip = get_max_sum(i + 1, len(indices))

                # If including the current subarray gives a higher sum or equal sum, choose it
                if include >= skip:
                    indices.append(i)  # Add the starting index of this subarray
                    i += k  # Move to the next potential subarray after skipping `k` elements
                else:
                    i += 1  # Otherwise, move to the next index
            return indices

        # Return the starting indices of the 3 subarrays with the maximum sum
        return get_indices()


c = Solution()
nums = [1, 2, 1, 2, 6, 7, 5, 1]
k = 2
print(c.maxSumOfThreeSubarrays(nums, k))
