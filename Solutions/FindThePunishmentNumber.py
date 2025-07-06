# Techdose: https://www.youtube.com/watch?v=NByJemyF_rQ&ab_channel=Techdose
# Recursion-based approach
class Solution:
    def isValid(self, sq: str, pos: int, sum_val: int, val: int) -> bool:
        """
        Checks whether the square of a number can be partitioned into segments
        whose sum equals the original number.

        :param sq: String representation of the squared number
        :param pos: Current position in the string
        :param sum_val: Current sum of selected segments
        :param val: The original number before squaring
        :return: True if a valid partition exists, else False
        """
        if pos >= len(sq):  # Base case: If we reach the end of the string
            return sum_val == val  # Check if the sum matches the original number

        # Try all possible partitions starting from current position
        for i in range(len(sq) - pos):
            curr_val = int(sq[pos:pos + i + 1])  # Extract a number segment
            # Recursively check if the remaining string forms a valid partition
            if self.isValid(sq, pos + i + 1, sum_val + curr_val, val):
                return True

        return False  # No valid partition found

    def punishmentNumber(self, n: int) -> int:
        """
        Calculates the punishment number for a given range.

        :param n: Upper bound of the range (1 to n)
        :return: Sum of squares of numbers that satisfy the partitioning condition
        """
        punishment_number = 1  # Initialize with 1, as 1^2 is always valid

        for i in range(2, n + 1):  # Iterate through numbers from 2 to n
            sq = str(i * i)  # Compute the square and convert to string
            # Check if the square can be partitioned to sum to the original number
            if self.isValid(sq, 0, 0, i):
                punishment_number += i * i  # Add valid squared value to the sum

        return punishment_number  # Return the final punishment number


c = Solution()
n = 10
print(c.punishmentNumber(n))
