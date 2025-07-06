from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []  # This will store all the subsets
        subset = []  # Current subset being constructed

        def dfs(i):
            # Base case: if we've considered all elements
            if i >= len(nums):
                res.append(subset.copy())  # Add a copy of the current subset to results
                return

            # Include nums[i] in the subset
            subset.append(nums[i])
            dfs(i + 1)  # Recurse with the next index

            # Exclude nums[i] from the subset (backtrack)
            subset.pop()
            dfs(i + 1)  # Recurse with the next index, skipping nums[i]

        dfs(0)  # Start recursion from the first index
        return res


c = Solution()
nums = [1, 2, 3]
print(c.subsets(nums))
