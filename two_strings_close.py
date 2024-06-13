class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        d1 = {}
        d2 = {}

        for c in word1:
            if c in d1:
                d1[c] += 1
            else:
                d1[c] = 1

        for c in word2:
            if c in d2:
                d2[c] += 1
            else:
                d2[c] = 1

        # print(d1)
        # print(d2)

        keys1 = d1.keys()
        keys2 = d2.keys()

        v1 = list(d1.values())
        v2 = list(d2.values())

        v1.sort()
        v2.sort()

        # print(keys1)
        # print(keys2)
        #
        # print(v1)
        # print(v2)

        return keys1 == keys2 and v1 == v2


c = Solution()
word1 = "aaabbbbccddeeeeefffff"
word2 = "aaaaabbcccdddeeeeffff"
print(c.closeStrings(word1, word2))
