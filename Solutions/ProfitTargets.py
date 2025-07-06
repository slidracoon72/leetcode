# User Friendly Password System - HackerRank Question
# Tik-Tok Coding Interview Question
class Solution:
    # Efficient solution - Similar to 3-Sum
    # Time: O(n), Space: O(n)
    def stockPairs(self, stocksProfit, target):
        seen = set()
        pairs = set()

        for profit in stocksProfit:
            complement = target - profit
            if complement in seen:
                # To avoid duplicate pairs i.e, (3,7) and (7,3) are same, so add once
                pairs.add((min(profit, complement), max(profit, complement)))
            seen.add(profit)

        return len(pairs)

    # Inefficient
    # Time: O(n^2), Space: O(n)
    def stockPairs1(self, stocksProfit, target):
        res = set()
        l = len(stocksProfit)
        stocksProfit.sort()

        for i in range(l):
            for j in range(i + 1, l):
                cur = stocksProfit[i] + stocksProfit[j]
                if cur == target:
                    res.add((stocksProfit[i], stocksProfit[j]))
                elif cur > target:
                    break

        return len(res)
