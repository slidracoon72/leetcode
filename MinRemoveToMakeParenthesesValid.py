class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove = set()
        stack = []

        # First pass to identify unmatched closing parentheses
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)  # Track opening parentheses
            elif c == ")":
                if stack:
                    stack.pop()  # Pair with an opening parenthesis
                else:
                    remove.add(i)  # Unmatched closing parenthesis

        # Add remaining unmatched opening parentheses from the stack
        remove.update(stack)

        # Build the resulting string
        res = [c for i, c in enumerate(s) if i not in remove]
        return "".join(res)
