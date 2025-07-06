from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Generate all possible subsets (power set) of the input list `nums`, which may contain duplicates.
        # Uses backtracking to explore all combinations, ensuring no duplicate subsets by sorting and skipping duplicates.
        # Args:
        #     nums: List of integers, may contain duplicates.
        # Returns:
        #     List of all unique subsets, where each subset is a list of integers.

        res = []  # Store the final list of unique subsets
        subset = []  # Track the current subset being built

        # Sort the array to group duplicates together, making it easier to skip them
        nums.sort()

        def backtrack(i: int) -> None:
            # Backtracking function to generate subsets starting from index i.
            # Args:
            #     i: Current index in nums to consider.

            # Base case: if we've processed all elements, add the current subset to the result
            if i == len(nums):
                res.append(subset.copy())  # Make a copy to avoid modifying the subset later
                return

            # Decision 1: Include the current number in the subset
            subset.append(nums[i])
            backtrack(i + 1)  # Recurse with the next index

            # Decision 2: Skip the current number
            subset.pop()  # Remove the current number to explore the "skip" path

            # Skip duplicates to avoid duplicate subsets
            # If the next number is the same as the current one, skip it
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)  # Recurse with the next non-duplicate index

        # Start backtracking from index 0
        backtrack(0)
        return res

# Time Complexity: O(2^n), where n is the length of nums
# - We make two decisions (include or skip) for each element, but skipping duplicates reduces redundant work
# Space Complexity: O(n) for the recursion stack and current subset
# - The result list (res) is not counted in space complexity as per LeetCode convention
