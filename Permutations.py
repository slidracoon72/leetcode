from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Generate all possible permutations of the input list `nums`.
        # Uses a recursive approach: for each permutation of nums[1:], insert nums[0]
        # at every possible position to create new permutations.
        # Args:
        #     nums: List of integers to permute.
        # Returns:
        #     List of all possible permutations, where each permutation is a list of integers.

        # Base case: if the input list is empty, return a list containing an empty list
        if len(nums) == 0:
            return [[]]

        # Recursively generate permutations for the sublist nums[1:] (excluding the first element)
        perms = self.permute(nums[1:])
        res = []  # Store the final list of permutations

        # For each permutation of the sublist
        for p in perms:
            # Insert nums[0] at every possible position in the permutation
            # Positions range from 0 to len(p) (inclusive)
            for i in range(len(p) + 1):
                # Create a copy of the current permutation to avoid modifying it
                p_copy = p.copy()
                # Insert nums[0] at position i
                p_copy.insert(i, nums[0])
                # Add the new permutation to the result
                res.append(p_copy)

        # Return the list of all permutations
        return res

# Time Complexity: O(n!), where n is the length of nums
# - For n elements, we generate n! permutations
# - Each permutation takes O(n) to construct (due to copying and inserting)
# Space Complexity: O(n!) to store all permutations
# - Recursion stack depth is O(n)
