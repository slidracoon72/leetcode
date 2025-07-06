class Solution:
    def merge_alternately(self, word1: str, word2: str) -> str:
        result = []
        for i in range(min(len(word1), len(word2))):
            result.append(word1[i] + word2[i])

        return ''.join(result) + word1[i + 1:] + word2[i + 1:]

    # Alternate solution
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        l1, l2 = len(word1), len(word2)
        for i in range(min(l1, l2)):
            res += word1[i]
            res += word2[i]

        if l1 > l2:
            res += word1[i + 1:]
        elif l2 > l1:
            res += word2[i + 1:]

        return res


word1 = "absxc"
word2 = "pqrs"

c = Solution()
print(c.merge_alternately(word1, word2))
