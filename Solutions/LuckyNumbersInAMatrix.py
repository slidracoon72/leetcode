from typing import List


class Solution:
    # Straight Forward (Simple) Solution
    # Time: O(m*n), Space: O(m+n)
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        min_row = set()
        max_col = set()

        # Finding minimum in rows
        for r in range(rows):
            smallest = float('inf')
            for c in range(cols):
                if matrix[r][c] <= smallest:
                    smallest = matrix[r][c]
            min_row.add(smallest)

        # can also do it this way
        # for r in range(rows):
        #     min_row.add(min(matrix[r]))

        # Finding largest in columns
        for c in range(cols):
            largest = float('-inf')
            for r in range(rows):
                if matrix[r][c] >= largest:
                    largest = matrix[r][c]
            max_col.add(largest)

        return list(min_row.intersection(max_col))

    # Greedy Approach
    # Time: O(m*n) , Space: O(1)
    # Neetcode: https://www.youtube.com/watch?v=ceuQgACqr78
    def luckyNumbers1(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])

        # Step 1: Find the maximum of the minimum values from each row
        max_of_row_mins = float('-inf')  # Initialize to negative infinity to find the max value
        for r in range(rows):
            row_min = min(matrix[r])  # Find the minimum value in the current row
            max_of_row_mins = max(max_of_row_mins, row_min)  # Update max_of_row_mins if current row_min is larger

        # Step 2: Check each column to find if the max_of_row_mins is the maximum in any column
        for c in range(cols):
            col_max = float('-inf')  # Initialize to negative infinity to find the max value
            for r in range(rows):
                col_max = max(col_max, matrix[r][c])  # Update col_max if the current element is larger
            if col_max == max_of_row_mins:  # If we find a column where col_max matches max_of_row_mins
                return [col_max]  # Return the lucky number as a list

        return []  # If no lucky number is found, return an empty list


c = Solution()
matrix1 = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
matrix2 = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
matrix3 = [[7, 8], [1, 2]]
print(c.luckyNumbers(matrix1))
print(c.luckyNumbers1(matrix2))
print(c.luckyNumbers1(matrix3))
