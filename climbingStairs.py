class Solution:
    def climbStairs(self, n: int) -> int:

        # This question follows the Fibonacci Sequence
        # 1 2 3 4 5 6 - Stair Number
        # 1 2 3 5 8 13 - Steps Required (Sum of two previous steps)

        if n <= 2: return n

        prev1 = 1
        prev2 = 2
        current = 0

        for _ in range(2, n):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current
        return current

    # Dynamic Programming Solution
    # Time: O(n), Space: O(1)
    def climbStairsDP(self, n: int) -> int:
        one = 1
        two = 1
        for _ in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one


c = Solution()
print(c.climbStairs(2))
print(c.climbStairsDP(2))
