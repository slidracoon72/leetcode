from typing import List


class Solution:
    # Using Hash-Map
    # Time: O(n), Space: O(n)
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen and i - seen[nums[i]] <= k:
                return True
            seen[nums[i]] = i

        return False


c = Solution()
nums = [1, 2, 3, 1, 2, 3]
k = 2
nums1 = [1, 2, 3, 1]
k1 = 3
print(c.containsNearbyDuplicate(nums1, k1))
