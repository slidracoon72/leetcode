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


c = Solution()
s1 = "lee(t(c)o)de)"
s2 = "a)b(c)d"
s3 = "))(("
print(c.minRemoveToMakeValid(s1))
print(c.minRemoveToMakeValid(s2))
print(c.minRemoveToMakeValid(s3))
