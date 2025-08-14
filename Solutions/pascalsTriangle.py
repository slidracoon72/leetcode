from typing import List


class Solution:
    # Time and Space: O(numRows ^ 2)
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize the result with the first row of Pascal's Triangle
        res = [[1]]

        # Generate the remaining rows
        for i in range(numRows - 1):
            # Pad the previous row with 0s on both sides to simplify addition
            temp = [0] + res[-1] + [0]

            # Initialize the new row
            row = []

            # Construct the next row by summing adjacent pairs from the padded row
            for j in range(len(temp) - 1):
                row.append(temp[j] + temp[j + 1])

            # Append the newly constructed row to the result
            res.append(row)

        # Return the complete Pascal's Triangle with numRows rows
        return res


sol = Solution()
a = 5
b = 7
c = 10
print("Pascal Triangle with", a, "rows:", sol.generate(a))
print("Pascal Triangle with", b, "rows:", sol.generate(b))
print("Pascal Triangle with", c, "rows:", sol.generate(c))

ar = [0] + [1, 2, 3, 4, 5] + [6]
print(ar)
r = [7, 8, 9, 10]
for x in r:
    ar.append(x)
print("New:", ar)
