from typing import List


class Solution:
    # Dynamic Programming - Bottom-Up Approach
    # Time Complexity: O(amount * len(coins))
    # Space Complexity: O(amount)
    # Neetcode: https://www.youtube.com/watch?v=H9bfqozjoqs&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=17
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dp array with a value larger than any possible number of coins needed
        # Here, dp[i] represents the minimum number of coins needed to make amount i.
        # We set all values to amount + 1 initially (infinity), since no amount of coins can initially achieve this.
        dp = [amount + 1] * (amount + 1)

        # Base case: Zero coins are needed to make amount 0
        dp[0] = 0

        # Iterate over each amount from 1 to the target amount
        for a in range(1, amount + 1):
            # For each coin, check if it can be used to make up the current amount a
            for c in coins:
                if a - c >= 0:
                    # Explanation:
                    # For a given amount 'a', and a coin of denomination 'c',
                    # We check if using the coin 'c' results in fewer coins needed:
                    # dp[a] = min(dp[a], 1 + dp[a - c])
                    # This means: If we use coin 'c', we need 1 coin plus the minimum coins needed for amount 'a - c'.
                    # Eg. coin = 4, amount = 6
                    # dp[6] = 1 (using coin 4) + dp[6-4] (remaining) = 1 + dp[2]
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # If dp[amount] is still amount + 1, it means it's not possible to make up that amount with the given coins
        if dp[amount] != amount + 1:
            return dp[amount]
        else:
            return -1


c = Solution()
coins = [1, 2, 5]
amount = 11
print(c.coinChange(coins, amount))
