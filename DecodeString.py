class Solution:
    # Solved using Stack
    # Time: O(n), Space: O(n)
    def decodeString(self, s: str) -> str:
        stack = []
        for x in s:
            if x == "]":
                temp = ""
                # Get the substring within brackets
                while stack[-1] != "[":
                    temp = stack.pop() + temp  # keep order correct (by popping and then adding)
                stack.pop()  # Remove the '['

                # Get the repeat count k (could be multiple digits)
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k  # Build the number from stack (reverse order)

                # Repeat the substring and push back to stack
                stack.append(temp * int(k))
            else:
                stack.append(x)

        return "".join(stack)


c = Solution()
s = "3[a]2[bc]"
print(c.decodeString(s))
