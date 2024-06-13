from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for x in tokens:
            c = 0
            if x.startswith("-") and len(x) >= 2:
                stack.append(int(x))

            elif x.isdigit():
                stack.append(int(x))

            else:
                if len(stack) >= 2:
                    a = int(stack[-1])
                    b = int(stack[-2])

                    if x == "+":
                        c = a + b
                    elif x == "-":
                        c = b - a
                    elif x == "/":
                        c = int(b / a)
                    elif x == "*":
                        c = a * b

                    stack.pop(-1)
                    stack.pop(-1)
                    stack.append(c)

        return stack[-1]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# tokens = ["2", "1", "+", "3", "*"]
# tokens = ["4", "13", "5", "/", "+"]
# tokens = ["3", "-4", "+"]
# tokens = ["4", "3", "-"]

c = Solution()
print(c.evalRPN(tokens))
