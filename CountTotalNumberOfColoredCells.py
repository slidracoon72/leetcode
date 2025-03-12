class Solution:
    # Pattern: 1, 4, 13, 25... (each step increases by a multiple of 4)
    # The number of newly added colored cells increases by 4 in each step.
    # Time: O(n), Space: O(1)
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1  # Base case: If n is 1, only the center cell is colored.

        res = 1  # Start with the initial single colored cell at n=1.
        add = 4  # The number of new cells added in the first expansion step.

        for _ in range(n - 1):  # Loop n-1 times to expand the pattern.
            res += add  # Add new cells to the total count.
            add += 4  # Increase the number of new cells by 4 for the next step.

        return res  # Return the total number of colored cells after n steps.

    # Using Math - Gauss Formula
    # Neetcode: https://www.youtube.com/watch?v=Ajg7LRTBo6U&ab_channel=NeetCodeIO
    # Time: O(1), Space: O(1)
    def coloredCells1(self, n: int) -> int:
        return 1 + 4 * (n * (n - 1) // 2)


c = Solution()
print(c.coloredCells(1))
print(c.coloredCells(2))
print(c.coloredCells(3))
print(c.coloredCells(4))
print(c.coloredCells(5))
