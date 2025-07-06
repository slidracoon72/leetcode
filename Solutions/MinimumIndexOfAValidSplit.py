from collections import Counter
from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Step 1: Find the overall dominant element
        count = Counter(nums)
        dominant = max(count.items(), key=lambda x: x[1])[0]  # Most frequent element
        n = len(nums)
        if count[dominant] * 2 <= n:  # No dominant element exists
            return -1

        # Step 2: Track left segment count and check split
        left_count = 0  # Count of dominant in left segment
        for i in range(n - 1):  # Up to n-2 since right must be non-empty
            if nums[i] == dominant:
                left_count += 1
            right_count = count[dominant] - left_count

            # Left segment: [0, i], length = i + 1
            # Right segment: [i + 1, n-1], length = n - (i + 1)
            if left_count * 2 > i + 1 and right_count * 2 > n - (i + 1):
                return i

        return -1  # No valid split found


c = Solution()
nums = [2, 1, 3, 1, 1, 1, 7, 1, 2, 1]
print(c.minimumIndex(nums))
