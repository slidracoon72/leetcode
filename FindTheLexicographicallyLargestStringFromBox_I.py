# LC - 3403: Find the Lexicographically Largest String From the Box I
# DO AGAIN

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        res = ""
        for i in range(n):
            res = max(res, word[i: min(i + n - numFriends + 1, n)])
        return res


c = Solution()
word = "dbca"
numFriends = 2
print(c.answerString(word, numFriends))
