class Solution:
    # Time: O(n), Space: O(n)
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and c.isdigit():
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)


c = Solution()
s1 = "abc"
s2 = "cb34"
s3 = "rahu12"
print(c.clearDigits(s1))
print(c.clearDigits(s2))
print(c.clearDigits(s3))
