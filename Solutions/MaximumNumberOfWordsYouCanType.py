class Solution:
    # Time: O(n), Space: O(n)
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        broken = set(brokenLetters)

        res = 0
        for word in words:
            flag = True
            for c in word:
                if c in broken:
                    flag = False
                    break
            if flag:
                res += 1

        return res


c = Solution()

text = "hello world"
brokenLetters = "ad"
print(c.canBeTypedWords(text, brokenLetters))

text = "leet code"
brokenLetters = "e"
print(c.canBeTypedWords(text, brokenLetters))
