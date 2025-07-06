from typing import List


class Solution:
    # Median-Based Approach
    # Neetcode: https://www.youtube.com/watch?v=2LfVNDlx8mY&ab_channel=NeetCodeIO
    # Time: O(n*m log(n*m)), Space: O(n)
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # 1. Check if all elements have the same remainder when divided by x
        # If not, it is impossible to make all elements equal
        total = 0
        for row in grid:
            for r in row:
                total += r  # Calculate the total sum of grid elements
                if r % x != grid[0][0] % x:  # Check if remainder is consistent across all elements
                    return -1  # If remainders differ, return -1 (impossible case)

        # 2. Flatten the grid into a single list and sort it
        nums = [r for row in grid for r in row]
        nums.sort()  # Sorting helps in finding the median-based approach

        # 3. Use prefix sum and suffix sum to find the minimum number of operations
        prefix = 0  # Keeps track of sum of elements before index `i`
        res = float('inf')  # Initialize result with a high value

        for i in range(len(nums)):
            # Compute cost of making all elements equal to nums[i]
            # Cost for the left side (smaller elements): increase them to nums[i]
            cost_left = (nums[i] * i) - prefix

            # Cost for the right side (larger elements): decrease them to nums[i]
            cost_right = total - prefix - nums[i] * (len(nums) - i)

            # Total number of operations required
            operations = (cost_left + cost_right) // x
            res = min(res, operations)  # Track the minimum operations needed

            # Update prefix sum for the next iteration
            prefix += nums[i]

        return res  # Return the minimum number of operations


c = Solution()
grid = [[2, 4], [6, 8]]
x = 2
print(c.minOperations(grid, x))
