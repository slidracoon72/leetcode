class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        # Continue until there are no more "digits" to process
        while columnNumber > 0:
            columnNumber -= 1  # Adjust for 1-based indexing (Excel-style)
            offset = columnNumber % 26  # Get the current character's position (0 to 25)

            # Convert the offset to the corresponding uppercase letter and add to result
            res += chr(ord('A') + offset)

            # Move to the next "digit" to the left
            columnNumber //= 26

        # The result is built in reverse order, so reverse it before returning
        return ''.join(reversed(res))


c = Solution()
print(c.convertToTitle(28))
print(c.convertToTitle(1))
print(c.convertToTitle(34))
