# This question can also be solved with Knuth-Morris-Pratt (KMP) Algorithm
# Techdose: https://www.youtube.com/watch?v=bCxYcTcztF0&ab_channel=Techdose

class Solution:
    # Using replace() method
    # Time: O(n * m)
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:  # Keep removing until no occurrences left
            s = s.replace(part, "", 1)  # Remove only the leftmost occurrence
        return s

    # Using Stack
    # Time: O(n * m), Space: O(n + m)
    def removeOccurrences1(self, s: str, part: str) -> str:
        stack = []
        n = len(part)

        for c in s:
            stack.append(c)
            if len(stack) >= n and "".join(stack[-n:]) == part:
                for _ in range(n):
                    stack.pop()

        return "".join(stack)

    # Using Stack - Similar as above
    #  # Time: O(n*m), Space: O(n+m)
    def removeOccurrences2(self, s: str, part: str) -> str:
        stack = []
        n = len(part)

        for c in s:
            stack.append(c)
            # Check only when the stack has enough characters
            if len(stack) >= n and stack[-n:] == list(part):
                del stack[-n:]  # Remove `part` efficiently

        return "".join(stack)  # Convert list to string at the end


c = Solution()
s = "daabcbaabcbc"
part = "abc"
print(c.removeOccurrences(s, part))
print(c.removeOccurrences1(s, part))
print(c.removeOccurrences2(s, part))
