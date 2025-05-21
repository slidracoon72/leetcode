from typing import List


class Solution:
    # Time: O(m + n), Space: O(1)
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        t1, t2 = 0, 0
        z1, z2 = 0, 0

        # Calculate sum and zero count for nums1
        for num in nums1:
            t1 += num
            if num == 0:
                z1 += 1

        # Calculate sum and zero count for nums2
        for num in nums2:
            t2 += num
            if num == 0:
                z2 += 1

        # Minimum sums after replacing zeros with 1
        s1 = t1 + z1
        s2 = t2 + z2

        # Check feasibility
        if z1 == 0 and s1 < s2:  # Can't increase nums1's sum
            return -1
        if z2 == 0 and s2 < s1:  # Can't increase nums2's sum
            return -1

        # Return the minimum possible equal sum
        return max(s1, s2)


c = Solution()
nums1 = [3, 2, 0, 1, 0]
nums2 = [6, 5, 0]
print(c.minSum(nums1, nums2))
