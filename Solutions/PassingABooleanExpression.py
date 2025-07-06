# LC - Hard
from collections import deque


class Solution:
    # Recursive Solution
    # Neetcode: https://www.youtube.com/watch?v=q2L6yHIIbs8
    # Time: O(n), Space: O(n)
    def parseBoolExpr(self, expression: str) -> bool:
        s = expression
        i = 0

        def helper():
            nonlocal i
            c = s[i]
            i += 1
            if c == "t":
                return True
            if c == "f":
                return False
            if c == "!":
                i += 1
                res = not helper()
                i += 1
                return res

            children = []
            i += 1
            while s[i] != ")":
                if s[i] != ",":
                    children.append(helper())
                else:
                    i += 1

            i += 1
            if c == "&":
                return all(children)
            if c == "|":
                return any(children)

        return helper()

    # Using Stack - Easier to understand
    # Time: O(n), Space: O(n)
    def parseBoolExpr1(self, expression: str) -> bool:
        st = deque()
        operators = ["!", "&", "|"]
        truth = ["f", "t"]
        ignore = [",", "("]

        for c in expression:
            if c in ignore:
                continue
            if c in operators or c in truth:
                st.append(c)
            elif c == ")":
                has_True = False
                has_False = False
                while st[-1] in truth:
                    top_value = st.pop()
                    if top_value == "t":
                        has_True = True
                    elif top_value == "f":
                        has_False = True

                op = st.pop()
                if op == "!":
                    st.append("t" if not has_True else "f")
                elif op == "&":
                    st.append("f" if has_False else "t")
                else:
                    st.append("t" if has_True else "f")

        return st[-1] == "t"


c = Solution()
expression = "!(&(f,t))"
print(c.parseBoolExpr1(expression))
