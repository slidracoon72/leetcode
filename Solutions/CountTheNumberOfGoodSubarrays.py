from collections import defaultdict
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0  # Start of the sliding window
        right = 0  # End of the sliding window
        res = 0  # Total count of "good" subarrays
        freq = defaultdict(int)  # Frequency map to count elements in the current window
        equal_pairs = 0  # Number of equal index pairs in the window

        # Move the left pointer of the sliding window
        while left < n:
            # Expand the right pointer until we get at least `k` equal pairs
            while right < n and equal_pairs < k:
                freq[nums[right]] += 1
                # If we've seen this number before, it contributes to equal pairs
                if freq[nums[right]] >= 2:
                    equal_pairs += freq[nums[right]] - 1
                right += 1

            # If we have at least `k` equal pairs, all subarrays from current left to end are valid
            if equal_pairs >= k:
                res += n - right + 1

            # Shrink the window from the left, update frequency and equal_pairs accordingly
            freq[nums[left]] -= 1
            if freq[nums[left]] > 0:
                equal_pairs -= freq[nums[left]]
            left += 1

        return res


c = Solution()
nums = [3, 1, 4, 3, 2, 2, 4]
k = 2
print(c.countGood(nums, k))