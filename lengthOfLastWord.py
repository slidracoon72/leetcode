class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        return len(a[-1])


c = Solution()
print(c.lengthOfLastWord("luffy is still joyboy"))
