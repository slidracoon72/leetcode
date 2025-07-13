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

    def subsets1(self, nums: List[int]) -> List[List[int]]:
        res = set()  # Use a set to store unique subsets (as tuples, since lists are unhashable)

        def dfs(i, cur):
            # Base case: if we've considered all elements
            if i == len(nums):
                res.add(tuple(cur))  # Convert list to tuple to store in set
                return

            # Recursive case 1: include nums[i] in the current subset
            cur.append(nums[i])
            dfs(i + 1, cur)

            # Backtrack: remove the last element to explore the "exclude" case
            cur.pop()

            # Recursive case 2: exclude nums[i] from the current subset
            dfs(i + 1, cur)

        dfs(0, [])  # Start DFS from index 0 with an empty subset
        return [list(t) for t in res]  # Convert result back to list of lists


c = Solution()
nums = [1, 2, 3]
print(c.subsets(nums))
