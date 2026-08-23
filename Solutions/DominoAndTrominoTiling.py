# DO AGAIN
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (max(4, n + 1))
        dp[1], dp[2], dp[3] = 1, 2, 5
        for i in range(4, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD
        return dp[n]


# DO AGAIN
class Solution1:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        # dp[i] = number of ways to fully tile a 2 x i board
        # Base cases, found by hand-counting small boards:
        # dp[0] = 1 (empty board, one "way" — do nothing)
        # dp[1] = 1 (single vertical domino)
        # dp[2] = 2 (two vertical dominoes, or two horizontal dominoes stacked)
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2

        # Recurrence: dp[i] = 2*dp[i-1] + dp[i-3]
        # Intuition:
        #  - 2*dp[i-1]: take a fully tiled board of width i-1, and close it
        #    off with either a vertical domino, or a tromino-completing pair
        #    (there are 2 mirrored ways to do this "notch" completion)
        #  - dp[i-3]: accounts for the case where a tromino pair straddles
        #    the boundary further back, avoiding double-counting
        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD

        return dp[n]


c = Solution()
n = 3
# n = 1
print(c.numTilings(n))
