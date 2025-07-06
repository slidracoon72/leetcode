from typing import List


class Solution:
    # Top - Down Approach
    # DFS - Recursion With Memoization
    # Time: O(n * m), Space: O(n)
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Durations corresponding to ticket types: 1-day, 7-day, 30-day
        d = [1, 7, 30]
        # Memoization dictionary to store the minimum cost for each starting index
        dp = {}

        # Helper function to calculate the minimum cost using recursion and memoization
        def dfs(i):
            # Base case: If we've processed all travel days, no more cost is needed
            if i == len(days):
                return 0

            # Check if the result for this index is already computed
            if i in dp:
                return dp[i]

            # Initialize the minimum cost for the current index as infinity
            res = float('inf')
            # Start another pointer `j` at the current index
            j = i

            # Iterate through the ticket types and their costs
            for cost, duration in zip(costs, d):
                # Move the pointer `j` to skip all the days covered by the current ticket
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1
                # Calculate the cost of choosing this ticket and add the result of the next step
                res = min(res, cost + dfs(j))

            # Store the result in the memoization dictionary
            dp[i] = res
            return dp[i]

        # Start the recursive function from the first travel day
        return dfs(0)


c = Solution()
days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
print(c.mincostTickets(days, costs))
