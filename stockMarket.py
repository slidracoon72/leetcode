from typing import List


class Solution:
    # Time: O(n), Memory: O(1)
    # Solved using "two-pointer"
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # left = buy, right = sell
        maxP = 0

        while r < len(prices):
            # profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1

        return maxP


v = Solution()

prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]

print("Max Profit: ", v.maxProfit(prices2))
