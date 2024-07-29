import heapq
from typing import List


# This is a LeetCode Hard problem
# It uses a Two-Heap approach to solve the problem efficiently
# Time Complexity: O(k * logn), Space Complexity: O(n)
# Neetcode: https://www.youtube.com/watch?v=1IUzNJ6TPEM
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Max Heap to store the profits of the projects we can currently afford
        maxProfit = []

        # Min Heap to store the projects by their capital requirement (capital, profit)
        minCapital = [(c, p) for c, p in zip(capital, profits)]

        # Heapify the minCapital list to create a Min-Heap
        heapq.heapify(minCapital)

        # We can select at most k projects
        for i in range(k):
            # Move projects from minCapital to maxProfit if we have enough capital to start them
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                # Use -p to turn the min-heap into a max-heap by profit
                heapq.heappush(maxProfit, -1 * p)

            # If there are no affordable projects, break out of the loop
            if not maxProfit:
                break

            # Select the project with the maximum profit
            w += -1 * heapq.heappop(maxProfit)

        # Return the maximized capital after selecting up to k projects
        return w


c = Solution()
k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]
print(c.findMaximizedCapital(k, w, profits, capital))
