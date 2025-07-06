from typing import List


# Neetcode: https://www.youtube.com/watch?v=unIz8W9nuyk
# Time Complexity: O(m + n), where m is the length of the given rolls list and n is the number of missing rolls.
# Space Complexity: O(1), as the space used does not scale with the input size (except for the output list).

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        """
        This function calculates the missing dice rolls based on the existing rolls and the target mean.
        It returns a list of possible dice values for the missing rolls or an empty list if it's not possible.

        Args:
        rolls (List[int]): List of known dice rolls.
        mean (int): Target mean for the combined rolls (known and missing).
        n (int): Number of missing dice rolls to be determined.

        Returns:
        List[int]: List of dice values for the missing rolls or an empty list if a valid solution is not possible.
        """

        # Step 1: Determine the number of known rolls (m).
        m = len(rolls)

        # Step 2: Calculate the total sum required to achieve the target mean for all rolls (m known rolls + n missing rolls).
        total_sum = mean * (m + n)

        # Step 3: Calculate the sum required from the missing rolls by subtracting the sum of known rolls from the total sum.
        missing_sum = total_sum - sum(rolls)

        # Step 4: Validation check:
        # - If the missing sum is too large to be filled by n dice rolls (maximum sum = 6 * n), return an empty list.
        # - If the missing sum is too small to be filled by n dice rolls (minimum sum = n), return an empty list.
        if missing_sum > 6 * n or missing_sum < n:
            return []

        # Step 5: If the validation passes, start computing the missing rolls.
        # Initialize an empty list to store the results.
        res = []

        # Step 6: Iterate while we still have missing rolls to fill (n > 0).
        while n:
            # Step 7: Calculate the value for the current dice roll.
            # - Use the minimum of 6 (maximum possible value for a dice) and the remaining missing sum spread across the remaining rolls.
            #   This ensures that we don't exceed the required sum and keep the distribution valid.
            dice = min(6, missing_sum - n + 1)

            # Step 8: Append the calculated dice value to the result list.
            res.append(dice)

            # Step 9: Update the remaining missing sum by subtracting the value we just assigned.
            missing_sum -= dice

            # Step 10: Decrease the number of remaining missing rolls.
            n -= 1

        # Step 11: Return the list of computed missing rolls.
        return res


c = Solution()
rolls = [3, 2, 4, 3]
mean = 4
n = 2
print(c.missingRolls(rolls, mean, n))
