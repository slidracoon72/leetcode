# LC-2226: Maximum Candies Allocated to K Children
from typing import List


class Solution:
    # Solved using Binary Search
    # Similar to KokoEatingBananas.py
    # Time: (n*log(m)), Space: O(1)
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        if total < k:  # If total candies < k kids, impossible
            return 0

        # Define binary search range: 1 to max pile size
        l, r = 1, max(candies)  # r = total // k also works and is more efficient
        res = 0  # Track maximum possible candies per child

        # Binary search for maximum candies per child
        while l <= r:
            mid = (l + r) // 2
            child = 0
            # Calculate how many children can get 'mid' candies
            for c in candies:
                child += c // mid

            if child >= k:  # If enough children can get 'mid' candies
                res = mid  # Update result
                l = mid + 1  # Try a larger value
            else:  # If not enough children
                r = mid - 1  # Try a smaller value

        return res


c = Solution()
candies = [5, 8, 6]
k = 3
print(c.maximumCandies(candies, k))
