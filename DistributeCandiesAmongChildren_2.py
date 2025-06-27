# DO AGAIN
# Inclusion-Exclusion + Combinatorics

class Solution:
    # Solved using DFS + Memoization
    # Gives TLE - 500 / 958 testcases passed
    def distributeCandies(self, n: int, limit: int) -> int:
        # If total candies exceed 3 * limit, no valid distribution possible
        if n > 3 * limit:
            return 0

        # Memoization cache: (remaining candies, children left to assign)
        memo = {}

        # DFS function: remaining candies to distribute, children left to assign
        def dfs(remain, children):
            # Base case: no candies left and no children left, valid distribution
            if remain == 0 and children == 0:
                return 1
            # Invalid cases: negative candies, too many candies, or no children but candies remain
            if remain < 0 or children == 0 or remain > children * limit:
                return 0
            # Check memoized result
            key = (remain, children)
            if key in memo:
                return memo[key]

            count = 0
            # Try assigning 0 to limit candies to the current child
            for candies in range(min(remain, limit) + 1):
                # Recursively distribute remaining candies to remaining children
                count += dfs(remain - candies, children - 1)

            # Store result in memo and return
            memo[key] = count
            return count

        # Start DFS: distribute n candies among 3 children
        return dfs(n, 3)

    # Solved using Inclusion-Exclusion + Combinatorics Principle - DO AGAIN
    # Time: O(1), Space: O(1)
    def distributeCandies1(self, n: int, limit: int) -> int:
        def cal(x):
            if x < 0:
                return 0
            return x * (x - 1) // 2

        return (
                cal(n + 2)
                - 3 * cal(n - limit + 1)
                + 3 * cal(n - (limit + 1) * 2 + 2)
                - cal(n - 3 * (limit + 1) + 2)
        )


c = Solution()
print(c.distributeCandies(5, 2))
print(c.distributeCandies1(3, 3))
