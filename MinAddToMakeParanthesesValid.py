class Solution:
    # Neetcode: https://www.youtube.com/watch?v=UizI7R6ND9Q
    # Time: O(n), Space: O(1)
    def minAddToMakeValid(self, s: str) -> int:
        # 'opened' tracks the number of unbalanced open brackets
        # 'closed' tracks the number of unbalanced close brackets
        opened, closed = 0, 0

        for x in s:
            # If the current character is an open bracket
            if x == "(":
                opened += 1
            # If the current character is a close bracket
            else:
                # If there are no unmatched open brackets, we need an extra close bracket
                if opened == 0:
                    closed += 1
                # If there is an unmatched open bracket, we pair it with the close bracket
                opened = max(opened - 1, 0)

        # The total moves required is the sum of unmatched open and close brackets
        return opened + closed

    # Similar
    def minAddToMakeValid1(self, s: str) -> int:
        opened, closed = 0, 0

        for x in s:
            if x == "(":
                opened += 1
            else:
                opened -= 1
                if opened < 0:
                    opened = 0
                    closed += 1

        return opened + closed


c = Solution()
s = "((("
print(c.minAddToMakeValid1(s))
