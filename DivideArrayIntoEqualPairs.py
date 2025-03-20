from collections import defaultdict
from typing import List


class Solution:
    # Using Hash-Map
    # Time: O(n), Space: O(n)
    def divideArray(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        for v in count.values():
            if v % 2:  # if odd count of values, a pair is not possible
                return False

        return True

    # Using Hash-Set
    def divideArray1(self, nums: List[int]) -> bool:
        # Track unpaired numbers
        unpaired = set()

        # Add numbers to set if unseen, remove if seen
        for num in nums:
            if num in unpaired:
                unpaired.remove(num)
            else:
                unpaired.add(num)

        # Return true if all numbers were paired
        return len(unpaired) == 0


c = Solution()
nums = [3, 2, 3, 2, 2, 2]
print(c.divideArray(nums))
print(c.divideArray1(nums))
