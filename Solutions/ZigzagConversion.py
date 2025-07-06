class Solution:
    # Time: O(n), Space: O(n)
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if only one row or the string is too short to zigzag
        if numRows == 1 or numRows >= len(s):
            return s

        idx, d = 0, 1  # idx: current row, d: direction (1 for down, -1 for up)

        # Initialize a list of lists to store characters for each row
        rows = [[] for _ in range(numRows)]

        # Place characters in appropriate rows following the zigzag pattern
        for char in s:
            rows[idx].append(char)
            # Change direction at the top or bottom row
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d  # Move to the next row based on direction

        # Join all characters in each row to form complete strings
        for i in range(numRows):
            rows[i] = ''.join(rows[i])

        # Concatenate all rows to get the final zigzag string
        return ''.join(rows)


c = Solution()
s = "PAYPALISHIRING"
numRows = 4
print(c.convert(s, numRows))
