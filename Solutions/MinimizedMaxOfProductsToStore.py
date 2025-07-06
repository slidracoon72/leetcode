# LC:2064 - Minimized Maximum of Products Distributed to Any Store
import math
from typing import List


class Solution:
    # Neetcode: https://www.youtube.com/watch?v=GKSSr2xkR8A&ab_channel=NeetCodeIO
    # Using Binary Search (similar to KokoEatingBananas.py)
    # Time: O(len(quantities) * log(max(quantities))
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # Helper function to check if it's possible to distribute quantities
        # such that no store has more than x items
        def can_distribute(x):
            stores = 0  # count of stores required
            for q in quantities:
                # Calculate number of stores needed for current quantity q with max x items per store
                stores += math.ceil(q / x)
            # Return True if the required stores are less than or equal to available stores (n)
            return stores <= n

        # Initialize binary search range between 1 and the maximum of quantities
        l, r = 1, max(quantities)
        res = 0  # Variable to store the minimized maximum number of items per store

        # Binary search to find the smallest possible maximum (minimized maximum)
        while l <= r:
            x = (l + r) // 2  # Midpoint of the current range
            if can_distribute(x):  # Check if x items per store is feasible
                res = x  # If feasible, record x as a potential result
                r = x - 1  # Try to minimize further by searching left half
            else:
                l = x + 1  # If not feasible, search the right half

        return res  # Return the minimized maximum number of items per store
