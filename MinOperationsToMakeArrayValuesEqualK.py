# LC-3375: Minimum Operations to Make Array Values Equal to K
from typing import List


class Solution:
    # Time: O(nlogn), Space: O(n)
    def minOperations(self, nums: List[int], k: int) -> int:
        # Remove duplicates and sort the numbers
        nums_set = sorted(set(nums))
        n = len(nums_set)

        # Case 1: If the smallest number is equal to k,
        # we can remove all other elements (apart from the smallest element = k) to make all values equal to k
        if nums_set[0] == k:
            return n - 1

        # Case 2: If the smallest number is greater than k,
        # we can remove all elements to make all values equal to k
        if nums_set[0] > k:
            return n

        # Case 3: If k is smaller than the minimum value in the set,
        # and we can't reach it through any operation, return -1
        return -1

    # Using Hash-Set
    # Time: O(n), Space: O(n)
    def minOperations1(self, nums: List[int], k: int) -> int:
        st = set()
        for x in nums:
            if x < k:
                return -1
            elif x > k:
                st.add(x)
        return len(st)


c = Solution()
nums = [5, 2, 5, 4, 5]
k = 2
print(c.minOperations(nums, k))
