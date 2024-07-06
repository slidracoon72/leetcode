from typing import List


# Backtracking - Recursive
# Time: O(n*(4^n))
# Neetcode: https://www.youtube.com/watch?v=0snEunUacZY
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Mapping of digits to corresponding characters
        digitsToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # List to store the resulting combinations
        res = []

        # Helper function to perform backtracking
        def backtrack(i, curStr):
            # Base Case: if the current string length matches the input digits length
            if len(curStr) == len(digits):
                res.append(curStr)  # Add the current combination to the result list
                return

            # Recursive Case: Iterate over all characters that the current digit maps to
            for c in digitsToChar[digits[i]]:
                # Recursively call backtrack with the next index and current string + current character
                backtrack(i + 1, curStr + c)

        # If the input digits string is not empty, initiate backtracking
        if digits:
            backtrack(0, "")

        # Return the list of combinations
        return res
