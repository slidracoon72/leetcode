from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = set(nums1), set(nums2)

        res = []
        for n in n1:
            if n in n2:
                res.append(n)
        return res


c = Solution()
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(c.intersection(nums1, nums2))
