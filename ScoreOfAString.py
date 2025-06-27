class Solution:
    # ord() gives the ASCII value of characters
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s) - 1):
            # Calculate the absolute difference of adjacent characters
            score += abs(ord(s[i]) - ord(s[i + 1]))
        return score

    def scoreOfString1(self, s: str) -> int:
        score = 0
        for i in range(1, len(s)):
            score += abs(ord(s[i - 1]) - ord(s[i]))
        return score


c = Solution()
s = "hello"
print(c.scoreOfString(s))
