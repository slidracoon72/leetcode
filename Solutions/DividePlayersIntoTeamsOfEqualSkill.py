from typing import List


class Solution:
    # Time complexity: O(n*logn) for sorting, Space complexity: O(n) for storing pairs
    def dividePlayers(self, skill: List[int]) -> int:
        # Step 1: Sort the skills to pair smallest with largest elements
        skill.sort()

        # Initialize an empty list to store valid pairs of players
        s = list()
        # Set two pointers, left (l) and right (r), at the start and end of the sorted list
        l, r = 0, len(skill) - 1
        # Calculate the initial target sum based on the first and last player's skill
        target_sum = skill[l] + skill[r]

        # Step 2: Pair players from both ends of the sorted list
        while l < r:
            # Check if the current pair of players' skill sum matches the target sum
            if skill[l] + skill[r] == target_sum:
                # Append the valid pair to the list
                s.append((skill[l], skill[r]))
                # Update pointers to check the next pair
                l += 1
                r -= 1
            else:
                # If any pair does not match the target sum, return -1 as it's not possible to divide players equally
                return -1

        # Step 3: Calculate the result based on the product of skill levels in each pair
        res = 0
        for x, y in s:
            # Add the product of each pair to the result
            res += x * y
        return res

    # Optimized - Similar Approach
    # Not using list
    def dividePlayers1(self, skill: List[int]) -> int:
        skill.sort()

        l, r = 0, len(skill) - 1
        target_sum = skill[l] + skill[r]
        res = 0

        while l < r:
            if skill[l] + skill[r] == target_sum:
                res += skill[l] * skill[r]
                l += 1
                r -= 1
            else:
                return -1

        return res
