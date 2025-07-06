from typing import List


class Solution:
    # Time Complexity: O(n^2) in the worst case (when all elements are equal to the key)
    # Space Complexity: O(n) to store the indices of key elements
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []  # Stores the final result of indices satisfying the condition
        temp = []  # Stores indices where nums[i] == key

        # First pass: collect all indices where nums[i] == key
        for i, num in enumerate(nums):
            if num == key:
                temp.append(i)

        # Second pass: for each index, check if it's within distance k of any key index
        for i, num in enumerate(nums):
            for j in temp:
                if abs(i - j) <= k:  # If index i is within k distance from key index j
                    res.append(i)
                    break  # No need to check other key indices for this i

        return res

    # Single Pass and Sliding Window
    # Time: O(n), Space: O(n)
    def findKDistantIndices1(self, nums: List[int], key: int, k: int) -> List[int]:
        key_indices = []

        # First pass: collect all indices where nums[i] == key
        for i, num in enumerate(nums):
            if num == key:
                key_indices.append(i)

        res = set()
        # For each key index, add all indices within k distance to result
        for index in key_indices:
            start = max(0, index - k)
            end = min(len(nums) - 1, index + k)
            for i in range(start, end + 1):
                res.add(i)

        return sorted(res)


c = Solution()
print(c.findKDistantIndices(nums=[3, 4, 9, 1, 3, 9, 5], key=9, k=1))
print(c.findKDistantIndices(nums=[2, 2, 2, 2, 2], key=2, k=2))
print(c.findKDistantIndices1(nums=[3, 4, 9, 1, 3, 9, 5], key=9, k=1))
print(c.findKDistantIndices1(nums=[2, 2, 2, 2, 2], key=2, k=2))