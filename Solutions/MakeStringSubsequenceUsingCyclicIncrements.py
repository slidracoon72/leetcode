class Solution:
    # Time: O(N), Space: O(1)
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                j += 1
            else:
                next_char = (ord(str1[i]) - ord("a") + 1) % 26
                next_char = chr(next_char + ord("a"))
                if next_char == str2[j]:
                    j += 1
            i += 1

        return j == len(str2)


c = Solution()
str1 = "abc"
str2 = "ad"
print(c.canMakeSubsequence(str1, str2))
