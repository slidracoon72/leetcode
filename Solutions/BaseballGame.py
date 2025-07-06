from typing import List


class Solution:
    # Solved using stack
    # Time: O(n), Space: O(n)
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                if len(stack) >= 2:
                    stack.append((stack[-1] + stack[-2]))
            elif op == "D":
                score = 2 * stack[-1]
                stack.append(score)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)

    # Similar as above
    def calPoints1(self, operations: List[str]) -> int:
        stack, res = [], 0
        for op in operations:
            if op == "+":
                res += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                res += (2 * stack[-1])
                stack.append(2 * stack[-1])
            elif op == "C":
                res -= stack.pop()
            else:
                res += int(op)
                stack.append(int(op))
        return res


c = Solution()
ops = ["5", "2", "C", "D", "+"]
print(c.calPoints(ops))
