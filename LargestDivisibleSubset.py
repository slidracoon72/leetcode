from typing import List


class Solution:
    # Recursion + Memoization
    # Time: O(n^2), Space: O(n^2)
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Sort the numbers to make it easier to check divisibility relationships
        nums.sort()

        # Cache to memoize the results of (i, prev)
        # Key: (current index, previous number included in subset)
        # Value: largest divisible subset starting from index i with previous number 'prev'
        cache = {}

        # Helper function using DFS with memoization
        def dfs(i, prev):
            # Base case: if we've considered all elements, return empty list
            if i == len(nums):
                return []

            # If result already computed for this state, return it
            if (i, prev) in cache:
                return cache[(i, prev)]

            # Option 1: skip nums[i]
            res = dfs(i + 1, prev)

            # Option 2: include nums[i] if it's divisible by 'prev'
            if nums[i] % prev == 0:
                # Recursively build the subset including nums[i]
                temp = [nums[i]] + dfs(i + 1, nums[i])
                # Choose the longer subset between including and excluding nums[i]
                res = temp if len(temp) > len(res) else res

            # Memoize and return the result
            cache[(i, prev)] = res
            return res

        # Initial call with index 0 and previous value 1 (since all nums[i] % 1 == 0)
        return dfs(0, 1)


c = Solution()
nums = [1, 2, 4, 8]
print(c.largestDivisibleSubset(nums))
