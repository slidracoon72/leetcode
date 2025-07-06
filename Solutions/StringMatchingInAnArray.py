from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        res = []
        for i in range(n):
            cur = words[i]
            for j in range(n):
                if i == j:
                    continue
                if cur in words[j]:
                    res.append(cur)
                    break
        return res

    def stringMatching1(self, words: List[str]) -> List[str]:
        words_set = set(words)
        res = set()

        for word in words:
            if word in res:
                continue

            for i in range(len(word)):
                for j in range(len(word)):
                    sub = word[i:j + 1]
                    if sub in words_set and sub != word:
                        res.add(sub)

        return list(res)


c = Solution()
words = ["mass", "as", "hero", "superhero"]
print(c.stringMatching(words))
print(c.stringMatching1(words))
