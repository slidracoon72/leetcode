class Solution:
    def merge_alternately(self, word1: str, word2: str) -> str:
        result = []
        for i in range(min(len(word1), len(word2))):
            result.append(word1[i] + word2[i])

        return ''.join(result) + word1[i + 1:] + word2[i + 1:]

    # Alternate solution
    def mergeAlternately2(self, word1: str, word2: str) -> str:
        merged = ""
        w1 = len(word1)
        w2 = len(word2)
        smaller = min(w1, w2)

        for i in range(smaller):
            merged += word1[i]
            merged += word2[i]

        if w1 > w2:
            merged += word1[smaller:]
        elif w2 > w1:
            merged += word2[smaller:]

        return merged


word1 = "absxc"
word2 = "pqrs"

c = Solution()
print(c.merge_alternately(word1, word2))
