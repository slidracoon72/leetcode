from typing import List


class Solution:
    # Neetcode: https://www.youtube.com/watch?v=LZr1w0LVzFw&ab_channel=NeetCodeIO
    # Time: O(rows * cols), Space: O(1)
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])  # Get dimensions of the box

        # Step 1: Simulate gravity by shifting stones ('#') to the right within each row
        for r in range(rows):  # Process each row independently
            # Initialize 'i' to the rightmost position in the row. This tracks the next empty position.
            i = cols - 1
            for c in reversed(range(cols)):  # Iterate from right to left in the current row
                if box[r][c] == "#":  # If we find a stone ('#'):
                    # Swap the stone with the current empty position tracked by 'i'
                    box[r][c], box[r][i] = box[r][i], box[r][c]
                    i -= 1  # Update 'i' to the next empty position (move left)

                elif box[r][c] == "*":  # If we encounter an obstacle ('*'):
                    # Reset 'i' to one position left of the obstacle
                    i = c - 1

        # Step 2: Rotate the box 90 degrees clockwise to transform rows into columns
        res = []  # Initialize the result matrix (rotated box)
        for c in range(cols):  # Iterate over columns in the original box
            col = []  # Collect elements for the new row in the rotated matrix
            for r in reversed(range(rows)):  # Iterate from bottom to top in the current column
                col.append(box[r][c])  # Add the element to the new row
            res.append(col)  # Append the new row to the result matrix

        return res  # Return the rotated box
