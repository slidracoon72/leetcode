from typing import List


class Solution:
    # Inefficient Solution
    # Time: O(n^2 + nlogn), Space: O(n^2)
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # Step 1: Generate all pairwise distances
        l = []
        length = len(nums)

        for i in range(length):
            for j in range(i + 1, length):
                diff = abs(nums[j] - nums[i])
                l.append(diff)

        # Step 2: Sort the distances
        l.sort()

        # Step 3: Return the k-th smallest distance (1-based index)
        return l[k - 1]


# LC Hard Problem
# Neetcode: https://www.youtube.com/watch?v=bQ-QcFKwsZc
# Time: O(nlogn), Space: O(logn)
class Solution1:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # Sort the input array
        nums.sort()

        # Helper function to count the number of pairs with distance <= dist
        def helper(dist):
            l = 0  # Left pointer
            pairs = 0  # Count of valid pairs
            for r in range(len(nums)):  # Right pointer iterates through each element
                # Move the left pointer to maintain the condition nums[r] - nums[l] <= dist
                while nums[r] - nums[l] > dist:
                    l += 1
                # r - l gives the number of pairs in current window
                pairs += r - l
            return pairs

        # Binary search to find the k-th smallest distance
        l, r = 0, max(nums)  # Initialize search range: 0 to the max possible distance
        while l < r:
            m = l + (r - l) // 2  # Midpoint distance
            pairs = helper(m)  # Count pairs with distance <= m
            if pairs >= k:
                # If we have at least k pairs with distance <= m, move the right pointer
                r = m
            else:
                # If we have fewer than k pairs, move the left pointer
                l = m + 1

        # At the end of binary search, l and r converge to the smallest distance with at least k pairs
        return r
        # Alternatively, return l, as l == r at this point


c = Solution1()
nums = [1, 3, 1]
k = 1
print(c.smallestDistancePair(nums, k))
