from typing import List


# Neetcode: https://www.youtube.com/watch?v=_wBj3IMV7tY
class Solution:
    # Brute Force - Works well
    # Time: O(2^n), Space: O(n)
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Calculate the maximum possible OR value by OR-ing all elements in the nums list
        max_or = 0
        for n in nums:
            max_or = max_or | n

        res = 0  # To keep track of the number of subsets with the maximum OR value

        # Depth-First Search (DFS) function to explore all subsets
        def dfs(i, cur_or):
            nonlocal res, max_or  # Use nonlocal to access res and max_or from the outer function
            if i == len(nums):  # Base case: reached the end of the list
                # If the current OR value matches the maximum OR value, increment the result
                res += 1 if max_or == cur_or else 0
                return

            # Recursive call: explore the subset that excludes the current element
            dfs(i + 1, cur_or)
            # Recursive call: explore the subset that includes the current element (OR with the current element)
            dfs(i + 1, cur_or | nums[i])

        # Start DFS from index 0 with an initial OR value of 0
        dfs(0, 0)
        return res  # Return the count of subsets with the maximum OR value
