from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []

        for i, word in enumerate(words):
            if x in word:
                res.append(i)

        return res


c = Solution()
words = ["leet", "code"]
x = "e"
print(c.findWordsContaining(words, x))
words = ["abc", "bcd", "aaaa", "cbc"]
x = "a"
print(c.findWordsContaining(words, x))
