# LC-1475. Final Prices With a Special Discount in a Shop
from typing import List


class Solution:
    # Time: O(n^2), Space: O(1)
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices) - 1):
            cur = prices[i]
            for j in range(i + 1, len(prices)):
                if prices[j] <= cur:
                    prices[i] = cur - prices[j]
                    break
        return prices


c = Solution()
prices = [8, 4, 6, 2, 3]
print(c.finalPrices(prices))
