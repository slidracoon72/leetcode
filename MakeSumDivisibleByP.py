from typing import List


# Neetcode: https://www.youtube.com/watch?v=tZXsLAyE0SE
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remainder = total % p

        # If the total sum is already divisible by p, return 0 (no need to remove anything)
        if remainder == 0:
            return 0

        prefix_sum = 0
        min_len = len(nums)
        prefix_map = {0: -1}  # Maps prefix_sum mod p to its index

        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p

            # Find the complement that would cancel out the remainder
            target = (prefix_sum - remainder) % p

            if target in prefix_map:
                min_len = min(min_len, i - prefix_map[target])

            # Store current prefix sum modulo p
            prefix_map[prefix_sum] = i

        return min_len if min_len < len(nums) else -1
