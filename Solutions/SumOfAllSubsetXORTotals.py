from typing import List


class Solution:
    # Recursion + Memoization
    # Time: O(2^n), Space: O(n)
    def subsetXORSum(self, nums: List[int]) -> int:
        # Helper function for recursive DFS traversal
        def dfs(i, total):
            # Base case: if we have considered all elements,
            # return the accumulated XOR total
            if i == len(nums):
                return total

            # Recursive case 1: include nums[i] in the subset
            include = dfs(i + 1, total ^ nums[i])

            # Recursive case 2: exclude nums[i] from the subset
            skip = dfs(i + 1, total)

            # Return the sum of both possibilities
            return include + skip

        # Start DFS traversal from index 0 with initial XOR value 0
        return dfs(0, 0)


c = Solution()
nums = [5, 1, 6]
print(c.subsetXORSum(nums))
