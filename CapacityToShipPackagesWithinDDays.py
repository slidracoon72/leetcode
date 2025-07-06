from typing import List


class Solution:
    # Solved using Binary Search
    # Similar to KokoEatingBananas.py
    # Time: O(nlogs); s = range from l to r, Space: O(1)
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Lower bound is the max weight (can't split an item)
        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            capacity = (l + r) // 2

            cur_w = 0
            d = 1  # Start with day 1

            for w in weights:
                if cur_w + w <= capacity:
                    cur_w += w
                else:
                    d += 1
                    cur_w = w  # Start new day with current weight

            if d <= days:
                res = capacity
                r = capacity - 1
            else:
                l = capacity + 1

        return res


c = Solution()
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
print(c.shipWithinDays(weights, days))
