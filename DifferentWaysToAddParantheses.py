from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # A dictionary that maps operators to their respective lambda functions for arithmetic operations.
        operations = {
            "+": lambda x, y: x + y,  # For addition
            "-": lambda x, y: x - y,  # For subtraction
            "*": lambda x, y: x * y,  # For multiplication
        }

        # Define a helper function 'backtrack' that computes all possible results for a sub-expression
        def backtrack(left, right):
            res = []  # List to store all possible results for the current sub-expression

            # Iterate over the current sub-expression to find operators and recursively split at each one
            for i in range(left, right + 1):
                op = expression[i]

                # Check if the current character is an operator
                if op in operations:
                    # Recursively compute possible values for the left and right sub-expressions
                    nums1 = backtrack(left, i - 1)  # Compute results for the left side (before the operator)
                    nums2 = backtrack(i + 1, right)  # Compute results for the right side (after the operator)

                    # Combine results from both sides using the current operator
                    for n1 in nums1:  # Iterate through all possible results from the left sub-expression
                        for n2 in nums2:  # Iterate through all possible results from the right sub-expression
                            res.append(operations[op](n1, n2))  # Apply the operator and add result to 'res'

            # If no operators were found (i.e., the sub-expression is a number), add the number to 'res'
            if res == []:
                res.append(
                    int(expression[left: right + 1]))  # Convert the numeric substring to an integer and add it to 'res'

            return res  # Return the list of results for this sub-expression

        # Call the backtrack function on the entire expression, from index 0 to the last index
        return backtrack(0, len(expression) - 1)
