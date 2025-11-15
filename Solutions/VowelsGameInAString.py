class Solution:
    # Time: O(n), Space: O(1)
    def doesAliceWin(self, s: str) -> bool:
        vowels = "aeiou"
        for c in s:
            if c in vowels:
                return True

        return False


c = Solution()
print(c.doesAliceWin("leetcoder"))
print(c.doesAliceWin("bbcd"))
