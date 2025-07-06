# LC-3396: Minimum Number of Operations to Make Elements in Array Distinct

from collections import Counter
from typing import List


class Solution:
    # Time: O(N), Space: O(N)
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = Counter(nums)  # Count occurrences of each number in the array
        start = 0  # Keeps track of the current group of three elements to remove
        i = 0  # Iterator through the array
        while i < n:
            if count[nums[i]] > 1:  # If the current element is not unique
                # Remove up to the next three elements starting from `start`
                for j in range(start, min(start + 3, n)):
                    count[nums[j]] -= 1  # Decrease the count for removed elements
                start += 3  # Update the start index to the next group
                i = start  # Reset the loop to the new start position
            else:
                i += 1  # Move to the next element if current is unique

        # Each deletion removes 3 elements, so (start // 3) returns num of operations/jumps
        return start // 3


c = Solution()
nums = [1, 2, 3, 4, 2, 3, 3, 5, 7]
print(c.minimumOperations(nums))
