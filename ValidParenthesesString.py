class Solution:
    # Time: O(n), Space: O(n)
    def checkValidString(self, s: str) -> bool:
        left = []  # Stack to keep track of indices of '('
        star = []  # Stack to keep track of indices of '*'

        # First pass: try to match ')' with '(' or '*'
        for i, ch in enumerate(s):
            if ch == '(':
                left.append(i)  # Push index of '('
            elif ch == '*':
                star.append(i)  # Push index of '*'
            else:  # ch == ')'
                # If there's no unmatched '(' or '*', string is invalid
                if not left and not star:
                    return False
                if left:
                    left.pop()  # Prefer to match ')' with '('
                else:
                    star.pop()  # Otherwise, match ')' with '*'

        # Second pass: match remaining '(' with '*' (as ')')
        # '*' must appear after '(', so compare indices
        while left and star:
            if left.pop() > star.pop():
                return False  # '(' comes after '*', can't be matched

        # If all '(' are matched, the string is valid
        return not left


c = Solution()
s1 = "((**)"
s2 = "(((*)"
print(c.checkValidString(s1))
print(c.checkValidString(s2))
