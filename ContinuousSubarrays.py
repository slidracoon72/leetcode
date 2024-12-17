from collections import defaultdict
from typing import List


class Solution:
    # Time: O(N), Space: O(N)
    def continuousSubarrays(self, nums: List[int]) -> int:
        # Map to maintain sorted frequency map of current window
        freq = defaultdict(int)
        count = 0
        l, r = 0, 0

        while r < len(nums):
            # Add current element to frequency map
            freq[nums[r]] += 1

            # While window violates the condition |nums[i] - nums[j]| ≤ 2
            # Shrink window from left
            while max(freq) - min(freq) > 2:
                # Remove leftmost element from frequency map
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1

            # Add count of all valid subarrays ending at right
            count += r - l + 1
            r += 1

        return count


c = Solution()
nums = [5, 4, 2, 4]
print(c.continuousSubarrays(nums))
