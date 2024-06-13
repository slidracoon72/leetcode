class Solution:
    def maxProfit(self, prices) -> int:

        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit


c = Solution()

p1 = [7, 1, 5, 3, 6, 4]
p2 = [1, 2, 3, 4, 5]
p3 = [7, 6, 4, 3, 1]

print(c.maxProfit(p1))
print(c.maxProfit(p2))
print(c.maxProfit(p3))
